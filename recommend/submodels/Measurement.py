from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from .Dora_kpi import Dora_kpi
from .Metric import Metric
from .Team import Team
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Measurement (models.Model):
    limit = models.Q(app_label='recommend', model='dora_kpi') | models.Q(app_label='recommend', model='metric')
    measured_at = models.DateTimeField(default=timezone.now)
    # measurement_json = models.JSONField(default=default_measurement())
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE,limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    measured_metric = GenericForeignKey('content_type','object_id')
    value = models.FloatField()
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='metric_history')
    rating = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return f"Metric {self.measured_metric.name} measured at {self.measured_at} for team {self.team.name}"