from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Metric(models.Model):
    name = models.CharField(max_length=250)
    # max, min, metric levels, source, explanation
    def __str__(self):
        return self.name
class Dora_kpi(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
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
    def __str__(self):
        return self.body
class Measurement (models.Model):
    measured_at = models.DateTimeField(default=timezone.now)
    metric1=models.FloatField()       
    metric2=models.FloatField()       
    metric3=models.FloatField()       
    metric4=models.FloatField()       
    metric5=models.FloatField()
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='metric_history')
class Correlation (models.Model):
    dora_kpi = models.ForeignKey(Dora_kpi,
                                on_delete=models.CASCADE,
                                related_name='correlations')   
    metric = models.ForeignKey(Metric,
                                on_delete=models.CASCADE,
                                related_name='correlations')
    value = models.FloatField(default=1)
    class Meta:
        unique_together = (("dora_kpi", "metric"),)
    def __str__(self):
        return f"{self.dora_kpi}, {self.metric}, {self.value}"
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
        
