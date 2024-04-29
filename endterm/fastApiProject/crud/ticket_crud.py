from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Ticket, Plane
import schemas

def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def get_tickets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ticket).offset(skip).limit(limit).all()

def get_tickets_available(db: Session, skip: int = 0, limit: int = 10, plane_name: str = ""):
    query = db.query(Ticket).join(Plane)
    if plane_name is not None:
        query = query.filter(func.lower(Plane.name).contains(plane_name.lower()))
    return query.filter(Ticket.is_reserved == False).offset(skip).limit(limit).all()

def reserve_ticket(db: Session, ticket_id: int):
    db_ticket = get_ticket(db, ticket_id)
    if db_ticket is None:
        return None
    if db_ticket.is_reserved:
        return "reserved"
    db_ticket.is_reserved = True
    db.commit()
    return db_ticket

def update_ticket(db: Session, ticket_id: int, ticket: schemas.TicketCreate):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        for var, value in ticket:
            setattr(db_ticket, var, value)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket
    return None

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
        return db_ticket
    return None
