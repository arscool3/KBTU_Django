from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define models
class Anime(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

class Character(BaseModel):
    id: int
    name: str
    anime_id: int

class Rating(BaseModel):
    id: int
    anime_id: int
    character_id: int
    score: int

# Example data
anime_db = [
    Anime(id=1, title="Naruto", description="A ninja adventure anime."),
    Anime(id=2, title="Attack on Titan", description="A story of humanity's fight for survival against giant humanoid creatures."),
]

characters_db = [
    Character(id=1, name="Naruto Uzumaki", anime_id=1),
    Character(id=2, name="Sasuke Uchiha", anime_id=1),
    Character(id=3, name="Eren Yeager", anime_id=2),
    Character(id=4, name="Mikasa Ackerman", anime_id=2),
]

ratings_db = []

# GET endpoints
@app.get("/anime/", response_model=List[Anime])
async def get_anime():
    return anime_db

@app.get("/characters/", response_model=List[Character])
async def get_characters():
    return characters_db

@app.get("/ratings/", response_model=List[Rating])
async def get_ratings():
    return ratings_db

# POST endpoints
@app.post("/anime/", response_model=Anime)
async def create_anime(anime: Anime):
    anime_db.append(anime)
    return anime

@app.post("/characters/", response_model=Character)
async def create_character(character: Character):
    anime_exists = any(anime.id == character.anime_id for anime in anime_db)
    if not anime_exists:
        raise HTTPException(status_code=404, detail="Anime not found")
    characters_db.append(character)
    return character

@app.post("/ratings/", response_model=Rating)
async def create_rating(rating: Rating):
    anime_exists = any(anime.id == rating.anime_id for anime in anime_db)
    character_exists = any(character.id == rating.character_id for character in characters_db)
    if not anime_exists or not character_exists:
        raise HTTPException(status_code=404, detail="Anime or Character not found")
    ratings_db.append(rating)
    return rating
