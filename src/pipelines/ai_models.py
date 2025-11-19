
# Utils
from ..utils.loggers import GlobalTranslatorLogger

# Schemas
from ..schemas.outputs.model_outputs import SimilarTopicAudioFiles
from ..schemas.inputs.file_data import AudioFile, AudioFiles
from ..schemas.outputs.model_outputs import GenreList, GenreLists

# Pipelines
from .genre_classification import GenreClassification

class AiPipeline:

    def __init__(self, pipe_config):
        self.pipe_config = pipe_config
        self.logger = GlobalTranslatorLogger(pipe_name="AiPipeline")
        self.correctness = 0
        self.total = 0
    

    def run_pipeline(self, audio_files_list: AudioFiles, folder_path: str, user_defined_file: str) -> SimilarTopicAudioFiles:
        audio_genre_list = []
        for audio_file in audio_files_list:
            genre_classification = GenreClassification(audio_file, self.pipe_config, folder_path, user_defined_file)
            ai_genre = genre_classification.run_pipeline()
            audio_genre_list.append(ai_genre)
            self.monitor_curr_correctness(ai_genre, audio_file)
        
        struct_genre_audio_files = GenreLists(root=audio_genre_list)
        

    # Create analytics.py
    def monitor_curr_correctness(self, genres: GenreList, data: AudioFile) -> None:
            self.total += 1
            dominant_genre_confidence = genres[0]
            dominant_genre = dominant_genre_confidence.Label
            real_genre = data.Genre
            if dominant_genre == real_genre:
                self.correctness += 1
            self.logger.log_info("GenreClassificationCorrectness", f"The current correctness: {self.correctness/self.total}")




    

    




