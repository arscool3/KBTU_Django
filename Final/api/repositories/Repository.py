from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
import api.models.schemas as sch
import api.models.models as mdl
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from api.database.database import session


class FoodRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_food(self, food: sch.Food):
        self.db.add(mdl.Food(**food.model_dump()))
        return "Food was created"
    
    def get_food(self, id: int):
        return self.db.query(mdl.Food).filter(mdl.Food.id == id).first()
        
    
    def get_foods(self):
        return self.db.query(mdl.Food).all()
        
    def get_foods_by_category(self, id: int):
        return self.db.query(mdl.Food).filter(mdl.Food.category_id == id).all()
    
    def delete_food(self, id: int):
        product = self.get_food(id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return product
        return None
        
class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_category(self, category: sch.Category):
        self.db.add(mdl.Category(**category.model_dump()))
        return "Category was created"
    
    def get_category(self, id: int):
        return self.db.query(mdl.Category).filter(mdl.Category.id == id).first()
    
    def get_categories(self):
        return self.db.query(mdl.Category).all()
    
    def delete_category(self, id: int):
        category = self.get_category(id)
        if category:
            self.db.delete(category)
            self.db.commit()
            return category
        return None
    
class OrderRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_order(self, order: sch.CreateOrder, id: int):
        order = mdl.Order(reservation = id)
        self.db.add(order)
        return "Order was created"
    
    def get_order_by_reservation(self, reservation: int):
        return self.db.query(mdl.Order).filter(mdl.Order.reservation == reservation).first()
    
    def update_status(self, reservation: int, status: str):
        order = self.get_order_by_reservation(reservation)
        if order:
            order.status = status
            order.created_at = func.now()
            self.db.commit()
        return order
    
    def pay(self, reservation: int):
        order = self.get_order_by_reservation(reservation)
        if order:
            order.pay = True
            self.db.commit()
        return order
    def delete_order(self, id: int):
        order = self.get_order_by_reservation(id)
        if order:
            orderitems = self.db.query(mdl.OrderItem).filter(mdl.OrderItem.order_id == order.id).all()
            for orderitem in orderitems:
                self.db.delete(orderitem)
            self.db.delete(order)
            self.db.commit()
            return order
        return None
        
    def get_orders(self):
        return self.db.query(mdl.Order).all()
    

class OrderItemRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_order_items(self, orderitem: sch.OrderItem):
        self.db.add(mdl.OrderItem(**orderitem.model_dump()))
        return "OrderItem was created"
    
    def add_food_to_order(self, orderitem: sch.OrderItem, reservation: int):
        order = self.db.query(mdl.Order).filter(mdl.Order.reservation == reservation).first()
        if order:
            order_item = mdl.OrderItem(food_id = orderitem.food_id, order_id = order.id, quantity = orderitem.quantity)
            self.db.add(order_item)
        else:
            return "Order not found"
    
    def get_order_items_by_order(self, reservation: int):
        try:
            order = self.db.query(mdl.Order).filter(mdl.Order.reservation == reservation).first()
            return self.db.query(mdl.OrderItem).filter(mdl.OrderItem.order_id == order.id).all()
        except Exception:
            return "smth wrong"
    
    
    def delete_orderitem_from_order(self, reservation_id: int, orderitem_id: int):
        order = self.db.query(mdl.Order).filter(mdl.Order.reservation == reservation_id).first()
        if order and not order.pay:
            orderitem = self.db.query(mdl.OrderItem).filter(mdl.OrderItem.food_id == orderitem_id and mdl.OrderItem.order_id == order.id)
            self.db.delete(orderitem)
            self.db.commit()
            return order
        return None
    

def get_db():
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        session.close()

def get_food_repo(db: Session = Depends(get_db)):
    return FoodRepository(db)


def get_category_repo(db: Session = Depends(get_db)):
    return CategoryRepository(db)

def get_order_repo(db: Session = Depends(get_db)):
    return OrderRepository(db)

def get_order_item_repo(db: Session = Depends(get_db)):
    return OrderItemRepository(db)