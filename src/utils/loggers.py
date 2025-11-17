import logging
import sys

def set_azure_services_logger() -> logging.Logger:
    azure_logger = logging.getLogger('azure')
    azure_logger.setLevel(logging.ERROR)

def set_global_ai_workflow_logger() -> logging.Logger:
    global_logger = logging.getLogger(__name__)
    global_logger.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    ch_stdout = logging.StreamHandler(stream=sys.stdout)
    ch_stdout.setLevel(logging.INFO)
    ch_stdout.setFormatter(formatter)

    ch_stderr = logging.StreamHandler(stream=sys.stderr)
    ch_stderr.setLevel(logging.ERROR)
    ch_stderr.setFormatter(formatter)

    global_logger.addHandler(ch_stdout)
    global_logger.addHandler(ch_stderr)

    return global_logger

logger = set_global_ai_workflow_logger()

class GlobalTranslatorLogger:

    def __init__(self, pipe_name):
        self.logger = logger
        self.pipe_name = pipe_name
    
    def _prepare_data(self, action, message, **kwargs):
        extra_data = {"feature": "GCService", "pipeline": self.pipe_name, "action": action, **kwargs}
        pattern_message = f"[{extra_data['feature']}] [{self.pipe_name}] [{action}] {message}"
        return extra_data, pattern_message
    
    def log_info(self, action, message, **kwargs):
        extra_data, pattern_message = self._prepare_data(action, message, **kwargs)
        self.logger.info(msg=pattern_message, extra=extra_data)
    
    def log_warning(self, action, message, **kwargs):
        extra_data, pattern_message = self._prepare_data(action, message, **kwargs)
        self.logger.warning(msg=pattern_message, extra=extra_data)
    
    def log_exception(self, action, message, **kwargs):
        extra_data, pattern_message = self._prepare_data(action, message, **kwargs)
        self.logger.exception(msg=pattern_message, extra=extra_data)