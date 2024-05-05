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
from crud import user_crud, country_crud, city_crud, airport_crud, plane_crud, flight_crud, ticket_crud
from crud.user_crud import ALGORITHM, SECRET_KEY
from dto import Token
from database import SessionLocal, engine
from task import celery_app, log_to_file, reserve_ticket

models.Base.metadata.create_all(bind=engine)
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "country",
        "description": "Manage country. So _fancy_ they have their own docs.",
    },
    {
        "name": "city",
        "description": "Manage city. So _fancy_ they have their own docs.",
    },
    {
        "name": "plane",
        "description": "Manage plane. So _fancy_ they have their own docs.",
    },
    {
        "name": "flight",
        "description": "Manage flight. So _fancy_ they have their own docs.",
    },
    {
        "name": "ticket",
        "description": "Manage ticket. So _fancy_ they have their own docs.",
    },
]
app = FastAPI(openapi_tags=tags_metadata)
celery_app = celery_app
country_log_filename = "country_log"
city_log_filename = "city_log"
airport_log_filename = "airport_log"
plane_log_filename = "plane_log"
flight_log_filename = "flight_log"
ticket_log_filename = "ticket_log"
user_log_filename = "user_log"
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
@app.post("/register", response_model=schemas.User, tags=["users"])
def register(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    message = f"SOME USER TRYING TO REGISTER. REGISTRATION DATA: {str(user)}"
    create_log(user_log_filename, user.username, request.method, message)
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    message = f"{user.username} REGISTERED SUCCESSFULLY"
    create_log(user_log_filename, user.username, request.method, message)
    return user_crud.create_user(db=db, user=user)


# Login endpoint
@app.post("/token", response_model=Token, tags=["users"])
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    message = f"{user.username} IS TRYING TO LOG IN"
    print(user_crud.get_tickets(db=db, username=user.username))
    create_log(user_log_filename, user.username, request.method, message)
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
    message = f"{user.username} SUCCESSFULLY LOGGED IN"
    create_log(user_log_filename, user.username, request.method, message)
    return result


@app.get("/countries/", response_model=list[schemas.Country], tags=["country"])
def read_countries(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING ALL COUNTRIES"
    countries = country_crud.get_countries(db, skip=skip, limit=limit)
    create_log(country_log_filename, username, request.method, message)
    return countries

@app.get("/countries/{country_id}", response_model=schemas.Country, tags=["country"])
def read_country(request: Request, country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING THE COUNTRY WITH ID: {country_id}"
    country = country_crud.get_country(db, country_id=country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    create_log(country_log_filename, username, request.method, message)
    return country

@app.post("/countries/", response_model=schemas.Country, tags=["country"])
def create_country(request: Request, country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A COUNTRY: {country}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.create_country(db=db, country=country)

@app.put("/countries/{country_id}", response_model=schemas.Country, tags=["country"])
def update_country(request: Request, country_id: int, country: schemas.CountryCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING THE COUNTRY WITH ID: {country_crud.get_country(db, country_id).name} -> {str(country)}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.update_country(db=db, country_id=country_id, country=country)

@app.delete("/countries/{country_id}", response_model=schemas.Country, tags=["country"])
def delete_country(request: Request, country_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING THE COUNTRY WITH ID: {country_id}"
    method = request.method
    create_log(country_log_filename, username, method, message)
    return country_crud.delete_country(db=db, country_id=country_id)


# Create City endpoint
@app.get("/cities/", response_model=list[schemas.City], tags=["city"])
def read_cities(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING CITIES"
    cities = city_crud.get_cities(db, skip=skip, limit=limit)
    create_log(city_log_filename, username, request.method, message)
    return cities

@app.get("/cities/{city_id}", response_model=schemas.City, tags=["city"])
def read_city(request: Request, city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A CITY WITH ID: {city_id}"
    city = city_crud.get_city(db, city_id=city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="CITY NOT FOUND")
    create_log(city_log_filename, username, request.method, message)
    return city

@app.post("/cities/", response_model=schemas.City, tags=["city"])
def create_city(request: Request, city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A CITY: {str(city)}"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.create_city(db=db, city=city)

@app.put("/cities/{city_id}", response_model=schemas.City, tags=["city"])
def update_city(request: Request, city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A CITY WITH ID: {city_crud.get_city(db, city_id).name} -> {str(city)}"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.update_city(db=db, city_id=city_id, city=city)

@app.delete("/cities/{city_id}", response_model=schemas.City, tags=["city"])
def delete_city(request: Request, city_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A CITY WITH ID: {city_id}"
    create_log(city_log_filename, username, request.method, message)
    return city_crud.delete_city(db=db, city_id=city_id)


# Create Airport endpoint
@app.get("/airports/", response_model=list[schemas.Airport], tags=["airport"])
def read_airports(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AIRPORTS"
    airports = airport_crud.get_airports(db, skip=skip, limit=limit)
    create_log(airport_log_filename, username, request.method, message)
    return airports

@app.get("/airports/{airport_id}", response_model=schemas.Airport, tags=["airport"])
def read_airport(request: Request, airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AN AIRPORT WITH ID: {airport_id}"
    airport = airport_crud.get_airport(db, airport_id=airport_id)
    if airport is None:
        raise HTTPException(status_code=404, detail="AIRPORT NOT FOUND")
    create_log(airport_log_filename, username, request.method, message)
    return airport

@app.get("/airports/country/{country_id}", response_model=list[schemas.Airport], tags=["airport"])
def read_airports_by_country(request: Request, skip: int = 0, limit: int = 10, country_id: int = None, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING AIRPORTS IN COUNTRY: {country_id}"
    airports = airport_crud.get_airports(db, skip, limit, country_id)
    if airports is None:
        raise HTTPException(status_code=404, detail="AIRPORTS NOT FOUND")
    create_log(airport_log_filename, username, request.method, message)
    return airports


@app.post("/airports/", response_model=schemas.Airport, tags=["airport"])
def create_airport(request: Request, airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING AN AIRPORT: {str(airport)}"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.create_airport(db=db, airport=airport)

@app.put("/airports/{airport_id}", response_model=schemas.Airport, tags=["airport"])
def update_airport(request: Request, airport_id: int, airport: schemas.AirportCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING AN AIRPORT WITH ID: {airport_id} -> {str(airport)}"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.update_airport(db=db, airport_id=airport_id, airport=airport)

@app.delete("/airports/{airport_id}", response_model=schemas.Airport, tags=["airport"])
def delete_airport(request: Request, airport_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING AN AIRPORT WITH ID: {airport_id}"
    create_log(airport_log_filename, username, request.method, message)
    return airport_crud.delete_airport(db=db, airport_id=airport_id)


@app.get("/planes/{plane_id}", response_model=schemas.Plane, tags=["plane"])
def read_plane(request: Request, plane_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A PLANE WITH ID: {plane_id}"
    plane = plane_crud.get_plane(db, plane_id)
    if plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    create_log(plane_log_filename, username, request.method, message)
    return plane

# Endpoint to get a list of planes
@app.get("/planes/", response_model=list[schemas.Plane], tags=["plane"])
def read_planes(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING PLANES"
    planes = plane_crud.get_planes(db, skip=skip, limit=limit)
    create_log(plane_log_filename, username, request.method, message)
    return planes

# Endpoint to create a new plane
@app.post("/planes/", response_model=schemas.Plane, tags=["plane"])
def create_plane(request: Request, plane: schemas.PlaneCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A PLANE: {str(plane)}"
    create_log(plane_log_filename, username, request.method, message)
    return plane_crud.create_plane(db=db, plane=plane)

# Endpoint to update an existing plane
@app.put("/planes/{plane_id}", response_model=schemas.Plane, tags=["plane"])
def update_plane(request: Request, plane_id: int, plane: schemas.PlaneUpdate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A PLANE WITH ID: {plane_id} -> {str(plane)}"
    create_log(plane_log_filename, username, request.method, message)
    updated_plane = plane_crud.update_plane(db=db, plane_id=plane_id, plane=plane)
    if updated_plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    message = f"{username} UPDATED A PLANE WITH ID: {plane_id} -> {str(plane)}"
    create_log(plane_log_filename, username, request.method, message)
    return updated_plane

# Endpoint to delete a plane
@app.delete("/planes/{plane_id}", response_model=schemas.Plane, tags=["plane"])
def delete_plane(request: Request, plane_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A PLANE WITH ID: {plane_id}"
    create_log(plane_log_filename, username, request.method, message)
    deleted_plane = plane_crud.delete_plane(db=db, plane_id=plane_id)
    if deleted_plane is None:
        raise HTTPException(status_code=404, detail="PLANE NOT FOUND")
    message = f"{username} IS DELETED A PLANE WITH ID: {plane_id}"
    create_log(plane_log_filename, username, request.method, message)
    return deleted_plane

@app.get("/flights/", response_model=list[schemas.Flight], tags=["flight"])
def read_flights(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    flights = flight_crud.get_flights(db, skip=skip, limit=limit)
    if flights is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    message = f"{username} IS READING FLIGHTS"
    create_log(flight_log_filename, username, request.method, message)
    return flights

@app.get("/flights/{flight_id}", response_model=schemas.Flight, tags=["flight"])
def read_flight(request: Request, flight_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS READING A FLIGHT WITH ID: {flight_id}"
    flight = flight_crud.get_flight(db, flight_id=flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    create_log(flight_log_filename, username, request.method, message)
    return flight

@app.post("/flights/", response_model=schemas.Flight, tags=["flight"])
def create_flight(request: Request, flight: schemas.FlightCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A FLIGHT: {str(flight)}"
    create_log(flight_log_filename, username, request.method, message)
    return flight_crud.create_flight(db=db, flight=flight)

@app.put("/flights/{flight_id}", response_model=schemas.Flight, tags=["flight"])
def update_flight(request: Request, flight_id: int, flight: schemas.FlightUpdate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A FLIGHT WITH ID: {flight_id} -> {str(flight)}"
    create_log(flight_log_filename, username, request.method, message)
    updated_flight = flight_crud.update_flight(db=db, flight_id=flight_id, flight=flight)
    if updated_flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    message = f"{username} UPDATED A FLIGHT WITH ID: {flight_id} -> {str(flight)}"
    create_log(flight_log_filename, username, request.method, message)
    return updated_flight

@app.delete("/flights/{flight_id}", response_model=schemas.Flight, tags=["flight"])
def delete_flight(request: Request, flight_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A FLIGHT WITH ID: {flight_id}"
    create_log(flight_log_filename, username, request.method, message)
    deleted_flight = flight_crud.delete_flight(db=db, flight_id=flight_id)
    if deleted_flight is None:
        raise HTTPException(status_code=404, detail="FLIGHT NOT FOUND")
    message = f"{username} DELETED A FLIGHT WITH ID: {flight_id}"
    create_log(flight_log_filename, username, request.method, message)
    return deleted_flight

@app.get("/tickets/{ticket_id}", response_model=schemas.Ticket, tags=["ticket"])
def read_ticket(request: Request, ticket_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    db_ticket = ticket_crud.get_ticket(db=db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    message = f"{username} IS READING A TICKET WITH ID: {ticket_id}"
    create_log(ticket_log_filename, username, request.method, message)
    return db_ticket

# Get all tickets
@app.get("/tickets/", response_model=list[schemas.Ticket], tags=["ticket"])
def read_tickets(request: Request, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    tickets = ticket_crud.get_tickets(db=db, skip=skip, limit=limit)
    if tickets is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    message = f"{username} IS READING TICKETS"
    create_log(ticket_log_filename, username, request.method, message)
    return tickets

@app.post("/tickets/", response_model=schemas.Ticket, tags=["ticket"])
def create_ticket(request: Request, ticket: schemas.TicketCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS CREATING A TICKET: {str(ticket)}"
    create_log(ticket_log_filename, username, request.method, message)
    return ticket_crud.create_ticket(db=db, ticket=ticket)

# Update a ticket
@app.put("/tickets/{ticket_id}", response_model=schemas.Ticket, tags=["ticket"])
def update_ticket(request: Request, ticket_id: int, ticket: schemas.TicketCreate, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS UPDATING A TICKET: {ticket_id} -> {str(ticket)}"
    create_log(ticket_log_filename, username, request.method, message)
    updated_ticket = ticket_crud.update_ticket(db=db, ticket_id=ticket_id, ticket=ticket)
    if updated_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    message = f"{username} UPDATED A TICKET: {ticket_id} -> {str(ticket)}"
    create_log(ticket_log_filename, username, request.method, message)
    return updated_ticket

# Delete a ticket
@app.delete("/tickets/{ticket_id}", response_model=schemas.Ticket, tags=["ticket"])
def delete_ticket(request: Request, ticket_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS DELETING A TICKET: {ticket_id}"
    create_log(ticket_log_filename, username, request.method, message)
    deleted_ticket = ticket_crud.delete_ticket(db=db, ticket_id=ticket_id)
    if deleted_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    message = f"{username} DELETED A TICKET: {ticket_id}"
    create_log(ticket_log_filename, username, request.method, message)
    return deleted_ticket

@app.get("/tickets/available/", response_model=list[schemas.Ticket], tags=["ticket"])
def read_available_tickets(request: Request, plane_name: str = "", skip: int = 0, limit: int = 10, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    tickets = ticket_crud.get_tickets_available(db=db, skip=skip, limit=limit, plane_name=plane_name)
    if tickets is None:
        raise HTTPException(status_code=404, detail="Tickets not found")
    message = f"{username} IS READING AVAILABLE TICKETS"
    create_log(ticket_log_filename, username, request.method, message)
    return tickets

@app.post("/tickets/reserve", response_model=schemas.Ticket, tags=["ticket"])
def reserve_ticket(request: Request, ticket_id: int, db: Session = Depends(get_db), username: str = Depends(TokenVerifier.verify_token)):
    message = f"{username} IS RESERVING A FLIGHT"
    create_log(ticket_log_filename, username, request.method, message)
    ticket: schemas.Ticket = ticket_crud.reserve_ticket(db=db, ticket_id=ticket_id)

    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if ticket == "reserved":
        raise HTTPException(status_code=400, detail="Ticket is reserved")
    departure_airport_id = flight_crud.get_flight(db, ticket.flight_id).departure_airport_id
    destination_airport_id = flight_crud.get_flight(db, ticket.flight_id).destination_airport_id
    flight = f"FLIGHT ID: {ticket.flight_id} | DEPARTURE: {airport_crud.get_airport(db, departure_airport_id).name} | DESTINATION: {airport_crud.get_airport(db, destination_airport_id).name}"
    message = f"{username} RESERVED A FLIGHT: {flight}; PLANE: {ticket.plane_id}; SEAT_NUMBER: {ticket.seat_number}; TICKET: {ticket.id}"
    create_log(ticket_log_filename, username, request.method, message)
    reserve_ticket(ticket)
    return ticket