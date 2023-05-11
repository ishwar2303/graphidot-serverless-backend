def main(payload: dict) -> dict:
    rating = payload.get('rating')
    message = payload.get('message')

    if not rating and not message:
        return ({'message': 'Missing parameters'}, 400)
    
    # Push data in dynamodb feedback partition

    return ({'message': 'Success'}, 200)