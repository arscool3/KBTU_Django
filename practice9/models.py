from typing import Annotated

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base

_id = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]



class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[_id]
    name: Mapped[str] = mapped_column(String(50))
    photo_url: Mapped[str]
    product: Mapped['Product'] = relationship(back_populates='category')


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[_id]
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int]
    description: Mapped[str]
    photo_url: Mapped[str]

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id')) 
    category: Mapped['Category'] = relationship(back_populates='product')



