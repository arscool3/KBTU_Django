from boto3 import Session
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime

from models import Base, Player, Team, Match

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI setup
app = FastAPI()


# Pydantic models
class PlayerBase(BaseModel):
    name: str


class PlayerCreate(PlayerBase):
    pass


class PlayerInDB(PlayerBase):
    id: int

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str


class TeamCreate(TeamBase):
    pass


class TeamInDB(TeamBase):
    id: int

    class Config:
        orm_mode = True


class MatchBase(BaseModel):
    team_id: int
    player_id: int
    date: datetime


class MatchCreate(MatchBase):
    pass


class MatchInDB(MatchBase):
    id: int

    class Config:
        orm_mode = True


# Routes
@app.post("/players/", response_model=PlayerInDB)
def create_player(player: PlayerCreate, db: Session = Depends(SessionLocal)):
    db_player = Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


@app.get("/players/{player_id}", response_model=PlayerInDB)
def get_player(player_id: int, db: Session = Depends(SessionLocal)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.post("/teams/", response_model=TeamInDB)
def create_team(team: TeamCreate, db: Session = Depends(SessionLocal)):
    print(team)
    db_team = Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


@app.get("/teams/{team_id}", response_model=TeamInDB)
def get_team(team_id: int, db: Session = Depends(SessionLocal)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@app.post("/matches/", response_model=MatchInDB)
def create_match(match: MatchCreate, db: Session = Depends(SessionLocal)):
    db_match = Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match
