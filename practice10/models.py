from typing import Annotated

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base

_id = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]


class User(Base):
    __tablename__ = 'users'
    id: Mapped[_id]
    username: Mapped[str] = mapped_column(String(50))

    cart: Mapped['Cart'] = relationship( back_populates='user')
    store: Mapped['Store'] = relationship(back_populates='user')



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

    cartitem: Mapped['CartItem'] = relationship(back_populates='product')
    storeitem: Mapped['StoreItem'] = relationship(back_populates='product')



class Cart(Base):
    __tablename__ = 'carts'
    id: Mapped[_id]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped[User] = relationship(back_populates='cart')

    cartitem: Mapped['CartItem'] = relationship(back_populates="cart") 


class CartItem(Base):
    __tablename__ = 'cart_items'
    id: Mapped[_id]
    
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product: Mapped[Product] = relationship(back_populates='cartitem')

    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.id'))
    cart : Mapped[Cart] = relationship(back_populates='cartitem')
    
    quantity: Mapped[int]

class Store(Base):
    __tablename__ = 'stores'

    id: Mapped[_id] 
    store_name: Mapped[str]  = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='store')
    storeitem: Mapped['StoreItem'] = relationship(back_populates='store')

class StoreItem(Base):
    __tablename__ = 'storeitems'
    id: Mapped[_id] 

    store_id: Mapped[int] = mapped_column(ForeignKey('stores.id'))
    product_id: Mapped[int] =  mapped_column(ForeignKey('products.id'))
    
    store: Mapped[Store] = relationship(back_populates='storeitem')
    product: Mapped[Product] = relationship(back_populates='storeitem')