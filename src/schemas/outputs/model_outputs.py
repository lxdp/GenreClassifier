from pydantic import BaseModel, RootModel
from typing import List

class Topics(BaseModel):
    topic_name: str
    confidence: float

class SimilarTopicAudioFile(BaseModel):
    file_name: str
    topics: List[Topics]

class SimilarTopicAudioFiles(RootModel):
    root: List[SimilarTopicAudioFile]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]

class GenreConfidence(BaseModel):
    Score: float
    Label: str

class GenreList(RootModel):
    root: List[GenreConfidence]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, item):
        return self.root[item]
