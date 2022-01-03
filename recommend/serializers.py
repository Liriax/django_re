from rest_framework import serializers
from .models import Recommendation, SuggestedRecommendation

class SuggestedRecommendationSerializer(serializers.ModelSerializer):
    recommendation_headline = serializers.CharField(source='recommendation.headline')
    recommendation_description = serializers.CharField(style={'base_template': 'textarea.html'},source='recommendation.description')
    team_name = serializers.CharField(source='team.name')
    class Meta:
        fields = (
            'id',
            'recommendation',
            'team',
            'created_at',
            'updated_at',
            'status',
            'confidence',
            'recommendation_headline',
            'recommendation_description',
            'team_name'
        )
        model = SuggestedRecommendation