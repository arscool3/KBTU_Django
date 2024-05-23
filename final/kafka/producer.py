from typing import NewType
import confluent_kafka

producer=confluent_kafka.Producer(
    {
    "bootstrap.servers": "localhost:9092",
    }
)
topic='main_topic'
Message=NewType("Message",str)

def produce(message:Message) -> None :
    producer.produce(topic=topic, value=message)
    producer.flush() 
    print(f'Produced message : {message} into topic :{topic}')


if __name__=="__main__":
    message=Message("Hello, producer")
    produce(message)

