from django.views.generic import ListView, DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin

# View current user orders
class UserOrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/user_orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# View specific order details
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
