import confluent_kafka
consumer=confluent_kafka.Consumer(
    {
    "bootstrap.servers": "localhost:9092","group.id":"main_group",
    }
)
topic="main_topic"
consumer.subscribe([topic])

number_of_messages=5
def consume():

    try:
        while True:
            messages=consumer.consume(num_messages=number_of_messages,timeout=1.5)
            if messages is None:

                continue
            print(f"Consumed {len(messages)}")
            #getting the value of the object
            for message in messages:
                print(message.value().decode("utf-8"))
    except Exception as e:
        print(f"Raised {e}")
    finally:
        consumer.close()



if __name__=="__main__":
    consume()
    print("Hello,consumer")

