from django.db import models
from django.utils import timezone
from .Team import Team
from .Recommendation import Recommendation

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
    
        
    # weight/rank?
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f"recommendation {self.recommendation} for team {self.team.name} on {self.created_at}, {self.status}"
        
