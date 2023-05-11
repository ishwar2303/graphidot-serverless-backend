import json
import sys
import traceback
from app.functions.feedback import feedback_sender


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
        # response = {'message': 'Success'}
        # status = 200
        response, status = feedback_sender.main(payload)
        return _http_response(response, status)
    except Exception:
        _handle_error(context)
        return _http_response({'message': 'Internal Error'}, 500)
        
