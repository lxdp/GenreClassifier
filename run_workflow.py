import sys

# Utils
from src.utils.loggers import GlobalTranslatorLogger

from src.pipelines.service import GlobalWorkflow

if __name__=="__main__":
    
    # Provide genre and audio file from that genre as arguments when running 'python run_workflow.py'
    try:
        genre = sys.argv[1]
        audio_file = sys.argv[2]
        global_workflow = GlobalWorkflow(genre, audio_file)
        global_workflow.run_workflow()
    except IndexError as error:
        GlobalTranslatorLogger.log_exception("CommandLineArgumentReadingFailure", "The necessary values in the command line were not provided")