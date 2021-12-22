from django.db import models

class Dora_kpi(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    class Meta:
        app_label = 'recommend'