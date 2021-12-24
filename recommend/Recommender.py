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
class Recommender(object):
    def __init__(self):
        self.n_dora_kpis = 1 # change this
        self.n_metrics = 1 # change this
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
        
        metrics = get_n_latest_measurements(team,1)
        correlations = self.get_correlation_matrix()
        print(metrics)
        dora_kpis = Dora_kpi.objects.all()
        # TODO: find the dora kpis to improve
        
        # find the most correlated metrics
        values = {}
        for correlation_pair in Correlation.objects.all():
            dora = correlation_pair.dora_kpi
            metric=correlation_pair.metric
            correlation = correlation_pair.value
            values[metric]=correlation*metrics[metric.id]
        print(values)
        sort_correlated = sorted(values.items(), key=lambda x: x[1], reverse=True)
        most_correlated = [ metric_value_tuple[0] for metric_value_tuple in sort_correlated]
        # get the top 1 corresponding recommendations -> TODO: set the number of recommendations per metric
        recommendations = [metric.recommendations.all()[0] for metric in most_correlated]
        print(recommendations)
        
        # add newly generated recommendations to the database:
        for recommendation in recommendations:
            new_recommendation = SuggestedRecommendation.objects.create(recommendation=recommendation, team=team)
        return recommendations
            
if __name__=="__main__":
    Recommender().generate_recommendations(Team.objects.get(id=1))
