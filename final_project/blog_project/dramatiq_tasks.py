import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

# Broker setup
broker = RabbitmqBroker(url="amqp://guest:guest@localhost:5672")
dramatiq.set_broker(broker)

@dramatiq.actor
def process_post_creation(post_id):
    from posts.models import Post
    post = Post.objects.get(id=post_id)
    
    print(f"Post processed with title: {post.title}")