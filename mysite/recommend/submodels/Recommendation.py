from django.db import models
from .Metric import Metric
class Recommendation(models.Model):
    body = models.TextField()
    metric = models.ForeignKey(Metric,
                            on_delete=models.CASCADE,
                            related_name='recommendations')
    def __str__(self):
        return self.body