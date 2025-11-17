from typing import Optional

import transformers
from transformers.models.bart.tokenization_bart_fast import BartTokenizerFast
from transformers.pipelines.zero_shot_classification import ZeroShotClassificationPipeline

# Interfaces
from ..interfaces.ai_models import BaseHFModel

# Utils
from ..utils import env_configuration

class ZeroShotClassificationTopicModel(BaseHFModel):

    def __init__(self, model_name: str = "models/topics", access_token: str = ""):
        self.model_name = model_name,
        self.access_token = access_token
    
    def get_tokenizer(self) -> BartTokenizerFast:
        return BartTokenizerFast.from_pretrained(pretrained_model_name_or_path=self.model_name, token=self.access_token)

    def create_pipeline(self) -> ZeroShotClassificationPipeline:
        
        pipeline = transformers.pipeline(
            task="zero-shot-classification",
            model=self.model_name,
            device=env_configuration.DEVICE,
            token=self.access_token
        )
        return pipeline
    
class MockZeroShotClassificationTopicModel(BaseHFModel):

    def __init__(self, model_name: str="models/topics", access_token: str = ""):
        self.model_name = model_name
        self.access_token = access_token
    
    def get_tokenizer(self) -> BartTokenizerFast:
        return BartTokenizerFast.from_pretrained(pretrained_model_name_or_path=self.model_name, token=self.access_token)

    def create_pipeline(self) -> Optional[ZeroShotClassificationPipeline]:
        return None

class MusicGenreClassificationModel(BaseHFModel):

    def __init__(self, model_name: str="models/genre_classification", access_token: str = ""):
        self.model_name = model_name
        self.access_token = access_token
    
    def get_tokenizer(self):
        return
    
    def create_pipeline(self):
        pipeline = transformers.pipeline(
            task="audio-classification",
            model=self.model_name,
            device=env_configuration.DEVICE,
            token=self.access_token
        )
        return pipeline

class MockMusicGenreClassificationModel():

    def __init__(self, model_name: str="models/genre_classification", access_token: str = ""):
        self.model_name = model_name
        self.access_token = access_token
    
    def get_tokenizer(self):
        return
    
    def create_pipeline(self):
        return
    

