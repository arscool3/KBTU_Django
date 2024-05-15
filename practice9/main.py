from fastapi import FastAPI, Depends

app = FastAPI()

# 1.аутентифицируем игрока
def authenticate_player(player_id: str):
    # Simulating authentication logic here
    if player_id == "player123":
        return {"player_id": player_id, "authenticated": True}
    else:
        return {"player_id": None, "authenticated": False}

@app.get("/players/{player_id}")
async def get_player_info(player_info: dict = Depends(authenticate_player)):
    if player_info["authenticated"]:
        return {"message": "Player authenticated", "player_info": player_info}
    else:
        return {"message": "Player not authenticated"}


# 2.менеджемент оружия
initial_weapon_inventory = ["AK-47"]

def get_weapon_inventory():
    return initial_weapon_inventory

@app.get("/weapons/")
def list_weapons(player_id: str, inventory = Depends(get_weapon_inventory)):
    return {"player_id": player_id, "weapons": inventory}

# 3.поведение бота
async def game_bot_behavior(player_id: str, current_weapon: str, bot_level: int):
    if current_weapon == "AK-47":
        damage = bot_level * 20
    elif current_weapon == "AWM":
        damage = bot_level * 30
    else:
        damage = bot_level * 10  # Default damage for other weapons
    return {"player_id": player_id, "bot_damage": damage}

@app.get("/bot/")
async def bot_simulation(player_id: str, weapon: str, bot_level: int = 1,
                         bot_info: dict = Depends(game_bot_behavior)):
    return bot_info
