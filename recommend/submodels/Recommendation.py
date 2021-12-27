from django.db import models
from .Metric import Metric
class Recommendation(models.Model):
    encoded_id = models.IntegerField(primary_key=True) # starts from 10101
    headline = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    metric = models.ForeignKey(Metric,
                            on_delete=models.CASCADE,
                            related_name='recommendations')
    weight = models.FloatField(default=1)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.headline