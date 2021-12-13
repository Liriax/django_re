from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Metric(models.Model):
    name = models.CharField(max_length=250)
    # max, min, metric levels, source, explanation

class Team(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name
        
class Recommendation(models.Model):
    body = models.TextField()
    metric = models.ForeignKey(Metric,
                            on_delete=models.CASCADE,
                            related_name='recommendations')
    
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
        
