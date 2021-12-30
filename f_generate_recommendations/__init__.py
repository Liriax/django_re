# import datetime
# import logging

# import azure.functions as func
# from recommend.Recommender import Recommender
# from recommend.models import Team
# def main(mytimer: func.TimerRequest) -> None:
#     utc_timestamp = datetime.datetime.utcnow().replace(
#         tzinfo=datetime.timezone.utc).isoformat()

#     if mytimer.past_due:
#         logging.info('The timer is past due!')

#     recommender = Recommender()
#     for team in Team.objects.all():
#         recommender.generate_recommendations(team)
        
#     logging.info('Python timer trigger function ran at %s', utc_timestamp)

import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)