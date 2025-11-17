import os
import time

from typing import Tuple, Optional

# Utils
from ..utils.loggers import GlobalTranslatorLogger
from ..utils.configuration import BasePipelineConfiguration
from ..utils import env_configuration
from ..utils.constants.genre_classification import genre_classification_output

# Schemas
from ..schemas.inputs.file_data import AudioFile
from ..schemas.outputs.file_data import AiGenre
from ..schemas.outputs.model_outputs import GenreList, GenreConfidence

class GenreClassification:

    def __init__(self, audio_data: AudioFile, pipe_config: BasePipelineConfiguration, folder_path: str, user_defined_file: str):
        self.logger = GlobalTranslatorLogger(pipe_name="GenreClassificationPipeline")
        self.audio_data = audio_data
        self.pipe_config = pipe_config
        self.folder_path = folder_path
        self.user_defined_file = user_defined_file

        self.pipeline = self.pipe_config.ai_model_pipelines.genre_classification_entities.pipeline
    
    def run_pipeline(self) -> GenreList:

        genre_list = self.genre_classification(self.audio_data)
        valid_genre_list = self.validate_classification(genre_list.GenreList[0], self.audio_data)
        if valid_genre_list:
            matched_genre_list = self.get_similar_songs(valid_genre_list)
        else:
            matched_genre_list = self.get_similar_songs(genre_list)
        
        return matched_genre_list
    
    def genre_classification(self, data: AudioFile) -> GenreList:

        genre_list = []
        if not env_configuration.MOCK_MODELS:
            self.logger.log_info("RealGenreClassifier", "Using the transformers genre classifier pipeline.")
            file_name = data.AudioName
            genre_file_path = os.path.join(self.folder_path, data.Genre)
            start_time = time.time()
            genre_classification = self.pipeline(os.path.join(genre_file_path, file_name))
            inference_time = time.time() - start_time
            self.logger.log_info("GenreClassificationInferenceTime", f"The genre classifier took: {inference_time:.2f} seconds.")
        else:
            self.logger.log_info("MockGenreClassifier", "Using the mock genre classifier.")
            genre_classification = genre_classification_output

        for genre_confidence in genre_classification:
            schema_output = GenreConfidence(Score=genre_confidence['score'], Label=genre_confidence['label'])
            genre_list.append(schema_output)
        
        return GenreList(GenreList=genre_list)

    def validate_classification(self, dominant_genre: GenreConfidence, data: AudioFile) -> Optional[GenreList]:

        genre_list = []
        if dominant_genre.Score >= 0.85 or env_configuration.MOCK_MODELS:
            self.logger.log_info("ConfidenceThresholdMet", "Pipeline genre classification confidence is high enough.")
            return
        else:
            self.logger.log_info("GenreReclassification", "Re-classification occuring due to low confidence.")
            file_name = data.AudioName
            genre_file_path = os.path.join(self.folder_path, data.Genre)
            start_time = time.time()
            genre_classification = self.pipeline(os.path.join(genre_file_path, file_name))
            inference_time = time.time() - start_time
            self.logger.log_info("GenreReclassificationInferenceTime", f"The genre classifier took: {inference_time:.2f} seconds.")
        
        for genre_confidence in genre_classification:
            schema_output = GenreConfidence(Score=genre_confidence['score'], Label=genre_confidence['label'])
            genre_list.append(schema_output)
        
        return GenreList(GenreList=genre_list)
    
    def get_similar_songs(self, genre_list) -> GenreList:







    
