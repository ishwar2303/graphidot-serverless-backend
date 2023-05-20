from app.shared.common.recaptcha import CaptchaValidation
from app.shared.database.dynamodb_client import DynamodbClient
from app.shared.models import CustomerReviewModel

def main(payload: dict) -> dict:
    firstName = payload.get('firstName')
    lastName = payload.get('lastName')
    email = payload.get('email')
    serviceName = payload.get('serviceName')
    comment = payload.get('comment')
    overallRating = payload.get('overallRating')
    refer = payload.get('refer')
    expectation = payload.get('expectation')
    subscribe = payload.get('subscribe')
    captchaToken = payload.get('captchaToken')

    if not firstName or not email or not serviceName or not comment or not overallRating or not refer or not expectation or not subscribe or not captchaToken:
        return ({'message': 'Missing parameters'}, 400)

    # Captcha verification
    captcha = CaptchaValidation()
    if not captcha.validate(captchaToken):
        return ({'message': 'Captcha validation failed'}, 400)

    # Prepare contact_us model
    review = CustomerReviewModel()
    review.firstName = firstName
    review.lastName = lastName
    review.email = email
    review.serviceName = serviceName
    review.comment = comment
    review.overallRating = overallRating
    review.refer = refer
    review.expectation = expectation
    review.subscribe = subscribe
    review.captchaToken = captchaToken

    # Push data in dynamodb contact_us partition
    dynamodb = DynamodbClient()
    dynamodb.customer_review.put(review)
    
    return ({'message': 'Success'}, 200)