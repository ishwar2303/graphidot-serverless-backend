import json
import sys
import traceback
from app.functions.feedback import feedback_sender
from app.functions.contact_us import contact_us_sender
from app.functions.report_bug import report_bug_sender
from app.functions.customer_review import customer_review_sender

def _extract_payload(event: dict) -> object:
    """ Extract payload from request, looks for body first, else in query parameter """

    json_string: str = None
    if event.get('body'):
        json_string = event['body']
        return json.loads(json_string)
    elif event.get('queryStringParameters'):
        return event['queryStringParameters']
    elif event:
        return event
    else:
        return None
    
def _handle_error(context: any) -> None:
    """ 
    Generic error handling function
    Use this to post error message to a channel where developers can see and take action
    """

    exception_type, exception_value, exception_traceback = sys.exc_info()
    traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)

    
def _http_response(body, status: int = 200) -> dict:

    """
    Wraps data into format suitable for http
    """

    return {
        'statusCode': status,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(body, default=lambda x: x.__dict__)
    }
    
def feedback_handler(event, context):
    try:
        payload = _extract_payload(event)
        print(payload)
        response, status = feedback_sender.main(payload)
        return _http_response(response, status)
    except Exception:
        traceback.print_exc()
        _handle_error(context)
        return _http_response({'message': 'Internal Error'}, 500)
        
def contact_us_handler(event, context):
    try:
        payload = _extract_payload(event)
        print(payload)
        response, status = contact_us_sender.main(payload)
        return _http_response(response, status)
    except Exception:
        traceback.print_exc()
        _handle_error(context)
        return _http_response({'message': 'Internal Error'}, 500)
        
def report_bug_handler(event, context):
    try:
        payload = _extract_payload(event)
        print(payload)
        response, status = report_bug_sender.main(payload)
        return _http_response(response, status)
    except Exception:
        traceback.print_exc()
        _handle_error(context)
        return _http_response({'message': 'Internal Error'}, 500)
        
def customer_review_handler(event, context):
    try:
        payload = _extract_payload(event)
        print(payload)
        response, status = customer_review_sender.main(payload)
        return _http_response(response, status)
    except Exception:
        traceback.print_exc()
        _handle_error(context)
        return _http_response({'message': 'Internal Error'}, 500)