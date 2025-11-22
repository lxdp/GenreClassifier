
# Utils
from ..utils.loggers import GlobalTranslatorLogger
from ..utils.configuration import BasePipelineConfiguration

# Schemas
from ..schemas.outputs.model_outputs import SimilarTopicAudioFiles
from ..schemas.inputs.file_data import AudioFile, AudioFiles
from ..schemas.outputs.model_outputs import GenreList, GenreLists

# Pipelines
from .genre_classification import GenreClassification
from .genre_searcher import GenreSearcher

class AiPipeline:

    def __init__(self, pipe_config: BasePipelineConfiguration):
        self.pipe_config = pipe_config
        self.logger = GlobalTranslatorLogger(pipe_name="AiPipeline")
        self.correctness = 0
        self.total = 0
    

    def run_pipeline(self, audio_files_list: AudioFiles, folder_path: str, user_defined_file: AudioFile) -> GenreLists:
        audio_genre_list = []
        for audio_file in audio_files_list:
            genre_classification = GenreClassification(audio_file, self.pipe_config, folder_path)
            ai_genre = genre_classification.run_pipeline()
            if not ai_genre:
                 continue
            audio_genre_list.append(ai_genre)
            self.monitor_curr_correctness(ai_genre, audio_file)
        
        struct_genre_audio_files = GenreLists(root=audio_genre_list)
        genre_searcher = GenreSearcher(self.pipe_config, struct_genre_audio_files, user_defined_file)
        matched_files = genre_searcher.run_pipeline()

        return matched_files
        

    # Create analytics.py
    def monitor_curr_correctness(self, genres: GenreList, data: AudioFile) -> None:
            self.total += 1
            dominant_genre_confidence = genres[0]
            dominant_genre = dominant_genre_confidence.Label
            real_genre = data.Genre
            if dominant_genre == real_genre:
                self.correctness += 1
            self.logger.log_info("GenreClassificationCorrectness", f"The current correctness: {self.correctness/self.total}")




    

    




