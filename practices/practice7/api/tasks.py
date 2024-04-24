import dramatiq
from django.core.mail import send_mail
from .models import Subscriber, BlogPost

@dramatiq.actor
def send_new_blog_post_notification(blog_post_id):
    try:
        blog_post = BlogPost.objects.get(pk=blog_post_id)
        subscribers = Subscriber.objects.all()
        
        subject = f'New Blog Post: {blog_post.title}'
        message = f'A new blog post titled "{blog_post.title}" has been published.'
        from_email = 'sala.mse2004@gmail.com'
        to_emails = [subscriber.email for subscriber in subscribers]
        send_mail(subject, message, from_email, [to_emails])
        
        print(f"Notification email sent for new blog post '{blog_post.title}'")
        
    except BlogPost.DoesNotExist:
        print(f"Blog post with id {blog_post_id} does not exist")

