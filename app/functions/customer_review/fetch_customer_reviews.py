from app.shared.database.dynamodb_client import DynamodbClient

def main(payload: dict) -> dict:
    limit = payload.get('limit')
    lastEvaluatedKey = payload.get('lastEvaluatedKey')

    if not limit:
        limit = 2

    # Push data in dynamodb contact_us partition
    dynamodb = DynamodbClient()
    response =  dynamodb.customer_review.get_reviews_pagination(limit=limit, lastEvaluatedKey=lastEvaluatedKey)

    if response:
        items = response['Items']
        count = 0

        """
        {'object_type': 'CUSTOMER_REVIEW', 'object_id': Decimal('1684600419')}
        """
        if 'LastEvaluatedKey' in response:
            lastEvaluatedKey = response['LastEvaluatedKey']
        else:
            lastEvaluatedKey = None
            
        data = []
        for item in items:
            count += 1
            customer_review = dynamodb.customer_review._record_to_model(item)
            # temp = {
            #     'firstName': customer_review.firstName,
            #     'lastName': customer_review.lastName,
            #     'email': customer_review.email,
            #     'comment': customer_review.comment,
            #     'overallRating': int(customer_review.overallRating),
            #     'expectation': customer_review.expectation,
            #     'refer': customer_review.refer,
            #     'subscribe': customer_review.subscribe
            # }
            data.append(customer_review)

        if lastEvaluatedKey:
            return ({
                'data': data,
                'lastEvaluatedKey': {
                    'object_type': 'CUSTOMER_REVIEW',
                    'object_id': int(lastEvaluatedKey['object_id'])
                },
                'message': 'More reviews to load'
            }, 200)
        
        return({
            'data': data,
            'message': 'No more reviews'
        }, 200)
    
    return ({'message': 'Something went wrong while fetching records'}, 400)