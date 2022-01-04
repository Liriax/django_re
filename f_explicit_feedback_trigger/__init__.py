import logging
import azure.functions as func
from recommend.models import SuggestedRecommendation
from recommend.submodels.Recommendation import Recommendation
# frontend should trigger an url like:
# http://localhost:7071/api/f_explicit_feedback_trigger?id=10&score=5
# with paramters 'id' and 'score'
# url pattern: http://localhost:7071/api/f_explicit_feedback_trigger?id={int}&score={int}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    id = req.params.get('id')
    score = req.params.get('score')

    if not id or not score:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')
            score = req_body.get('score')

    if not (id and score):
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass the object id and the feedback score in the query string or in the request body.",
             status_code=200
        )
        
    try:
        suggReco = SuggestedRecommendation.objects.get(id=id)
    except:
        return func.HttpResponse(
             f"Suggested Recommendation object with id={id} does not exist",
             status_code=404
        )
        
    if suggReco.score:
        return func.HttpResponse(
             f"Feedback for Suggested Recommendation object with id={id} has already been used for explicit learning.",
             status_code=200
        )
    
    
    learning_rate=0.1 # how much the score is taken into account for the learning
    
    reco = suggReco.recommendation
    original_weight = reco.weight
    new_weight = float(original_weight)*(1-learning_rate) + learning_rate * int(score)/5
    reco.weight = new_weight
    reco.save()
    
    suggReco.score = score
    suggReco.save()
    
    reco_id = reco.encoded_id
    return func.HttpResponse(f'''Suggested Recommendation object with id={id} and score={score}. This HTTP triggered function executed successfully.\n
                            learning rate: {learning_rate} \n
                             Old weight of recommendation {reco_id}: {original_weight} -> New weight {new_weight}''')