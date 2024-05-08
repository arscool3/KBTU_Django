from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
import api.models.schemas as sch
import api.database.database as db
import api.models.models as mdl
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.database.database import session
from api.repositories.Repository import *
from dramatiq.results.errors import ResultMissing
from kafka.producer import produce
import sys
from redis_worker.worker import payment_operations, result_backend
from sqlalchemy.sql import func

app = FastAPI()


@app.get('/menu')
def get_food_list(service: FoodRepository = Depends(get_food_repo)):
    result = service.get_foods()
    return [sch.Food.model_validate(food) for food in result]

@app.post('/add/food')
def create_food(food: sch.Food, service: FoodRepository = Depends(get_food_repo)):
    service.create_food(food)
    return "Food was added"

@app.post('/add/category')
def create_category(category: sch.Category ,service: CategoryRepository = Depends(get_category_repo)):
    service.create_category(category)

@app.get('/categories')
def get_categories(service: CategoryRepository = Depends(get_category_repo)):
    result = service.get_categories()
    return [sch.Category.model_validate(food) for food in result]

@app.post('/add/order/{reservation_id}')
def create_order(reservation_id: int, order: sch.CreateOrder, service: OrderRepository = Depends(get_order_repo)):
    service.create_order(order, reservation_id)
    return "Order was created"

@app.get("/orders")
def get_orders(service: OrderRepository = Depends(get_order_repo)):
    result = service.get_orders()
    return [sch.Order.model_validate(food) for food in result]


@app.post("/menu/{reservation_id}/add_to_order")
def add_to_order(orderitem: sch.OrderItem, reservation_id: int, service: OrderItemRepository = Depends(get_order_item_repo) ):
    service.add_food_to_order(orderitem, reservation_id)
    return "Item was added"

@app.get('/order/{reservation_id}')
def get_order_items(reservation_id:int ,service: OrderRepository = Depends(get_order_repo) ):
    result = service.get_order_by_reservation(reservation_id)
    return sch.Order.model_validate(result)
    

@app.get('/orders/{reservation_id}')
def get_order_items(reservation_id:int ,service: OrderItemRepository = Depends(get_order_item_repo) ):
    try:
        result = service.get_order_items_by_order(reservation_id)
        return [sch.OrderItem.model_validate(food) for food in result]
    except Exception:
        return "smth wrong"
    
@app.post('/payment/{reservation_id}')
def pay_order(reservation_id: int, db: Session = Depends(get_db), service: OrderRepository = Depends(get_order_repo)):
    service.update_status(reservation_id, "Ожидается оплата")
    task = payment_operations.send(reservation_id)
    status = mdl.PaymentStatus(reservation_id = reservation_id, status_code = task.message_id)
    db.add(status)
    return sch.PaymentStatus.model_validate(status)

@app.get('/status/{reservation_id}')
def get_status(reservation_id: int, db: Session = Depends(get_db), service: OrderRepository = Depends(get_order_repo)):
    result = db.query(mdl.PaymentStatus).filter(mdl.PaymentStatus.reservation_id == reservation_id).first()
    try:
        task = payment_operations.message().copy(message_id = result.status_code)
        return result_backend.get_result(task)
    except ResultMissing:
        return "Waiting for Payment"


    

   
@app.post('/pay/{reservation_id}')
def pay(reservation_id: int, service: OrderRepository = Depends(get_order_repo) ):
    order = service.pay(reservation_id)
    if order:
        service.update_status(reservation_id, "Заказ готовится") # Is first?
        return "Вы заплатили"
    else:
        raise HTTPException(status_code=404, detail=f"Order not found for reservation ID: {reservation_id}")


@app.post('/status/{reservation_id}/ready')
def update_status(reservation_id: int, service: OrderRepository = Depends(get_order_repo)):
    order = service.get_order_by_reservation(reservation_id)
    if order and (order.status == "Заказ готовится" or order.status == "Оплата прошла") :
        service.update_status(reservation_id, "Заказ готов")

@app.post('/status/{reservation_id}/completed')
def update_status(reservation_id: int, service: OrderRepository = Depends(get_order_repo)):
    order = service.get_order_by_reservation(reservation_id)
    if order:
        service.update_status(reservation_id, "Заказ выдан")
        produce(sch.Order.model_validate(order))
        return "Deleted"
    else:
        return "smth"

@app.post('/add/history')
def add_history(history: sch.History ,db: Session = Depends(get_db)):
    db.add(mdl.History(**history.model_dump()))


@app.get('/history')
def get_history(db: Session = Depends(get_db)):
    result = db.query(mdl.History).all()
    return [sch.History.model_validate(food) for food in result]



    
    
    