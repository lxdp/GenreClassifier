import os

from typing import Optional
from pathlib import Path

# Utils
from ..utils.loggers import GlobalTranslatorLogger

# Schemas
from ..schemas.inputs.file_data import AudioFiles, AudioFile
from ..schemas.outputs.model_outputs import SimilarTopicAudioFiles

# Pipelines
from ..pipelines.ai_models import AiPipeline

class WorkflowValidator:

    def __init__(self):
        self.logger = GlobalTranslatorLogger(pipe_name="WorkFlowValidator")
    
    def audio_files_validation(self, file_list: AudioFiles) -> Optional[AudioFiles]:
        try:
            AudioFiles.model_validate(file_list)
            return file_list
        except Exception as error:
            self.logger.log_exception("AudioFileListValidationFailure", f"The following error occured during validation: {error}.")
            return
    
    def ai_pipeline_validation(self, audio_files_list: AudioFiles, ai_pipeline: AiPipeline, folder_path: str, user_defined_file: str) -> Optional[SimilarTopicAudioFiles]:
        try:
            matched_audios = ai_pipeline.run_pipeline(audio_files_list, folder_path, user_defined_file)
            return matched_audios
        except Exception as error:
            self.logger.log_exception("AiPipelineValidationFailure", f"The following error occured during validation: {error}.")
            return

class BackendValidator:

    def __init__(self):
        self.logger = GlobalTranslatorLogger(pipe_name="BackendValidator")

    def user_audio_file_validation(self, folder_path: str, user_defined_path: str) -> Optional[str]:
        full_file_path = os.path.join(folder_path, user_defined_path)
        if os.path.isfile(full_file_path):
            return full_file_path
        else:
            self.logger.log_info("UserDefinedFilePathValidationFailure", "The file path does not exist.")
            return




