import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from order import fetch_order, check_delivery_status, update_order_status

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)


@dramatiq.actor(store_results=True)
def update_delivery_status_task(order_id: str):
    print('Starting status update for order:', order_id)
    order_info = fetch_order(order_id)
    delivery_status = check_delivery_status(order_info['shipping_tracking_number'])

    if delivery_status == 'Delivered':
        update_order_status(order_id, 'Delivered')
        print('Order', order_id, 'has been delivered.')
    else:
        update_order_status(order_id, 'In Transit')
        print('Order', order_id, 'is still in transit.')
    return delivery_status
