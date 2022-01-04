from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from .models import Correlation, Metric, Dora_kpi, Team, SuggestedRecommendation, Measurement
import pandas as pd
def get_n_latest_measurements(team,n, find_fp_metric):
        # get latest mesaurements if they exist
        if len(team.metric_history.all())==0:
            return None
        else:
            measurements = team.metric_history.all().order_by('-measured_at')[0:n]
        # get all metrics objects
        if find_fp_metric:
            metrics = {measurement.object_id : measurement.value for measurement in measurements if measurement.object_id > 100}
            return metrics
        else:
            dora_kpis = {measurement.object_id : measurement.value for measurement in measurements if measurement.object_id < 100}
            return dora_kpis
def rate_measurement(object_id,value):
        metric_object = Dora_kpi.objects.get(id=object_id) if object_id<10 else Metric.objects.get(id=object_id)
        if metric_object.elite_threshold_value:
            if value >= metric_object.elite_threshold_value:
                return ("elite",3)
            if value >= metric_object.high_threshold_value:
                return ("high",2)
            if value >= metric_object.medium_threshold_value:
                return ("medium",1)
            return ("low",0)
        return (None,4)

def extract_worst_metrics(metric_rating, n_metrics):
    assert n_metrics <= len(metric_rating)
    sorted_metric_rating=sorted(metric_rating.keys(), key=lambda x: metric_rating[x][1], reverse=False)
    return sorted_metric_rating[0:n_metrics]
    
def extract_n_recommendations (worst_metrics, n_recommendations):
    recommendations = []
    metric_recommendations = {metric:list(metric.recommendations.all()) for metric in worst_metrics}
    while len(worst_metrics)>0 and n_recommendations>0:
        for metric in metric_recommendations.keys():
            recommendation_set = metric_recommendations[metric]
            if len(recommendation_set)>0:
                recommendations.append(recommendation_set.pop(0))
            else:
                recommendations.append(recommendation_set)
                del metric_recommendations[metric]
            if len(recommendations)==n_recommendations:
                return recommendations
    return None

def most_correlated_metrics (metrics,worst_doras):
    values = {}
    for correlation_pair in Correlation.objects.all():
        dora = correlation_pair.dora_kpi
        if dora not in worst_doras:
            continue
        metric=correlation_pair.metric
        correlation = correlation_pair.value
        values[metric]=correlation*metrics[metric.id]
    sort_correlated = sorted(values.items(), key=lambda x: x[1], reverse=True)
    most_correlated = [ metric_value_tuple[0] for metric_value_tuple in sort_correlated]
    return most_correlated

def generate_recommendations_with_correlations(metrics, dora_kpis):
    dora_rating = {dora_kpi_id: rate_measurement(dora_kpi_id, dora_kpi_value) for dora_kpi_id, dora_kpi_value in dora_kpis.items()}
    low_medium_doras = {k: v for k, v in dora_rating.items() if v[1] == 0 or v[1] == 1}
    high_doras = {k: v for k, v in dora_rating.items() if v[1] == 2}
    worst_doras = low_medium_doras if len(low_medium_doras)>0 else high_doras
    if len(worst_doras) == 0:
        return None
    most_correlated = most_correlated_metrics(metrics, worst_doras.keys())
    recommendations = extract_n_recommendations (most_correlated, 5)
    if recommendations:
        return recommendations 
    else:
        return None
def generate_recommendations_without_correlations(metrics, dora_kpis):
    # without using correlations: find the metrics to improve on:
    metric_rating = {Metric.objects.get(id=metric_id):rate_measurement(metric_id,metrics[metric_id])  for metric_id in metrics}
    worst_metrics = extract_worst_metrics(metric_rating, 3)
    recommendations = extract_n_recommendations (worst_metrics, 5)
    return recommendations
class Recommender(object):
    def __init__(self):
        self.n_dora_kpis = 4 
        self.n_metrics = 24
   
    def generate_recommendations(self, team):        
        metrics = get_n_latest_measurements(team,self.n_metrics+self.n_dora_kpis, True)
        dora_kpis = get_n_latest_measurements(team, self.n_metrics+self.n_dora_kpis, False)
        recommendations = generate_recommendations_with_correlations(metrics,dora_kpis)
        if recommendations:
            return recommendations 
        else:
            return generate_recommendations_without_correlations(metrics,dora_kpis)
            
if __name__=="__main__":
    Recommender().generate_recommendations(Team.objects.get(id=1))
