import os

from typing import Any, Dict, Union
from dotenv import load_dotenv
load_dotenv()

# Models
from ..models.initialize import ModelInitializer


class ConfigLocator:

    _services: Dict[str, Any] = {}

    @classmethod
    def add_entity(cls, name: str, entity: Any) -> None:
        cls._services[name] = entity
    
    @classmethod
    def get_entity(cls, name: str) -> Union[Any, None]:
        return cls._services.get(name)

ConfigLocator.add_entity("ai_model_pipelines", ModelInitializer(mode=os.getenv("MODE")).init_ai_model_pipelines())


class BasePipelineConfiguration:

    def __init__(self):
        self.ai_model_pipelines = ConfigLocator.get_entity("ai_model_pipelines")