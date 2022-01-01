from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SuggestedRecommendationSerializer, MeasurementSerializer
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
@api_view(['GET', 'POST'])
def api_recommendations_list(request):
    # read all recommendations
    if request.method == 'GET':
        data = SuggestedRecommendation.objects.all()

        serializer = SuggestedRecommendationSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    # create new recommendation from API -> should be forbidden
    elif request.method == 'POST':
        serializer = SuggestedRecommendationSerializer(data=request.data)
        # ensure that the data received is conformed with our model
        if serializer.is_valid(): 
            # If all is fine, we save it to the database
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def api_recommendations_detail(request, pk):
    try:
        recommendation = SuggestedRecommendation.objects.get(pk=pk)
    except SuggestedRecommendation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # update status
    if request.method == 'PUT':
        try:
            recommendation.status = request.data['status']
            recommendation.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            print("failed updating data [PUT]")

    # delete
    elif request.method == 'DELETE':
        recommendation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def api_recommendations_team(request, id):
    try:
        team = Team.objects.get(id=id)
        data = SuggestedRecommendation.objects.filter(team = team)
    except:
        print(f'error getting recommendations for team {id}')
        data = []
    serializer = SuggestedRecommendationSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

class DetailSuggestedRecommendations(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuggestedRecommendation.objects.all()
    serializer_class = SuggestedRecommendationSerializer

@api_view(['GET'])
def api_dora_kpi(request, id, measurement_id):
    try:
        team = Team.objects.get(id=id)
        data = Measurement.objects.filter(team=team).filter(object_id=measurement_id)
    except:
        print(f'error getting dora kpis for team {id}')
        data = []
    serializer = MeasurementSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)