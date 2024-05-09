from api.models.models import Order, History
from api.repositories.Repository import *
import datetime
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import Session
from api.models.models import Order

def update_order_status(reservation_id: int, db: Session):
    order = db.query(Order).filter(Order.reservation == reservation_id).first()
    if order:
        order.status = "Оплата прошла"
        db.commit()


def add_to_history(order: mdl.Order, db: Session = Depends(get_db)):
    try:
        history = mdl.History(
            reservation=order.reservation,
            datetime=datetime.datetime.now(),
            total=order.total
        )        
        db.add(history)
        
        orderitems = db.query(mdl.OrderItem).filter(mdl.OrderItem.order_id == order.id).all()
        
        for orderitem in orderitems:
            history_item = mdl.HistoryItems(
                food_id = orderitem.food_id,
                history_id = history.id,
                quantity = orderitem.quantity
            )
            db.add(history_item)
        
        db.commit()
        
        return {"message": "Order successfully added to history"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
    
def total_orders_revenue_by_month(db: Session = Depends(get_db)):
    try:
        today = datetime.date.today()
        current_month_start = datetime.date(today.year, today.month, 1)
        current_month_end = datetime.date(today.year, today.month, today.day)

        total_revenue = db.query(func.sum(History.total)).filter(
            History.datetime >= current_month_start,
            History.datetime <= current_month_end
        ).scalar()

        return float(total_revenue)
    except SQLAlchemyError as e:
        return 0
def average_order_price(db: Session = Depends(get_db)):
    try:
        average_order_price = db.query(func.avg(History.total)).scalar()
        return float(average_order_price)
    except SQLAlchemyError as e:
        return 0





def revenue_per_visitor(db: Session = Depends(get_db)):
    try:
        revenue_per_visitor = db.query(func.sum(History.total) / func.count(History.reservation)).scalar()
        return float(revenue_per_visitor)
    except SQLAlchemyError as e:
        return 0


