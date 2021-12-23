from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import ListView
from rest_framework import generics
from .serializers import SuggestedRecommendationSerializer
from .Recommender import Recommender


class PostListView(ListView):
    queryset = SuggestedRecommendation.objects.all()
    # paginate_by = 3
    context_object_name = 'recommendations'
    template_name = 'recommend/list.html' 

def team_recommendations (request, id):
    team = Team.objects.get(id=id)
    generated_recommendations = Recommender().generate_recommendations(team)
    return render(request,
                  'recommend/team/latest_recommendations.html',
                  {
                   'recommendations':generated_recommendations,
                   'team':team
                   })
    
def team_time_recommendations (request, id, year, month, day):
    team = Team.objects.get(id=id)

    past_recommendations = SuggestedRecommendation.objects.filter(
                                        created_at__year=year,
                                        created_at__month=month,
                                        created_at__day=day,
                                        team = team)
    return render(request,
                  'recommend/team/recommendations.html',
                  {
                   'recommendations':past_recommendations,
                   'team':team
                   })
    
# api views:
class ListSuggestedRecommendations(generics.ListCreateAPIView):
    queryset = SuggestedRecommendation.objects.all()
    serializer_class = SuggestedRecommendationSerializer
    
class DetailSuggestedRecommendations(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuggestedRecommendation.objects.all()
    serializer_class = SuggestedRecommendationSerializer