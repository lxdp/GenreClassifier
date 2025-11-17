from typing import Any

from pydantic import BaseModel, ConfigDict

class BaseEntities(BaseModel):

    model_config = ConfigDict(arbitrary_types_allowed=True)
    tokenizer: Any
    pipeline: Any

class GlobalPipeline(BaseModel):

    genre_classification_entities: BaseEntities