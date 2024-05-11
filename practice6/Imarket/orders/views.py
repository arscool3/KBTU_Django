from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import json
from shop.models import WarehouseItem
from .models import Order, OrderItem

from .serializers import OrderSerializer, OrderItemSerializer
from users.permissions import IsAdminOrReadOnly, IsCustomer


def get_last_order(user_id):
    orders = Order.objects.filter(user_id=user_id)
    if orders.exists():
        return orders.last()
    return -1


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAdminOrReadOnly, IsCustomer)

    def purchase_orderitems_in_order(self, request, user_id):  # aka: purchase_orderitems_in_cart
        last_order = get_last_order(user_id)
        serializer = OrderSerializer(instance=last_order, data=request.data)
        if user_id != request.data["user"]:
            return Response({"error": "user_id must be same as in URL as in BODY"}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()

            new_order = Order(user_id=user_id)
            new_order.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    # permission_classes = (IsAdminOrReadOnly, IsCustomer)

    def get_order_items_in_cart(self, request, user_id):
        last_order = get_last_order(user_id)
        if last_order == -1:
            return Response({"message": "you are seller or please create cart"})

        queryset = OrderItem.objects.filter(order=last_order)
        serializer = OrderItemSerializer(queryset, many=True)
        products = []
        for ordered_dicts in serializer.data:
            product_in_cart = json.loads(json.dumps(ordered_dicts))
            whi = WarehouseItem.objects.get(id=product_in_cart['warehouse_item'])
            item = {
                "order_item_id": product_in_cart['id'],
                "product_id": whi.product.id,
                "name": whi.product.name,
                "quantity": product_in_cart['quantity'],
                "shop_name": whi.shop.name,
                "priceInThisShop": whi.price,
            }
            products.append(item)

        return Response(products)

    def get_user_orders(self, request, user_id):
        queryset = Order.objects.filter(user_id=user_id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_user_order_orderitems(self, request, order_id):
        queryset = OrderItem.objects.filter(order_id=order_id)
        serializer = OrderItemSerializer(queryset, many=True)
        products = []
        for ordered_dicts in serializer.data:
            product_in_cart = json.loads(json.dumps(ordered_dicts))
            whi = WarehouseItem.objects.get(id=product_in_cart['warehouse_item'])
            order = Order.objects.get(id=order_id)
            item = {
                "order_item_id": product_in_cart['id'],

                "delivery_date": order.delivery_date,
                "delivery_address": order.delivery_address,
                "delivery_price": order.delivery_price,

                "product_id": whi.product.id,
                "product_name": whi.product.name,
                "quantity": product_in_cart['quantity'],
                "shop_name": whi.shop.name,
                "priceInThisShop": whi.price,
            }
            products.append(item)
        return Response(products)


    def delete_order_item_from_order(self, request, orderitem_id):  # aka: delete_orderitem_from_cart
        try:
            deleting_order_item = OrderItem.objects.get(id=orderitem_id)
        except OrderItem.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        deleting_order_item.warehouse_item.quantity += deleting_order_item.quantity
        deleting_order_item.warehouse_item.save()

        deleting_order_item.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)

    def add_order_item_to_order(self, request, user_id):  # aka: add_product_to_cart
        last_order = get_last_order(user_id)
        if last_order == -1:
            return Response({"message": "you are seller or please create cart"})

        data = request.data
        data["order"] = last_order.id

        serializer = OrderItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            warehouse_item_id = serializer.data["warehouse_item"]
            warehouse_item = WarehouseItem.objects.get(id=warehouse_item_id)
            order_item_quantity = serializer.data["quantity"]

            warehouse_item.quantity = warehouse_item.quantity - order_item_quantity
            warehouse_item.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
