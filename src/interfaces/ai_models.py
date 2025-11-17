from abc import ABC, abstractmethod

class BaseHFModel(ABC):

    @abstractmethod
    def get_tokenizer(self):
        pass

    @abstractmethod
    def create_pipeline(self):
        pass