from app.shared.database.dynamodb_client import DynamodbClient
from app.shared.models import FeedbackModel
from app.shared.common.recaptcha import CaptchaValidation

def main(payload: dict) -> dict:
    rating = payload.get('rating')
    comment = payload.get('comment')
    captchaToken = payload.get('captchaToken')

    if not rating or not comment or not captchaToken:
        return ({'message': 'Missing parameters'}, 400)

    # Captcha verification
    captcha = CaptchaValidation()
    if not captcha.validate(captchaToken):
        return ({'message': 'Captcha validation failed'}, 400)

    # Prepare feedback model
    feedback = FeedbackModel()
    feedback.rating = rating
    feedback.comment = comment
    feedback.captchaToken = captchaToken

    # Push data in dynamodb feedback partition
    dynamodb = DynamodbClient()
    dynamodb.feedback.put(feedback)
    
    return ({'message': 'Success'}, 200)