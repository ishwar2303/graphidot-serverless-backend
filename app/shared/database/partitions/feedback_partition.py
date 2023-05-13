import time

from app.shared.database.partitions.partition import Partition
from app.shared.models import FeedbackModel
from app.shared.enums import GraphiDotObjectType

class FeedbackPartition(Partition):

    def __init__(self, table, client) -> None:
        self.table = table
        self.client = client

    def put(self, feedback:FeedbackModel):
        """ Put Feedback Record """
        record = self._model_to_record(feedback)
        self.table.put_item(Item = record)
        return True
    
    def get(self, object_id:str) -> FeedbackModel:
        """ Get a single Feedback record """
        if not object_id:
            raise ValueError('No object id provided')
        
        response = self.table.get_item(
            key = {
                'object_type': GraphiDotObjectType.FEEDBACK.value,
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

    def _record_to_model(self, record: dict) -> FeedbackModel:
        if not record:
            return None
        
        feedback = FeedbackModel()
        feedback.id = record.get('object_id')
        feedback.rating = record.get('rating')
        feedback.comment = record.get('comment')
        feedback.captchaToken = record.get('captchaToken')

        return feedback
    
    def _model_to_record(self, model: object) -> dict:

        # Assert required parameters
        assert model.id, 'Missing object id'

        # Add required data
        record = {
            'object_type': GraphiDotObjectType.FEEDBACK.value,
            'object_id': model.id,
            'modified': int(time.time())
        }

        # Add optional data
        if model.rating:
            record.update({'rating': model.rating})
        if model.comment:
            record.update({'comment': model.comment})
        if model.captchaToken:
            record.update({'captchaToken': model.captchaToken})

        return record

        
