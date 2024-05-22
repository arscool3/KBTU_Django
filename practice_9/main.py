from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/")
def greet():
    return "Welcome to the Anime API!"

@app.get("/anime/{anime_id}")
def get_anime(anime_id: int, user_agent: str = Depends(get_user_agent)):
    

    anime_data = {
        1: {"title": "Naruto", "episodes": 220, "genre": "Shounen"},
        2: {"title": "One Piece", "episodes": 1000, "genre": "Shounen"},
        3: {"title": "Attack on Titan", "episodes": 75, "genre": "Shounen"}
    }
    return {"anime_id": anime_id, "anime_data": anime_data.get(anime_id, {"error": "Anime not found!"}), "user_agent": user_agent}

# Endpoint for user input about fav anime
@app.post("/favorite-anime")
def process_favorite_anime(anime_title: str, episodes_watched: int, user_agent: str = Depends(get_user_agent)):
    #  process the user input n store it
    return {"message": f"Your favorite anime is {anime_title} and you've watched {episodes_watched} episodes!", "user_agent": user_agent}

# Dependency to get user agent
def get_user_agent(user_agent: str = Depends()):
    return user_agent

# Dependency to get client IP address
def get_client_ip(ip: str = Depends()):
    return ip

# Dependency to authenticate the user
def authenticate_user(auth_token: str = Depends()):
    
    return "User authenticated"
