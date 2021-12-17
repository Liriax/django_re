from django.forms.models import model_to_dict
from .models import Correlation, Metric, Dora_kpi, Team
from django.db.models import Max

class Recommender(object):
    def __init__(self):
        self.n_dora_kpis = 2
        self.n_metrics = 5
        self.n_recommendations_per_metric = 1
    def generate_recommendations(self, team):
        # print(team.metric_history.latest('measured_at'))
        values = model_to_dict(team.metric_history.latest('measured_at'))
        metrics = [values.get(x) for x in values.keys() if "metric" in x]
        # print(metrics)
        correlations = [[1 for x in range(0,self.n_dora_kpis)] for x in range(0,self.n_metrics)]
        for correlation_pair in Correlation.objects.all():
            dora = correlation_pair.dora_kpi
            metric=correlation_pair.metric
            value = correlation_pair.value
            correlations[metric.id-1][dora.id-1]=value
        # print(correlations)
        
        most_correlated = []
        for dora in Dora_kpi.objects.all():
            metrics_weight = [(metric.id, correlations[metric.id-1][dora.id-1] * metrics[metric.id-1]) for metric in Metric.objects.all()]
            metrics_weight.sort(key=lambda x: x[1], reverse=True)
            most_correlated.append(Metric.objects.get(id = metrics_weight[0][0]))
        # print(most_correlated)
        recommendations = [metric.recommendations.all()[0] for metric in most_correlated]
        print(recommendations)
        return recommendations
            
Recommender().generate_recommendations(Team.objects.get(id=1))
