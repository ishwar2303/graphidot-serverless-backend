import time

from app.shared.database.partitions.partition import Partition
from app.shared.models import CustomerReviewModel
from app.shared.enums import GraphiDotObjectType

class CustomerReviewPartition(Partition):

    def __init__(self, table, client) -> None:
        self.table = table
        self.client = client

    def put(self, customer_review:CustomerReviewModel):
        """ Put CustomerReview Record """
        record = self._model_to_record(customer_review)
        self.table.put_item(Item = record)
        return True
    
    def get(self, object_id:str) -> CustomerReviewModel:
        """ Get a single CustomerReview record """
        if not object_id:
            raise ValueError('No object id provided')
        
        response = self.table.get_item(
            key = {
                'object_type': GraphiDotObjectType.CONTACT_US.value,
                'object_id': object_id
            }
        )

        record = response.get('Item')
        return self._record_to_model(record)
    
    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass


    # Private methods

    def _record_to_model(self, record: dict) -> CustomerReviewModel:
        if not record:
            return None
        
        customer_review = CustomerReviewModel()
        customer_review.id = record.get('object_id')
        customer_review.firstName = record.get('firstName')
        customer_review.lastName = record.get('lastName')
        customer_review.email = record.get('email')
        customer_review.serviceName = record.get('serviceName')
        customer_review.comment = record.get('comment')
        customer_review.overallRating = record.get('overallRating')
        customer_review.refer = record.get('refer')
        customer_review.expectation = record.get('expectation')
        customer_review.subscribe = record.get('subscribe')
        customer_review.captchaToken = record.get('captchaToken')

        return customer_review
    
    def _model_to_record(self, model: object) -> dict:

        # Add required data
        record = {
            'object_type': GraphiDotObjectType.CUSTOMER_REVIEW.value,
            'object_id': int(time.time()),
            'modified': int(time.time())
        }

        # Add optional data
        if model.firstName:
            record.update({'firstName': model.firstName})
        if model.lastName:
            record.update({'lastName': model.lastName})
        if model.email:
            record.update({'email': model.email})
        if model.serviceName:
            record.update({'serviceName': model.serviceName})
        if model.comment:
            record.update({'comment': model.comment})
        if model.overallRating:
            record.update({'overallRating': model.overallRating})
        if model.refer:
            record.update({'refer': model.refer})
        if model.expectation:
            record.update({'expectation': model.expectation})
        if model.subscribe:
            record.update({'subscribe': model.subscribe})
        if model.captchaToken:
            record.update({'captchaToken': model.captchaToken})

        return record

        
