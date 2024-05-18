from telegram import send_pdf
import sys
from confluent_kafka import Consumer, KafkaException, KafkaError
from email_sender import send_pdf_to_email
import json
from database import make_database_record, check_in_database


conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'pdf_sender_service'
}

consumer = Consumer(conf)
running = True
MIN_COMMIT_COUNT = 13404013

def consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        msg_count = 0
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                kafka_data = msg.value().decode('utf-8')
                json_data = kafka_data.replace("'", "\"")
                data = json.loads(json_data)
                file_path = msg.key().decode('utf-8')
                if not check_in_database(data['bin']):
                    make_database_record(data, file_path=file_path)
                send_pdf(data.get('tg_id'), file_name=file_path)
                send_pdf_to_email(data.get('email'), pdf_url=file_path)

                msg_count += 1
                if msg_count % MIN_COMMIT_COUNT == 0:
                    consumer.commit(asynchronous=True)
    finally:
        consumer.close()

def shutdown():
    global running
    running = False

def start_consumer():
    consume_loop(consumer=consumer, topics=['pdf_sender_service'])