import json
from recommend.models import *

def create_five_test_teams():
    teams = []
    for x in range(1,6):
        teams.append({
            "model":"recommend.team",
            "pk":x,
            "fields":{
                "name":f"Team {x}",
                "contact_person":"admin"
            }
        })
    with open('recommend/fixtures/teams.json','w') as f:
        json.dump(teams,f)

def create_dora_kpis():
    dora_kpis=[
        {
            "model":"recommend.dora_kpi",
            "pk":1,
            "fields": {
                "name":"Change failure rate",
                # "max_value":
                # "min_value":
                # "medium_threshold_value":
                # "high_threshold_value":
                # "elite_threshold_value":
            }
        },
        {
            "model":"recommend.dora_kpi",
            "pk":2,
            "fields": {
                "name":"Deployment frequency",
            }
        }
    ]
    with open('recommend/fixtures/dora_kpis.json','w') as f:
        json.dump(dora_kpis,f)
   
# def create_fp_metrics():
#     Metric.objects.create(name =,
#                             max_value =,
#                             min_value =,
#                             medium_threshold_value =,
#                             high_threshold_value =,
#                             elite_threshold_value =,
#                             low_level=,
#                             source=,)
def create_recommendations():
    recommendations=[
        {
            "model":"recommend.recommendation",
            "pk": 10101,
            "fields":{
                ""
            }
        }
    ]

# def create_correlations():
#     Correlation.objects.create(dora_kpi=,
#                                metric=,
#                                value=,)
# def create_measurements():
#     Measurement.objects.create(measured_at=,
#                                value=,
#                                content_type=, #dora kpi or metric?
#                                object_id=, #id of the dora kpi or metric
#                                team=,)

def create_data():
    team1=Team(name="Team 1", contact_person="admin")
    team1.save()
    metric1=Metric(name="Metric 1", id=101)
    metric1.save()
    recommendation1 = Recommendation(encoded_id=10101, headline="Recommendation 1", metric=metric1)
    recommendation1.save()
    SuggestedRecommendation(recommendation=recommendation1, team=team1).save()
    
if __name__=="__main__":
    create_data()