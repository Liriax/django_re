from django.db import models
from .Dora_kpi import Dora_kpi
from .Metric import Metric

class Correlation (models.Model):
    dora_kpi = models.ForeignKey(Dora_kpi,
                                on_delete=models.CASCADE,
                                related_name='correlated_metrics')   
    metric = models.ForeignKey(Metric,
                                on_delete=models.CASCADE,
                                related_name='correlated_dora_kpis')
    value = models.FloatField(default=1)
    class Meta:
        unique_together = (("dora_kpi", "metric"),)
    def __str__(self):
        return f"{self.dora_kpi}, {self.metric}, {self.value}"