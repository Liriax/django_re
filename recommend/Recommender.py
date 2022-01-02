from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from .models import Correlation, Metric, Dora_kpi, Team, SuggestedRecommendation
from django.db.models import Max

def get_n_latest_measurements(team,n):
        # get latest mesaurements if they exist
        if len(team.metric_history.all())==0:
            return None
        else:
            measurements = team.metric_history.all().order_by('-measured_at')[0:n]
        # get all metrics objects
    
        metrics = {measurement.object_id : measurement.value for measurement in measurements if "metric" in str(measurement.content_type)}
        return metrics
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
    while True:
        for metric in metric_recommendations.keys():
            recommendation_set = metric_recommendations[metric]
            if len(recommendation_set)>0:
                recommendations.append(recommendation_set.pop(0))
            else:
                recommendations.append(recommendation_set)
                del metric_recommendations[metric]
            if len(recommendations)==n_recommendations:
                return recommendations
    
class Recommender(object):
    def __init__(self):
        self.n_dora_kpis = 4 # change this
        self.n_metrics = 24 # change this
        self.n_recommendations_per_metric = 1 # dynamic change?
        
    def get_correlation_matrix(self):
        # define initial correlation matrix
        correlations = [[1 for x in range(0,self.n_dora_kpis)] for x in range(0,self.n_metrics)]
        # fill correlation matrix with values
        for correlation_pair in Correlation.objects.all():
            dora = correlation_pair.dora_kpi
            metric=correlation_pair.metric
            value = correlation_pair.value
            correlations[metric.id-101][dora.id-1]=value
        return correlations
    
    def generate_recommendations(self, team):
        # TODO: refractor this method!
        
        metrics = get_n_latest_measurements(team,self.n_metrics+self.n_dora_kpis)
        # correlations = self.get_correlation_matrix()
        # dora_kpis = Dora_kpi.objects.all()
        # TODO: find the dora kpis to improve
        
        # # find the most correlated metrics
        # values = {}
        # for correlation_pair in Correlation.objects.all():
        #     dora = correlation_pair.dora_kpi
        #     metric=correlation_pair.metric
        #     correlation = correlation_pair.value
        #     values[metric]=correlation*metrics[metric.id]
        # # print(values)
        # sort_correlated = sorted(values.items(), key=lambda x: x[1], reverse=True)
        # most_correlated = [ metric_value_tuple[0] for metric_value_tuple in sort_correlated]
        # # get the top 1 corresponding recommendations -> TODO: set the number of recommendations per metric
        # recommendations = [metric.recommendations.all()[0] for metric in most_correlated]
        
        # without using correlations: find the metrics to improve on:
        metric_rating = {Metric.objects.get(id=metric_id):rate_measurement(metric_id,metrics[metric_id])  for metric_id in metrics}
        worst_metrics = extract_worst_metrics(metric_rating, 3)
        recommendations = extract_n_recommendations (worst_metrics, 5)
        
        # add newly generated recommendations to the database:
        for recommendation in recommendations:
            SuggestedRecommendation.objects.create(recommendation=recommendation, team=team)
        return recommendations
            
if __name__=="__main__":
    Recommender().generate_recommendations(Team.objects.get(id=1))
