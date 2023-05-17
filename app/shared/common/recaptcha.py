import os
import requests
import logging
import json

class CaptchaValidation:
    def __init__(self) -> None:
        self.google_captcha_verification_url = os.environ.get('GOOGLE_CAPTCHA_VERIFICATION_URL')
        self.recaptcha_key = '6LdUjB4iAAAAAF7eF795YJNyeciuveggQQ2pcXaz'

    def validate(self, captchaToken:str) -> bool:
        complete_url = f'{self.google_captcha_verification_url}?secret={self.recaptcha_key}&response={captchaToken}'
        print(complete_url)
        response = requests.post(complete_url, None)
        if response.status_code == 200:
            json_response = response.json()

            validation_status = 'Captcha Validation Passed' if json_response['success'] == True else 'Captcha Validation Failed'
            print(validation_status)
            # returns True or False based on captcha validation
            return json_response['success']
        else:
            logging.error('Recaptcha Validation Failed')
            return False
