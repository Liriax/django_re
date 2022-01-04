from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SuggestedRecommendationSerializer, MeasurementSerializer
from .Recommender import Recommender, rate_measurement
import pandas as pd
import re

class PostListView(ListView):
    queryset = SuggestedRecommendation.objects.all()
    # paginate_by = 3
    context_object_name = 'recommendations'
    template_name = 'recommend/list.html' 

def generate_correlations (request):
    df = pd.DataFrame.from_records(Measurement.objects.all().values())
    df["measured_at"]=re.match("^[^:]*",str(df["measured_at"])).group()
    df["rating"]=df.apply(lambda x: rate_measurement(x["object_id"],x["value"])[1],axis=1)
    df = df.groupby(by=["measured_at","team_id"])\
        .apply(lambda x: dict(zip(zip(x['object_id'],x['content_type_id']), x['rating'])))\
        .reset_index(name='measurements')
    measurement_list= list(df.iloc[:,2])
    measurement_df = pd.DataFrame.from_records(measurement_list)
    measurement_df = measurement_df.reindex(sorted(measurement_df.columns), axis=1)
    correlation = {}
    for x in range(0,4):
        dora_column=measurement_df.iloc[:,x]
        for y in range(4,28):
            metric_column=measurement_df.iloc[:,y]
            correlation[(dora_column.name, metric_column.name)] = dora_column.corr(metric_column) 
    try:  
        for x, y in correlation.items():
            dora_kpi = Dora_kpi.objects.get(id=x[0][0])
            metric = Metric.objects.get(id=x[1][0])
            Correlation.objects.create(dora_kpi=dora_kpi, metric=metric, value=y)
        return HttpResponse('generated correlations')
    except:
        return HttpResponse('Failed: not enough measurements?')
        
    
def team_recommendations (request, id):
    team = Team.objects.get(id=id)
    generated_recommendations = Recommender().generate_recommendations(team)
    # add newly generated recommendations to the database:
    if generated_recommendations and len(generated_recommendations)>0:
        for recommendation in generated_recommendations:
            SuggestedRecommendation.objects.create(recommendation=recommendation, team=team)
        return render(request,
                    'recommend/team/latest_recommendations.html',
                    {
                    'recommendations':generated_recommendations,
                    'team':team
                    })
    else:
        return HttpResponse('Error generating recommendations: no recommendations generated')
    
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

@api_view(['PUT', 'DELETE', 'GET'])
def api_recommendations_detail(request, id):
    try:
        recommendation = SuggestedRecommendation.objects.get(id=id)
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

    #get
    elif request.method == 'GET':
            serializer = SuggestedRecommendationSerializer(recommendation, context={'request': request})
            return Response(serializer.data)
    
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