from django.db import models
from django.utils import timezone
from .Team import Team
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