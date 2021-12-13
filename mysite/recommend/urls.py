from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('',views.PostListView.as_view()),
    path('<int:id>/<int:year>/<int:month>/<int:day>/',
         views.team_recommendations,
         name = 'team_recommendations'),

]
