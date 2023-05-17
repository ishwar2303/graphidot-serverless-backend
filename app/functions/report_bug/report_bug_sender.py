from app.shared.common.recaptcha import CaptchaValidation
from app.shared.database.dynamodb_client import DynamodbClient
from app.shared.models import ReportBugModel

def main(payload: dict) -> dict:
    url = payload.get('url')
    details = payload.get('details')
    browser = payload.get('browser')
    operatingSystem = payload.get('operatingSystem')
    captchaToken = payload.get('captchaToken')

    if not url or not details or not browser or not operatingSystem or not captchaToken:
        return ({'message': 'Missing parameters'}, 400)

    # Captcha verification
    captcha = CaptchaValidation()
    if not captcha.validate(captchaToken):
        return ({'message': 'Captcha validation failed'}, 400)

    # Prepare feedback model
    bug = ReportBugModel()
    bug.url = url
    bug.details = details
    bug.browser = browser
    bug.operatingSystem = operatingSystem
    bug.captchaToken = captchaToken

    # Push data in dynamodb feedback partition
    dynamodb = DynamodbClient()
    dynamodb.report_bug.put(bug)
    
    return ({'message': 'Success'}, 200)