import time

from app.shared.database.partitions.partition import Partition
from app.shared.models import ContactUsModel
from app.shared.enums import GraphiDotObjectType

class ContactUsPartition(Partition):

    def __init__(self, table, client) -> None:
        self.table = table
        self.client = client

    def put(self, feedback:ContactUsModel):
        """ Put ContactUs Record """
        record = self._model_to_record(feedback)
        self.table.put_item(Item = record)
        return True
    
    def get(self, object_id:str) -> ContactUsModel:
        """ Get a single ContactUs record """
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

    def _record_to_model(self, record: dict) -> ContactUsModel:
        if not record:
            return None
        
        contact_us = ContactUsModel()
        contact_us.id = record.get('object_id')
        contact_us.firstName = record.get('firstName')
        contact_us.lastName = record.get('lastName')
        contact_us.email = record.get('email')
        contact_us.contact = record.get('contact')
        contact_us.customerMessage1 = record.get('customerMessage1')
        contact_us.captchaToken = record.get('captchaToken')

        return contact_us
    
    def _model_to_record(self, model: object) -> dict:

        # Add required data
        record = {
            'object_type': GraphiDotObjectType.CONTACT_US.value,
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
        if model.contact:
            record.update({'contact': model.contact})
        if model.customerMessage1:
            record.update({'customerMessage1': model.customerMessage1})
        if model.captchaToken:
            record.update({'captchaToken': model.captchaToken})

        return record

        
