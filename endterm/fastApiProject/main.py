from datetime import timedelta

from starlette import status

import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


import models
import schemas
from crud import user_crud, country_crud, city_crud, airport_crud
from crud.user_crud import ALGORITHM, SECRET_KEY
from dto import Token
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
class TokenVerifier:
    def __init__(self):
        pass

    def verify_token(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except jwt.JWTError:
            raise credentials_exception
        return username

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User registration endpoint
@app.post("/register", response_model=schemas.User)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


# Login endpoint
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=user_crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=user_crud.REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = user_crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token = user_crud.create_refresh_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    result = Token(access_token=access_token, refresh_token=refresh_token)
    return result


@app.get("/countries/", response_model=list[schemas.Country])
def read_countries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading countries")
    countries = country_crud.get_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading a country with id: {country_id}")
    country = country_crud.get_country(db, country_id=country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@app.post("/countries/", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is creating a country: {country}")
    return country_crud.create_country(db=db, country=country)

@app.put("/countries/{country_id}", response_model=schemas.Country)
def update_country(country_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is updating a country with id: {country_id}")
    return country_crud.update_country(db=db, country_id=country_id, country=country)

@app.delete("/countries/{country_id}", response_model=schemas.Country)
def delete_country(country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is deleting a country with id: {country_id}")
    return country_crud.delete_country(db=db, country_id=country_id)


# Create City endpoint
@app.get("/cities/", response_model=list[schemas.City])
def read_cities(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading cities")
    cities = city_crud.get_cities(db, skip=skip, limit=limit)
    return cities

@app.get("/cities/{city_id}", response_model=schemas.City)
def read_city(city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading a city with id: {city_id}")
    city = city_crud.get_city(db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@app.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is creating a city")
    return city_crud.create_city(db=db, city=city)

@app.put("/cities/{city_id}", response_model=schemas.City)
def update_city(city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is updating a city with id: {city_id}")
    return city_crud.update_city(db=db, city_id=city_id, city=city)

@app.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is deleting a city with id: {city_id}")
    return city_crud.delete_city(db=db, city_id=city_id)


# Create Airport endpoint
@app.get("/airports/", response_model=list[schemas.Airport])
def read_airports(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading airports")
    airports = airport_crud.get_airports(db, skip=skip, limit=limit)
    return airports

@app.get("/airports/{airport_id}", response_model=schemas.Airport)
def read_airport(airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is reading an airport with id: {airport_id}")
    airport = airport_crud.get_airport(db, airport_id=airport_id)
    if airport is None:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport

@app.post("/airports/", response_model=schemas.Airport)
def create_airport(airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is creating an airport")
    return airport_crud.create_airport(db=db, airport=airport)

@app.put("/airports/{airport_id}", response_model=schemas.Airport)
def update_airport(airport_id: int, airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is updating an airport with id: {airport_id}")
    return airport_crud.update_airport(db=db, airport_id=airport_id, airport=airport)

@app.delete("/airports/{airport_id}", response_model=schemas.Airport)
def delete_airport(airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    print(f"{username} is deleting an airport with id: {airport_id}")
    return airport_crud.delete_airport(db=db, airport_id=airport_id)