from rest_framework import serializers
from .models import Recommendation, SuggestedRecommendation

class SuggestedRecommendationSerializer(serializers.ModelSerializer):
    recommendation_body = serializers.CharField(source='recommendation.body')
    team_name = serializers.CharField(source='team.name')
    class Meta:
        fields = (
            'id',
            'recommendation',
            'team',
            'created_at',
            'status',
            'recommendation_body',
            'team_name'
        )
        model = SuggestedRecommendation