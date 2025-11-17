from pydantic import BaseModel, RootModel

from typing import List

class AiGenre(BaseModel):
    genre: str
    confidence: float

class AiGenreList(RootModel):
    root: List[AiGenre]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]