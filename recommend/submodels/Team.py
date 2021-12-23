from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        ordering = ('-name',)
        app_label = 'recommend'
    def __str__(self):
        return self.name