from rest_framework import serializers
from .models import SuggestedRecommendation, Measurement

class SuggestedRecommendationSerializer(serializers.ModelSerializer):
    recommendation_headline = serializers.CharField(source='recommendation.headline')
    team_name = serializers.CharField(source='team.name')
    class Meta:
        fields = (
            'id',
            'recommendation',
            'team',
            'created_at',
            'status',
            'recommendation_headline',
            'team_name'
        )
        model = SuggestedRecommendation

class MeasurementObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Metric):
            return f'Metric: {value.name}'
        elif isinstance(value, Dora_kpi):
            return f'DORA KPI: {value.name}'
        raise Exception('Unexpected type of tagged object')
        
class MeasurementSerializer(serializers.ModelSerializer):
    measured_metric = MeasurementObjectRelatedField(read_only=True)
    team_name = serializers.CharField(source='team.name')
    class Meta:
        fields=(
            'id',
            'measured_at',
            'measured_metric',
            'object_id',
            'value',
            'team',
            'team_name'
        )
        model=Measurement