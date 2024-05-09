from typing import Annotated
from api.database.database import Base
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func
from sqlalchemy import Boolean, DateTime, func, Column


_id = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]

class User(Base):
    __tablename__ = "users"
    id: Mapped[_id]
    login: Mapped[str] = mapped_column(String, nullable=False, unique=True, primary_key=True)
    password: Mapped[str] = mapped_column(String)

class Food(Base):
    __tablename__ = "foods"
    id: Mapped[_id]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]

    order_item: Mapped['OrderItem'] = relationship(back_populates='food')
    category: Mapped['Category'] = relationship(back_populates='food')

    history_item: Mapped['HistoryItems'] = relationship(back_populates='food')

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[_id]
    reservation: Mapped[int]
    created_at: Mapped[str] = mapped_column(default= func.now())
    status: Mapped[str] = mapped_column(default= "Created")
    pay: Mapped[bool] = mapped_column(default= False)
    total: Mapped[int] = mapped_column(default = 0, nullable= False)
    order_item: Mapped['OrderItem'] = relationship(back_populates='order', cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "orderitems"
    id: Mapped[_id]
    
    food_id: Mapped[int] = mapped_column(ForeignKey("foods.id"))
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    quantity: Mapped[int] = mapped_column(default=1)


    food: Mapped['Food'] = relationship(back_populates='order_item')
    order: Mapped['Order'] = relationship(back_populates='order_item')

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[_id]
    name: Mapped[str]

    food: Mapped['Food'] = relationship(back_populates='category')



class PaymentStatus(Base):
    __tablename__ = "payments"
    id: Mapped[_id]
    status_code: Mapped[str]
    reservation_id: Mapped[int]

class HistoryItems(Base):
    __tablename__ = "historyitems"
    id: Mapped[_id]
    
    food_id: Mapped[int] = mapped_column(ForeignKey("foods.id"))
    history_id: Mapped[int] = mapped_column(ForeignKey("history.id"))

    quantity: Mapped[int] = mapped_column(default=1)


    food: Mapped['Food'] = relationship(back_populates='history_item')
    history: Mapped['History'] = relationship(back_populates='history_item')


class History(Base):
    __tablename__ = "history"
    id: Mapped[_id]
    reservation: Mapped[int]
    datetime = Column(DateTime, default=func.now()) 
    total: Mapped[int]

    history_item: Mapped['HistoryItems'] = relationship(back_populates='history')
    

    



