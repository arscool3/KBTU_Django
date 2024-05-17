from typing import List

import punq
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import select, insert
from fastapi import FastAPI, HTTPException
from kafka_utils import create_kafka_producer
import json
from task import async_process_payment
from sqlalchemy.orm import joinedload

import models as db
from sqlalchemy.orm.session import Session
from database import session
from schemas import (Hotel, CreateHotel, Room, CreateRoom,
                     Customer, CreateCustomer, Reservation,
                     CreateReservation, Review, CreateReview,
                     CreatePayment, Payment,
                     ReturnType)
from repository import AbcRepository, HotelRepository, RoomRepository, CustomerRepository, ReservationRepository, ReviewRepository, PaymentRepository


tags_metadata = [
    {"name": "Hotel", "description": "Hotel endpoints"},
    {"name": "Room", "description": "Room endpoints"},
    {"name": "Customer", "description": "Customer endpoints"},
    {"name": "Reservation", "description": "Reservation endpoints"},
    {"name": "Payment", "description": "Payment endpoints"},
    {"name": "Review", "description": "Review endpoints"},
]


app = FastAPI(openapi_tags=tags_metadata)


def get_db():
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        session.close()


class Dependency:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, id: int = None) -> List[ReturnType] | ReturnType | str:
        if id is not None:
            result = self.repo.get_by_id(id)
            if result is None:
                return f"Record with ID {id} not found"
            return result
        else:
            return self.repo.get_all()


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()
    container.register(AbcRepository, repository, instance=repository(session=session))
    container.register(Dependency)
    return container


app.add_api_route("/hotels/{hotel_id}", get_container(HotelRepository).resolve(Dependency), methods=["GET"], tags=["Hotel"])
app.add_api_route("/rooms/{room_id}", get_container(RoomRepository).resolve(Dependency), methods=["GET"], tags=["Room"])
app.add_api_route("/customers/{customer_id}", get_container(CustomerRepository).resolve(Dependency), methods=["GET"], tags=["Customer"])
app.add_api_route("/reservations/{reservation_id}", get_container(ReservationRepository).resolve(Dependency), methods=["GET"], tags=["Reservation"])
app.add_api_route("/reviews/{review_id}", get_container(ReviewRepository).resolve(Dependency), methods=["GET"], tags=["Review"])
app.add_api_route("/payments/{payment_id}", get_container(PaymentRepository).resolve(Dependency), methods=["GET"], tags=["Payment"])


@app.get("/available_rooms", tags=["Room"])
async def get_available_rooms():
    available_rooms = session.query(db.Room).filter_by(available=True).all()
    return [Room.model_validate(room) for room in available_rooms]


@app.get("/hotels/{hotel_id}/rooms", tags=["Hotel"])
async def get_hotel_rooms(hotel_id: int):
    hotel_rooms = session.query(db.Room).filter_by(hotel_id=hotel_id).all()
    return [Room.model_validate(room) for room in hotel_rooms]


@app.get("/hotels/{hotel_id}/customers", tags=["Hotel"])
async def get_hotel_customers(hotel_id: int):
    hotel_rooms = session.query(db.Room).filter_by(hotel_id=hotel_id).all()
    customers = [room.reservation.customer for room in hotel_rooms if room.reservation is not None]
    return [Customer.model_validate(customer) for customer in customers]


@app.post("/hotel", tags=["Hotel"])
def add_hotels(hotel: CreateHotel) -> str:
    session.add(db.Hotel(**hotel.model_dump()))
    session.commit()
    session.close()
    return "Hotel was added"


@app.post("/room", tags=["Room"])
def add_rooms(room: CreateRoom) -> str:
    session.add(db.Room(**room.model_dump()))
    session.commit()
    session.close()
    return "Room was added"


@app.get("/customers/{customer_id}/payments", tags=["Customer"])
async def get_customer_payments(customer_id: int):
    customer_reservations = session.query(db.Reservation).options(
        joinedload(db.Reservation.payment)
    ).filter_by(customer_id=customer_id).all()

    customer_payments = [res.payment for res in customer_reservations if res.payment is not None]

    return [Payment.model_validate(payment) for payment in customer_payments]


@app.post("/customer", tags=["Customer"])
def add_customers(customer: CreateCustomer) -> str:
    session.add(db.Customer(**customer.model_dump()))
    session.commit()
    session.close()
    return "Customer was added"

###############################
@app.post("/reservation", tags=["Reservation"])
def add_reservation(reservation: CreateReservation) -> str:
    room = session.query(db.Room).filter(db.Room.id == reservation.room_id).first()
    if not room.available:
        raise HTTPException(status_code=400, detail="Room is not available for reservation")

    session.add(db.Reservation(**reservation.model_dump()))
    session.commit()
    room.available = False
    session.commit()

    producer = create_kafka_producer()
    message = {'id': room.id, 'status': 'reserved'}
    producer.send('reservation_topic', json.dumps(message).encode('utf-8'))
    producer.flush()

    session.close()
    return "Reservation was added"

###################
@app.post("/payment", tags=["Payment"])
def add_payment(payment: CreatePayment):
    reservation = session.query(db.Reservation).get(payment.reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found.")

    new_payment = db.Payment(
        amount=payment.amount,
        reservation_id=payment.reservation_id
    )
    session.add(new_payment)
    session.commit()

    async_process_payment.send(new_payment.id, new_payment.amount)

    return {"message": "Payment initiated", "payment_id": new_payment.id}



@app.post("/review", tags=["Review"])
def add_review(review: CreateReview) -> str:
    session.add(db.Review(**review.model_dump()))
    session.commit()
    session.close()
    return "Review was added"
