from django.urls import path, re_path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('',views.PostListView.as_view()),
    # path('api/',views.ListSuggestedRecommendations.as_view()),
    re_path(r'^api/$',views.api_recommendations_list),
    path('api/<int:id>/',views.api_recommendations_detail),
    path('api/team/<int:id>/',views.api_recommendations_team),
    path('<int:id>/',views.team_recommendations),
    path('<int:id>/<int:year>/<int:month>/<int:day>/',
         views.team_time_recommendations,
         name = 'team_recommendations'),
    path('api/<int:id>/<int:measurement_id>/', views.api_dora_kpi)
]
