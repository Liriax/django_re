from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=250,null=True)
    class Meta:
        ordering = ('-name',)
        app_label = 'recommend'
    def __str__(self):
        return self.name