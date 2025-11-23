import os
import time
import torch

from dotenv import load_dotenv
load_dotenv()

# Utils
from ..utils.loggers import GlobalTranslatorLogger
from ..utils import env_configuration

# Schemas
from ..schemas.inputs.model_pipelines import BaseEntities, GlobalPipeline

# Models
from .model_variants import ZeroShotClassificationTopicModel, MockZeroShotClassificationTopicModel, MusicGenreClassificationModel, MockMusicGenreClassificationModel

class ModelInitializer:

    def __init__(
            self,
            access_token = os.getenv("HF_ACCESS_TOKEN"),
            mode="production"
    ):
        self.access_token=access_token
        self.mode = mode
        self.logger = GlobalTranslatorLogger(pipe_name="AiPipeline")

        if self.mode == "local" or self.mode == "development":
            self.topics_model_name = os.getenv("HF_TOPICS_MODEL")
            self.music_genre_classification_model_name = os.getenv("HF_GENRE_CLASS_MODEL")
            self.device = 'cpu'
        else:
            self.topics_model_name = "models/topics"
            self.music_genre_classification_model_name = "models/genre_classification"
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    
    def init_topic_model_pipeline(self) -> BaseEntities:

        if not env_configuration.MOCK_MODELS:
            init_topic_model = ZeroShotClassificationTopicModel(
                model_name=self.topics_model_name, access_token=self.access_token
            )
        else:
            init_topic_model = MockZeroShotClassificationTopicModel(
                model_name=self.topics_model_name, access_token=self.access_token
            )
        topic_entity = BaseEntities(tokenizer=init_topic_model.get_tokenizer(), pipeline=init_topic_model.create_pipeline())
        return topic_entity

    def init_genre_classifier_model_pipeline(self) -> BaseEntities:
        
        if not env_configuration.MOCK_MODELS:
            init_genre_model = MusicGenreClassificationModel(
                model_name=self.music_genre_classification_model_name, access_token=self.access_token
            )
        else:
            init_genre_model = MockMusicGenreClassificationModel(
                model_name=self.music_genre_classification_model_name, access_token=self.access_token
            )
        genre_classification_entity = BaseEntities(tokenizer=init_genre_model.get_tokenizer(), pipeline=init_genre_model.create_pipeline())
        return genre_classification_entity

    
    def init_ai_model_pipelines(self) -> GlobalPipeline:

        # start_time_topics = time.time()
        # topic_entities = self.init_topic_model_pipeline()
        # load_time_topics = time.time() - start_time_topics
        # self.logger.log_info("TopicsModelDownloadingTime", f"Time to load the Topic model: {load_time_topics:.2f} seconds.")
        
        start_time_genre_classification = time.time()
        genre_classification_entities = self.init_genre_classifier_model_pipeline()
        load_time_genre_classification = time.time() - start_time_genre_classification
        self.logger.log_info("GenreClassificationDownloadingTime", f"Time to load the Music Genre Classification model: {load_time_genre_classification:.2f} seconds.")

        return GlobalPipeline(genre_classification_entities=genre_classification_entities)
        