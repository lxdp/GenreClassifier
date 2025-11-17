from pydantic import BaseModel, RootModel
from typing import List


class AudioFile(BaseModel):
    AudioName: str
    Genre: str

class AudioFiles(RootModel):
    root: List[AudioFile]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]