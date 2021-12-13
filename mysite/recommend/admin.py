from django.contrib import admin
from .models import Recommendation, Metric, Team, SuggestedRecommendation
# Register your models here.

admin.site.register(Recommendation)
admin.site.register(Metric)
admin.site.register(Team)
admin.site.register(SuggestedRecommendation)