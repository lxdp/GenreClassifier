import os

from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Schemas
from ..schemas.outputs.model_outputs import GenreLists
from ..schemas.inputs.file_data import PlayListSong, PlayListSongs

app = FastAPI()

origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Allowed frontend origins
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # Allow all headers
)

@app.get("/")
def get_playlist():
    playlist = []
    music_folder_path = "music_files_dataset/genres_original"
    genres = os.listdir(music_folder_path)
    for genre in genres:
        if genre.isalpha():
            genre_file_path = os.path.join(music_folder_path, genre)
            for audio_file_name in os.listdir(genre_file_path):
                if audio_file_name != "jazz.00054.wav":
                    song = PlayListSong(AudioName=audio_file_name.rsplit(".", 1)[0], Genre=genre, AudioFile=audio_file_name)
                    playlist.append(song)
    
    return PlayListSongs(root=playlist).model_dump()
    






