import os
from kafka import KafkaProducer, KafkaConsumer


def create_kafka_producer():
    kafka_server = os.getenv('KAFKA_SERVER', 'localhost:9092')
    try:
        producer = KafkaProducer(bootstrap_servers=[kafka_server])
        print("Kafka Producer has been created successfully")
        return producer
    except Exception as e:
        print(f"Failed to create Kafka Producer: {e}")
        return None


def create_kafka_consumer(topic):
    kafka_server = os.getenv('KAFKA_SERVER', 'localhost:9092')
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[kafka_server],
            auto_offset_reset='earliest',
            group_id='my-group'
        )
        print("Kafka Consumer has been created successfully")
        return consumer
    except Exception as e:
        print(f"Failed to create Kafka Consumer: {e}")
        return None


if __name__ == "__main__":
    producer = create_kafka_producer()
    if producer:
        producer.send('my-topic', b'Test message')
        producer.flush()

    consumer = create_kafka_consumer('my-topic')
    if consumer:
        for message in consumer:
            print(f"Received message: {message.value}")