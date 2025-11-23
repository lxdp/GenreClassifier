import sys

# Utils
from src.app.utils.loggers import GlobalTranslatorLogger

from src.app.pipelines.service import GlobalWorkflow

if __name__=="__main__":
    global_workflow = GlobalWorkflow()
    global_workflow.run_workflow()