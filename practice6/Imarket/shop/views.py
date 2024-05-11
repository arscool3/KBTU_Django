from rest_framework import viewsets, status
from rest_framework.response import Response

from orders.models import Order, OrderItem, WarehouseItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from products.models import Product, SubCategory
from users.permissions import IsOwnerOfShop, IsOwnerOfWarehouseItem, IsAdminOrReadOnly
from .models import Shop, WarehouseItem
from .serializers import ShopSerializer, WarehouseItemSerializer
import json


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    # permission_classes = (IsAdminOrReadOnly, IsOwnerOfShop)
    def get_shop_info(self, request, user_id):
        shop = Shop.objects.get(seller_id=user_id)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put_rating_to_shop(self, request, shop_id, new_rating):
        shop = Shop.objects.get(id=shop_id)
        shop.rate_cnt = shop.rate_cnt + 1
        shop.rating = (shop.rating + new_rating) / shop.rate_cnt
        shop.save()
        return Response(data=shop.rating, status=status.HTTP_200_OK)

    def get_shops_of_category(self, request, category_id):
        subcategories = SubCategory.objects.filter(category_id=category_id)
        products = Product.objects.filter(subcategory_id__in=subcategories)
        warehouse_items = WarehouseItem.objects.filter(product_id__in=products)

        shops = Shop.objects.filter(id__in=warehouse_items)

        serializer = ShopSerializer(data=shops, many=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def get_sold_products(self, request, shop_id):
        taken_orders = Order.objects.filter(completed=True)
        taken_order_items = OrderItem.objects.filter(order__in=taken_orders)
        serializer = OrderItemSerializer(taken_order_items, many=True)

        result = []

        for ordered_dicts in serializer.data:
            orderitem = json.loads(json.dumps(ordered_dicts))

            item = {
                "quantity": orderitem['quantity'],
                "product_id": WarehouseItem.objects.get(id=orderitem['warehouse_item']).product.id,
                "product_name": WarehouseItem.objects.get(id=orderitem['warehouse_item']).product.name,
                "price": WarehouseItem.objects.get(id=orderitem['warehouse_item']).price,
            }

            result.append(item)

        return Response(result)

    def get_shops_of_subcategory(self, request, subcat_id):
        products = Product.objects.filter(subcat_id=subcat_id)

        warehouse_items = WarehouseItem.objects.filter(product_id__in=products)

        shops = Shop.objects.filter(id__in=warehouse_items)

        serializer = ShopSerializer(data=shops, many=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = WarehouseItem.objects.all()
    serializer_class = WarehouseItemSerializer

    # permission_classes = (IsAdminOrReadOnly, IsOwnerOfWarehouseItem)
    def get_sold_products(self, request, user_id):
        taken_orders = Order.objects.filter(completed=True).filter(user_id=user_id)
        taken_order_items = OrderItem.objects.filter(order__in=taken_orders)
        serializer = OrderItemSerializer(taken_order_items, many=True)

        result = []

        for ordered_dicts in serializer.data:
            orderitem = json.loads(json.dumps(ordered_dicts))
            item = {
                "quantity": orderitem['quantity'],
                "product_id": WarehouseItem.objects.get(id=orderitem['warehouse_item']).product.id,
                "product_name": WarehouseItem.objects.get(id=orderitem['warehouse_item']).product.name,
                "price": WarehouseItem.objects.get(id=orderitem['warehouse_item']).price,
            }
            result.append(item)
        return Response(result)

    def get_warehouse_items_min_max_price(self, request, min=0, max=1e9):
        queryset = WarehouseItem.objects.filter(price__range=(min, max))
        serializer = WarehouseItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_warehouse_items_of_shop(self, request, shop_id):
        queryset = WarehouseItem.objects.filter(shop_id=shop_id)
        serializer = WarehouseItemSerializer(queryset, many=True)
        items = []

        for ordered_dicts in serializer.data:
            warehouse_item = json.loads(json.dumps(ordered_dicts))
            #                 print("\n->", warehouse_item)
            item = {
                "id": warehouse_item['id'],
                "price": warehouse_item['price'],
                "quantity": warehouse_item['quantity'],
                "product_id": warehouse_item['product'],
                "name": Product.objects.get(id=warehouse_item['product']).name,
                "shop_id": warehouse_item['shop'],
            }
            items.append(item)
        return Response(items)

    def get_warehouse_items_of_product(self, request, product_id):
        queryset = WarehouseItem.objects.filter(product_id=product_id)
        serializer = WarehouseItemSerializer(queryset, many=True)

        return Response(serializer.data)
