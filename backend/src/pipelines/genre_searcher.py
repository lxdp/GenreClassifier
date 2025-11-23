
# Utils
from ..utils.loggers import GlobalTranslatorLogger
from ..utils.configuration import BasePipelineConfiguration

# Schemas
from ..schemas.outputs.model_outputs import GenreLists
from ..schemas.inputs.file_data import AudioFile

class GenreSearcher:

    def __init__(self, pipe_config: BasePipelineConfiguration, genre_audio_files: GenreLists, user_file: AudioFile):
        self.pipe_config = pipe_config
        self.genre_audio_files = genre_audio_files
        self.user_file = user_file
        
        self.logger = GlobalTranslatorLogger(pipe_name="GenreSearcherPipeline")
    
    def run_pipeline(self) -> GenreLists:
        matched_genre_list = self.get_matched_genre_list()
        return matched_genre_list
    
    def get_matched_genre_list(self) -> GenreLists:
        search_genre = self.user_file.Genre
        print(search_genre)
        matched_genre_list = []
        for genre_list in self.genre_audio_files:
            dominant_genre = genre_list[0]
            if dominant_genre.Label == search_genre:
                matched_genre_list.append(genre_list)
        return GenreLists(root=matched_genre_list)
