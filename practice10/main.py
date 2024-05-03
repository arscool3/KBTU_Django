from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/players/", response_model=schemas.Player)
def add_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@app.get("/players/", response_model=List[schemas.Player])
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Player).offset(skip).limit(limit).all()

@app.get("/players/{player_id}", response_model=schemas.Player)
def get_player_by_id(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.put("/players/{player_id}", response_model=schemas.Player)
def update_player(player_id: int, player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    for var, value in vars(player).items():
        setattr(db_player, var, value) if value else None
    db.commit()
    db.refresh(db_player)
    return db_player

@app.delete("/players/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    db.delete(db_player)
    db.commit()
    return {"message": "Player deleted"}


@app.post("/bots/", response_model=schemas.Bot)
def add_bot(bot: schemas.BotCreate, db: Session = Depends(get_db)):
    db_bot = models.Bot(**bot.dict())
    db.add(db_bot)
    db.commit()
    db.refresh(db_bot)
    return db_bot

@app.post("/weapons/", response_model=schemas.Weapon)
def add_weapon(weapon: schemas.WeaponCreate, owner_id: int, db: Session = Depends(get_db)):
    db_weapon = models.Weapon(**weapon.dict(), owner_id=owner_id)
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon

@app.get("/bots/", response_model=List[schemas.Bot])
def get_bots(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Bot).offset(skip).limit(limit).all()

@app.get("/bots/{bot_id}", response_model=schemas.Bot)
def get_bot_by_id(bot_id: int, db: Session = Depends(get_db)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    return db_bot

@app.put("/bots/{bot_id}", response_model=schemas.Bot)
def update_bot(bot_id: int, bot: schemas.BotCreate, db: Session = Depends(get_db)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    for var, value in vars(bot).items():
        setattr(db_bot, var, value) if value else None
    db.commit()
    db.refresh(db_bot)
    return db_bot

@app.delete("/bots/{bot_id}")
def delete_bot(bot_id: int, db: Session = Depends(get_db)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    db.delete(db_bot)
    db.commit()
    return {"message": "Bot deleted"}

@app.get("/weapons/", response_model=List[schemas.Weapon])
def get_weapons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Weapon).offset(skip).limit(limit).all()

@app.get("/weapons/{weapon_id}", response_model=schemas.Weapon)
def get_weapon_by_id(weapon_id: int, db: Session = Depends(get_db)):
    db_weapon = db.query(models.Weapon).filter(models.Weapon.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return db_weapon

@app.put("/weapons/{weapon_id}", response_model=schemas.Weapon)
def update_weapon(weapon_id: int, weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    db_weapon = db.query(models.Weapon).filter(models.Weapon.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    for var, value in vars(weapon).items():
        setattr(db_weapon, var, value) if value else None
    db.commit()
    db.refresh(db_weapon)
    return db_weapon

@app.delete("/weapons/{weapon_id}")
def delete_weapon(weapon_id: int, db: Session = Depends(get_db)):
    db_weapon = db.query(models.Weapon).filter(models.Weapon.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db.delete(db_weapon)
    db.commit()
    return {"message": "Weapon deleted"}

# потом как нибудь сокращу