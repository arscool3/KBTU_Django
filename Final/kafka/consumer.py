import json, sys

final_path = "/Users/dau04/Desktop/KBTU/KBTU_Advanced_Django/Final"

# Добавление пути к вашей директории в список путей поиска Python
sys.path.append(final_path)

import confluent_kafka
import api.models.models as mdl

from redis_worker.worker import analysis_of_order, result_backend
from api.repositories.Repository import *



final_path = "/Users/dau04/Desktop/KBTU/KBTU_Advanced_Django/Final"

# Добавление пути к вашей директории в список путей поиска Python
sys.path.append(final_path)

consumer = confluent_kafka.Consumer(
    {"bootstrap.servers": "localhost: 9092", "group.id": "main_group"}
)

topic = "main_topic"

consumer.subscribe([topic])
number_of_messages = 1

def consume():
    try:
        while True:
            messages = consumer.consume(num_messages=number_of_messages, timeout=1.5)
            for message in messages:
                order = sch.Order.model_validate(json.loads(message.value().decode("utf-8")))
                print(order)
                task = analysis_of_order.send(order.reservation)
                result = analysis_of_order.message().copy(message_id = task.message_id)
                print(result_backend.get_result(result))
    except Exception as e:
        print("Raised", e)
    finally:
        consumer.close()


if __name__ == "__main__":
    consume()
