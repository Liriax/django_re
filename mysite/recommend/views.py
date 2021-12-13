from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import ListView

class PostListView(ListView):
    queryset = SuggestedRecommendation.objects.all()
    # paginate_by = 3
    context_object_name = 'recommendations'
    template_name = 'recommend/team/list.html' 
    
# Create your views here.
def team_recommendations (request, id, year, month, day):
    team = Team.objects.get(id=id)
    recommendations = SuggestedRecommendation.objects.filter(
                                        created_at__year=year,
                                        created_at__month=month,
                                        created_at__day=day,
                                        team = team)
    return render(request,
                  'recommend/team/recommendations.html',
                  {'recommendations':recommendations,
                   'team':team})