from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment, Author, Category

class PostListView(ListView):
    model = Post
    queryset = Post.objects.published()  # Using a custom queryset method
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'author', 'categories', 'status']
    template_name = 'blog/post_form.html'  # Specify your custom template name

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('post-list')  # Adjust with your named URL for listing posts

class CommentCreateView(CreateView):
    model = Comment
    fields = ['post', 'name', 'email', 'body']

# Assume similar views for `Author` and `Category` listings and details
