import dramatiq
from dramatiq.results.backends.redis import RedisBackend
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
import requests
import time
from requests.exceptions import ReadTimeout
import sys
final_path = "/Users/dau04/Desktop/KBTU/KBTU_Advanced_Django/Final"

# Добавление пути к вашей директории в список путей поиска Python
sys.path.append(final_path)

from api.repositories.Repository import *
from redis_worker.tasks import update_order_status, add_to_history, total_orders_revenue_by_month, average_order_price,revenue_per_visitor
import datetime

result_backend = RedisBackend()
broker = RedisBroker()
broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(broker)



@dramatiq.actor(store_results=True)
def payment_operations(reservation_id: int):
    db: Session = next(get_db())
    while True:
        response = requests.get(f"http://127.0.0.1:8000/order/{reservation_id}")
        details = response.json()
        pay_status = details.get("pay")
        print(pay_status)
        if pay_status:
            update_order_status(reservation_id, db)
            return f"Payment has been completed for reservation ID: {reservation_id}"
        else:
            time.sleep(5)
            print("hi")
    
    
@dramatiq.actor(store_results=True)
def analysis_of_order(reservation_id: int):
    db: Session = next(get_db())
    service: OrderRepository = get_order_repo(db) 
    mdlOrder = service.get_order_by_reservation(reservation_id)
    add_to_history(mdlOrder, db)
    service.delete_order(reservation_id)
    return {
        "total_revenue": total_orders_revenue_by_month(db),
        "average_order_price": average_order_price(db),
        "revenue_per_visitor": revenue_per_visitor(db), 
    }


    