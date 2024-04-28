import datetime
import uuid
from datetime import timedelta
from starlette import status

import jwt
from jwt import PyJWTError
import os
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from celery.app import Celery

import models
import schemas
from crud import user_crud, country_crud, city_crud, airport_crud, plane_crud, flight_crud
from crud.user_crud import ALGORITHM, SECRET_KEY
from dto import Token
from database import SessionLocal, engine
from task import celery_app, log_to_file, reserve_ticket

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
celery_app = celery_app
country_log_filename = "country_log"
city_log_filename = "city_log"
airport_log_filename = "airport_log"
plane_log_filename = "plane_log"
flight_log_filename = "flight_log"
ticket_log_filename = "ticket_log"
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
        except PyJWTError:
            raise credentials_exception
        return username

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_time():
    return datetime.datetime.now()

def generate_log_id():
    return uuid.uuid4()

def create_log(filename: str, username: str, method, message: str):
    log_to_file.delay(f"{filename}", f"LOG_ID: {generate_log_id()} ---- "
                                                 f"TIME: {get_current_time()} ---- "
                                                 f"USER: {username} ---- "
                                                 f"OPERATION: {method} ---- "
                                                 f"MESSAGE: {message}")
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
def read_countries(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING ALL COUNTRIES"
    method = request.method
    create_log(country_log_filename, username, method, message)
    countries = country_crud.get_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(request: Request, country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING THE COUNTRY WITH ID: {country_id}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    country = country_crud.get_country(db, country_id=country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@app.post("/countries/", response_model=schemas.Country)
def create_country(request: Request, country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A COUNTRY: {country}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.create_country(db=db, country=country)

@app.put("/countries/{country_id}", response_model=schemas.Country)
def update_country(request: Request, country_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING THE COUNTRY WITH ID: {country_id}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.update_country(db=db, country_id=country_id, country=country)

@app.delete("/countries/{country_id}", response_model=schemas.Country)
def delete_country(request: Request, country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING THE COUNTRY WITH ID: {country_id}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.delete_country(db=db, country_id=country_id)


# Create City endpoint
@app.get("/cities/", response_model=list[schemas.City])
def read_cities(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING CITIES"
    create_log(city_log_filename, username, request.method, message)
    cities = city_crud.get_cities(db, skip=skip, limit=limit)
    return cities

@app.get("/cities/{city_id}", response_model=schemas.City)
def read_city(request: Request, city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A CITY WITH ID: {city_id}"
    create_log(city_log_filename, username, request.method, message)
    city = city_crud.get_city(db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="CITY NOT FOUND")
    return city

@app.post("/cities/", response_model=schemas.City)
def create_city(request: Request, city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A CITY"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.create_city(db=db, city=city)

@app.put("/cities/{city_id}", response_model=schemas.City)
def update_city(request: Request, city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A CITY WITH ID: {city_id}"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.update_city(db=db, city_id=city_id, city=city)

@app.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(request: Request, city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A CITY WITH ID: {city_id}"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.delete_city(db=db, city_id=city_id)


# Create Airport endpoint
@app.get("/airports/", response_model=list[schemas.Airport])
def read_airports(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AIRPORTS"
    create_log(airport_log_filename, username, request.method, message)
    airports = airport_crud.get_airports(db, skip=skip, limit=limit)
    return airports

@app.get("/airports/{airport_id}", response_model=schemas.Airport)
def read_airport(request: Request, airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AN AIRPORT WITH ID: {airport_id}"
    create_log(airport_log_filename, username, request.method, message)
    airport = airport_crud.get_airport(db, airport_id=airport_id)
    if airport is None:
        raise HTTPException(status_code=404, detail="AIRPORT NOT FOUND")
    return airport

@app.get("/airports/country/{country_id}", response_model=list[schemas.Airport])
def read_airports_by_country(request: Request, skip: int = 0, limit: int = 10, country_id: int = None, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AIRPORTS IN COUNTRY: {country_id}"
    create_log(airport_log_filename, username, request.method, message)
    airports = airport_crud.get_airports(db, skip, limit, country_id)
    if airports is None:
        raise HTTPException(status_code=404, detail="AIRPORTS NOT FOUND")
    return airports


@app.post("/airports/", response_model=schemas.Airport)
def create_airport(request: Request, airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING AN AIRPORT"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.create_airport(db=db, airport=airport)

@app.put("/airports/{airport_id}", response_model=schemas.Airport)
def update_airport(request: Request, airport_id: int, airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING AN AIRPORT WITH ID: {airport_id}"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.update_airport(db=db, airport_id=airport_id, airport=airport)

@app.delete("/airports/{airport_id}", response_model=schemas.Airport)
def delete_airport(request: Request, airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING AN AIRPORT WITH ID: {airport_id}"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.delete_airport(db=db, airport_id=airport_id)


@app.get("/planes/{plane_id}", response_model=schemas.Plane)
def read_plane(request: Request, plane_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A PLANE WITH ID: {plane_id}"
    create_log(plane_log_filename, username, request.method, message)
    plane = plane_crud.get_plane(db, plane_id)
    if plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    return plane

# Endpoint to get a list of planes
@app.get("/planes/", response_model=list[schemas.Plane])
def read_planes(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING PLANES"
    create_log(plane_log_filename, username, request.method, message)
    planes = plane_crud.get_planes(db, skip=skip, limit=limit)
    return planes

# Endpoint to create a new plane
@app.post("/planes/", response_model=schemas.Plane)
def create_plane(request: Request, plane: schemas.PlaneCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A PLANE"
    create_log(plane_log_filename, username, request.method, message)
    return plane_crud.create_plane(db=db, plane=plane)

# Endpoint to update an existing plane
@app.put("/planes/{plane_id}", response_model=schemas.Plane)
def update_plane(request: Request, plane_id: int, plane: schemas.PlaneUpdate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A PLANE WITH ID: {plane_id}"
    create_log(plane_log_filename, username, request.method, message)
    updated_plane = plane_crud.update_plane(db=db, plane_id=plane_id, plane=plane)
    if updated_plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    return updated_plane

# Endpoint to delete a plane
@app.delete("/planes/{plane_id}", response_model=schemas.Plane)
def delete_plane(request: Request, plane_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A PLANE WITH ID: {plane_id}"
    create_log(plane_log_filename, username, request.method, message)
    deleted_plane = plane_crud.delete_plane(db=db, plane_id=plane_id)
    if deleted_plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    return deleted_plane

@app.get("/flights/", response_model=list[schemas.Flight])
def read_flights(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING FLIGHTS"
    create_log(flight_log_filename, username, request.method, message)
    flights = flight_crud.get_flights(db, skip=skip, limit=limit)
    return flights

@app.get("/flights/{flight_id}", response_model=schemas.Flight)
def read_flight(request: Request, flight_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A FLIGHT WITH ID: {flight_id}"
    create_log(flight_log_filename, username, request.method, message)
    flight = flight_crud.get_flight(db, flight_id=flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    return flight

@app.post("/flights/", response_model=schemas.Flight)
def create_flight(request: Request, flight: schemas.FlightCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A FLIGHT"
    create_log(flight_log_filename, username, request.method, message)
    return flight_crud.create_flight(db=db, flight=flight)

@app.put("/flights/{flight_id}", response_model=schemas.Flight)
def update_flight(request: Request, flight_id: int, flight: schemas.FlightUpdate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A FLIGHT WITH ID: {flight_id}"
    create_log(flight_log_filename, username, request.method, message)
    updated_flight = flight_crud.update_flight(db=db, flight_id=flight_id, flight=flight)
    if updated_flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    return updated_flight

@app.delete("/flights/{flight_id}", response_model=schemas.Flight)
def delete_flight(request: Request, flight_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A FLIGHT WITH ID: {flight_id}"
    create_log(flight_log_filename, username, request.method, message)
    deleted_flight = flight_crud.delete_flight(db=db, flight_id=flight_id)
    if deleted_flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    return deleted_flight
