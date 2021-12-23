from .models import *

def create_five_test_teams():
    Team.objects.create(name='',
                        contact_person='')
'''
def create_dora_kpis():
    Dora_kpi.objects.create(name =,
                            max_value =,
                            min_value =,
                            medium_threshold_value =,
                            high_threshold_value =,
                            elite_threshold_value =,)
def create_fp_metrics():
    Metric.objects.create(name =,
                            max_value =,
                            min_value =,
                            medium_threshold_value =,
                            high_threshold_value =,
                            elite_threshold_value =,
                            low_level=,
                            source=,)
def create_recommendations():
    Recommendation.objects.create(headline = "",
                                    description = "",
                                    metric = ,
                                    weight = ,
                                    active = ,)
def create_correlations():
    Correlation.objects.create(dora_kpi=,
                               metric=,
                               value=,)
def create_measurements():
    Measurement.objects.create(measured_at=,
                               value=,
                               content_type=, #dora kpi or metric?
                               object_id=, #id of the dora kpi or metric
                               team=,)
    
    '''