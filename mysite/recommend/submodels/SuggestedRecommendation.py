from django.db import models
from django.utils import timezone
from .Team import Team
from .Recommendation import Recommendation

class RecommendationScores(models.IntegerChoices):
    TERRIBLE = 1
    BAD = 2
    OK = 3
    GOOD = 4
    HELPFUL = 5 
class SuggestedRecommendation(models.Model):
    STATUS_CHOICES = (
        ('suggested','SUGGESTED'),
        ('implemented',"IMPLEMENTED"),
        ('rejected',"REJECTED")
    )
    
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='suggested')
    recommendation = models.ForeignKey(Recommendation,
                                       on_delete = models.CASCADE,
                                       related_name="recommendations")
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='recommendations')
    confidence = models.FloatField(null=True) 
    # explicit feedback section:
    updated_at = models.DateTimeField(null=True)
    feedback = models.TextField(null=True)
    score = models.IntegerField(choices=RecommendationScores.choices,null=True)
       
    # weight/rank?
    class Meta:
        unique_together = (("created_at", "team"),)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f"recommendation {self.recommendation} for team {self.team.name} on {self.created_at}, {self.status}"
        
