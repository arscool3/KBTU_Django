from confluent_kafka import Producer
import api.models.models as mdl
import api.models.schemas as sch

producer = Producer(
    {"bootstrap.servers": "localhost: 9092"}
)

topic = "main_topic"


def produce(order: sch.Order ):
    producer.produce(topic = topic, value = order.model_dump_json())
    producer.flush()