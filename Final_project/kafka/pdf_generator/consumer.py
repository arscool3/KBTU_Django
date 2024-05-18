import sys
from confluent_kafka import Consumer, KafkaException, KafkaError

from generator import generate_pdf


conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'room_1'
}

consumer = Consumer(conf)
running = True
MIN_COMMIT_COUNT = 13404013

def consume_loop(consumer, topics=[]):
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
                generate_pdf(msg=msg)
                msg_count += 1
                if msg_count % MIN_COMMIT_COUNT == 0:
                    consumer.commit(asynchronous=True)
    finally:
        consumer.close()

def shutdown():
    global running
    running = False

def start_consumer():
    consume_loop(consumer=consumer, topics=['room_1'])

start_consumer()