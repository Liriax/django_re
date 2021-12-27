from django.db import models

class Dora_kpi(models.Model):
    name = models.CharField(max_length=250)
    max_value = models.FloatField(blank=True,null=True)
    min_value = models.FloatField(default=0,blank=True,null=True)
    medium_threshold_value = models.FloatField(blank=True,null=True)
    high_threshold_value = models.FloatField(blank=True,null=True)
    elite_threshold_value = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        app_label = 'recommend'