import time

from app.shared.database.partitions.partition import Partition
from app.shared.models import ReportBugModel
from app.shared.enums import GraphiDotObjectType

class ReportBugPartition(Partition):

    def __init__(self, table, client) -> None:
        self.table = table
        self.client = client

    def put(self, bug:ReportBugModel):
        """ Put Feedback Record """
        record = self._model_to_record(bug)
        self.table.put_item(Item = record)
        return True
    
    def get(self, object_id:str) -> ReportBugModel:
        """ Get a single Feedback record """
        if not object_id:
            raise ValueError('No object id provided')
        
        response = self.table.get_item(
            key = {
                'object_type': GraphiDotObjectType.REPORT_BUG.value,
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

    def _record_to_model(self, record: dict) -> ReportBugModel:
        if not record:
            return None
        
        bug = ReportBugModel()
        bug.id = record.get('object_id')
        bug.url = record.get('url')
        bug.details = record.get('details')
        bug.browser = record.get('browser')
        bug.operatingSystem = record.get('operatingSystem')
        bug.captchaToken = record.get('captchaToken')

        return bug
    
    def _model_to_record(self, model: object) -> dict:

        # Add required data
        record = {
            'object_type': GraphiDotObjectType.REPORT_BUG.value,
            'object_id': int(time.time()),
            'modified': int(time.time())
        }

        # Add optional data
        if model.url:
            record.update({'url': model.url})
        if model.details:
            record.update({'details': model.details})
        if model.browser:
            record.update({'browser': model.browser})
        if model.operatingSystem:
            record.update({'operatingSystem': model.operatingSystem})
        if model.captchaToken:
            record.update({'captchaToken': model.captchaToken})

        return record

        
