import time
from abc import ABC, abstractmethod

class Partition(ABC):

    @abstractmethod
    def put(self, **kwargs):
        pass

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass

    # Private methods

    @abstractmethod
    def _record_to_model(self, record:dict):
        pass

    @abstractmethod
    def _model_to_record(self, model:object):
        pass

    def _current_time(self) -> int:
        return int(time.time())
    
    def _chunks(self, list, n):
        """
        Yield successive n-sized chunks from list
        """

        for i in range(0, len(list), n):
            yield list[i:i+n]

    
