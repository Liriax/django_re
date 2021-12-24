from django.db import models
class Metric(models.Model):
    id = models.IntegerField(primary_key=True) # starts from 101
    name = models.CharField(max_length=250)
    max_value = models.FloatField(blank=True)
    min_value = models.FloatField(default=0,blank=True)
    medium_threshold_value = models.FloatField(blank=True)
    high_threshold_value = models.FloatField(blank=True)
    elite_threshold_value = models.FloatField(blank=True)
    low_level = models.BooleanField(default=False)
    source = models.CharField(max_length=100,blank=True)
    class Meta:
        app_label = 'recommend'
    def __str__(self):
        return self.name