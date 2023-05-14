from app.shared.database.dynamodb_client import DynamodbClient
from app.shared.models import ContactUsModel

def main(payload: dict) -> dict:
    firstName = payload.get('firstName')
    lastName = payload.get('lastName')
    email = payload.get('email')
    contact = payload.get('contact')
    customerMessage1 = payload.get('customerMessage1')
    captchaToken = payload.get('captchaToken')

    if not firstName or not lastName or not email or not contact or not customerMessage1 or not captchaToken:
        return ({'message': 'Missing parameters'}, 400)

    # Prepare contact_us model
    contact_us = ContactUsModel()
    contact_us.firstName = firstName
    contact_us.lastName = lastName
    contact_us.email = email
    contact_us.contact = contact
    contact_us.customerMessage1 = customerMessage1
    contact_us.captchaToken = captchaToken

    # Push data in dynamodb contact_us partition
    dynamodb = DynamodbClient()
    dynamodb.contact_us.put(contact_us)
    
    return ({'message': 'Success'}, 200)