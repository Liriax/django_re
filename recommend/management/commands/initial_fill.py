from django.core.management.base import BaseCommand
# import pandas as pd
from recommend.submodels.Recommendation import Recommendation
from recommend.submodels.Metric import Metric
class Command(BaseCommand):
    help = 'import booms'

    

    def handle(self, *args, **options):

    # Code for initial Metric initialisation
        #df=pd.read_csv('metrics.csv', sep=';', encoding= 'unicode_escape')
        #for ID,NAME in zip(df.ID,df.Name):
        #    models=Metric(id=ID,name=NAME)
        #    models.save()


        # df=pd.read_csv('recommendations.csv',sep=';' , encoding= 'unicode_escape')
        # for ID,HEADLINE,DISCRIPTION in zip(df.ID,df.Headline,df.Description):
        #   models=Recommendation(encoded_id=ID,headline=HEADLINE,description=DISCRIPTION)
        #   models.save()
        for recommendation in Recommendation.objects.all():
          encoded_id = str(recommendation.encoded_id)[0:3]
          # print(encoded_id)
          recommendation.metric = Metric.objects.get(id=int(encoded_id))
          recommendation.save()

       