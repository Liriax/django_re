
from django.db import migrations

def create_data(apps, schema_editor):
    Team = apps.get_model('recommend', 'Team')
    Metric = apps.get_model('recommend', 'Metric')
    Recommendation = apps.get_model('recommend', 'Recommendation')
    SuggestedRecommendation = apps.get_model('recommend', 'SuggestedRecommendation')
    team1=Team(name="Team 1", contact_person="admin")
    team1.save()
    metric1=Metric(name="Metric 1", id=101)
    metric1.save()
    recommendation1 = Recommendation(encoded_id=10101, headline="Recommendation 1", metric=metric1)
    recommendation1.save()
    SuggestedRecommendation(recommendation=recommendation1, team=team1).save()




class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
                migrations.RunPython(create_data),
    ]
