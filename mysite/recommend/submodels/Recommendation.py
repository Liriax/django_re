from django.db import models
from .Metric import Metric
class Recommendation(models.Model):
    headline = models.CharField(max_length=250)
    description = models.TextField(null=True)
    metric = models.ForeignKey(Metric,
                            on_delete=models.CASCADE,
                            related_name='recommendations')
    weight = models.FloatField(default=1)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.headline