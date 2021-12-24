from rest_framework import serializers
from .models import Recommendation, SuggestedRecommendation

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