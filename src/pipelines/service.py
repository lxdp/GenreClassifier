import os


# Utils
from ..utils.loggers import GlobalTranslatorLogger
from ..utils.configuration import BasePipelineConfiguration

# Errors
from ..errors.workflow_errors import WorkflowValidator, BackendValidator

# Pipelines
from .ai_models import AiPipeline

# Schemas
from ..schemas.inputs.file_data import AudioFiles, AudioFile

class GlobalWorkflow:

    def __init__(self, genre, audio_file: str):

        self.genre = genre
        self.audio_file = audio_file
        self.user_defined_path = os.path.join(self.genre, self.audio_file)

        self.pipe_config = BasePipelineConfiguration()
        self.logger = GlobalTranslatorLogger(pipe_name="ServicePipeline")

        self.workflow_validator = WorkflowValidator()
        self.backend_validatior = BackendValidator()
        self.ai_pipeline = AiPipeline(self.pipe_config)
        
        self.folder_path = "music_files_dataset/genres_original"
        os.makedirs(self.folder_path, exist_ok=True)


    def run_workflow(self) -> None:

        user_defined_file = self.backend_validatior.user_audio_file_validation(self.folder_path, self.user_defined_path)
        if not user_defined_file:
            self.logger.log_info("UserFileFailure", "You must define a valid audio file path.")
            return
        
        struct_user_defined_file = self.workflow_validator.struct_file_validation(self.user_defined_path)
        if not struct_user_defined_file:
            self.logger.log_info("LoadAudioFileFailure", "Unsuccessfully extracted file information.")
            return


        audio_files_list = self.extract_files_with_genres()
        valid_audio_files_list = self.workflow_validator.audio_files_validation(audio_files_list)
        if not valid_audio_files_list:
            self.logger.log_info("AudioFileFailure", "Audio files failed to meet the specified schema.")
            return
        
        matched_genre_data = self.workflow_validator.ai_pipeline_validation(audio_files_list, self.ai_pipeline, self.folder_path, struct_user_defined_file)
        if not matched_genre_data:
            self.logger.log_info("GenreSearchFailure", "Failed to retrieve songs of the same genre as user audio file")

    def extract_files_with_genres(self) -> AudioFiles:
        audio_files = []
        genre_list = os.listdir(self.folder_path)

        for genre in genre_list:
            if genre[0].isalpha():
                genre_file_list = os.listdir(os.path.join(self.folder_path, genre))
                for file_name in genre_file_list:
                    audio_files.append(AudioFile(AudioName=file_name, Genre=genre))
        return AudioFiles(root=audio_files)
