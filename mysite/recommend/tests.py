from django.test import TestCase

# Create your tests here.
from .models import Recommendation, Team, SuggestedRecommendation
from .Recommender import Recommender

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Team.objects.create(name='Team A')
        Team.objects.create(name='Team B')
        Team.objects.create(name='Team C')

    def test_title_content(self):
        team = Team.objects.get(id = 1)
        expected_object_name = f'{team.name}'
        self.assertEquals(expected_object_name, 'Team A')
