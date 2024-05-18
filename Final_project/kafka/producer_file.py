from kafka_final_package.KafkaProducer import KafkaAsyncProducer

config = {
    'bootstrap.servers': 'localhost:9092'
}

async def add_data_to_aggregating_queue(key, value):
    async with KafkaAsyncProducer(**config) as producer:
        await producer.send_message_async('room_1', key=key, value=value)

async def add_data_to_aggregated_queue(key, value):
    async with KafkaAsyncProducer(**config) as producer:
       await producer.send_message_async('pdf_sender_service', key=key, value=value)