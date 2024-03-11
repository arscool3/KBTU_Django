from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, MenuItem, Order, Delivery

from django.http import JsonResponse, HttpResponseNotAllowed

@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', '')
        customer = Customer.objects.create(name=name, email=email, phone_number=phone_number)
        return JsonResponse({'message': 'Customer created successfully', 'customer_id': customer.id})
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def create_menu_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        menu_item = MenuItem.objects.create(name=name, description=description, price=price)
        return JsonResponse({'message': 'Menu item created successfully', 'menu_item_id': menu_item.id})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        is_delivery = request.POST.get('is_delivery', False)
        customer = Customer.objects.get(id=customer_id)
        order = Order.objects.create(customer=customer, is_delivery=is_delivery)
        return JsonResponse({'message': 'Order created successfully', 'order_id': order.id})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def create_delivery(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        delivery_address = request.POST.get('delivery_address')
        order = Order.objects.get(id=order_id)
        delivery = Delivery.objects.create(order=order, delivery_address=delivery_address)
        return JsonResponse({'message': 'Delivery created successfully', 'delivery_id': delivery.id})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def get_customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_list = [{'id': customer.id, 'name': customer.name, 'email': customer.email, 'phone_number': customer.phone_number} for customer in customers]
        return JsonResponse(customer_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def get_menu_items(request):
    if request.method == 'GET':
        menu_items = MenuItem.objects.all()
        menu_item_list = [{'id': menu_item.id, 'name': menu_item.name, 'description': menu_item.description, 'price': menu_item.price} for menu_item in menu_items]
        return JsonResponse(menu_item_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def get_orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        order_list = [{'id': order.id, 'customer': order.customer.name, 'is_delivery': order.is_delivery} for order in orders]
        return JsonResponse(order_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def get_deliveries(request):
    if request.method == 'GET':
        deliveries = Delivery.objects.all()
        delivery_list = [{'id': delivery.id, 'order': delivery.order.id, 'delivery_address': delivery.delivery_address} for delivery in deliveries]
        return JsonResponse(delivery_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})
