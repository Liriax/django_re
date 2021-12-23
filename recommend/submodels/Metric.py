from django.db import models
class Metric(models.Model):
    name = models.CharField(max_length=250)
    # max, min, metric levels, source, explanation
    class Meta:
        app_label = 'recommend'
    def __str__(self):
        return self.name