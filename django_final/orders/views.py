import random

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from foods.models import Food
from orders.choices import StatusChoices
from orders.models import Order
from orders.notifiers import OrderStatusChangeNotifier
from orders.serializers import OrderSerializer, OrderGetSerializer, OrderUpdateSerializer, OrderStatusUpdateSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    notifier = OrderStatusChangeNotifier()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'my_orders':
            return OrderGetSerializer
        if self.action == 'update':
            return OrderUpdateSerializer
        if self.action in ("mark_ready", "mark_given"):
            return OrderStatusUpdateSerializer

        return OrderSerializer

    @action(detail=False, methods=["GET"])
    def my_orders(self, request, *args, **kwargs):
        orders = self.queryset.filter(customer=request.user, status=StatusChoices.Waiting)
        serializer = self.get_serializer(orders, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance, is_new = Order.objects.get_or_create(food_id=serializer.data["food"], customer_id=request.user.id)
        if not is_new:
            instance.amount += 1
        else:
            instance.amount = serializer.data["amount"]

        food = Food.objects.get(id=serializer.data["food"])
        if instance.amount > food.amount:
            return Response(
                {
                    "detail": "К сожалению, у нас нет достаточного количества этого блюда :("
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        food.amount -= 1
        food.save()
        instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        food = Food.objects.get(id=instance.food.id)

        food.amount += instance.amount

        food.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def send_user_orders(self, request, *args, **kwargs):
        orders = Order.objects.filter(status="Waiting", customer_id=request.user.id)
        identifier = random.randint(100000, 999999)

        for order in orders:
            order.status = "Processing"
            order.order_identifier = identifier

        Order.objects.bulk_update(orders, fields=["status", "order_identifier"])

        return Response({"detail": "ok"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def get_active_orders(self, request, *args, **kwargs):
        if request.user.user_type == "Manager":
            order_status = request.query_params["order_status"]
            orders = self.queryset.filter(status=order_status)
        else:
            orders = Order.objects.filter(status__in=("Processing", "Completed"), customer_id=request.user.id)
            print(orders)
        serializer = OrderGetSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def order_history(self, request, *args, **kwargs):
        orders = self.queryset.filter(status="Given", customer_id=request.user.id)

        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def mark_ready(self, request, *args, **kwargs):
        serializer = OrderStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._mark_orders("Completed", serializer.data["order_identifier"])

        user_id = Order.objects.filter(order_identifier=serializer.data["order_identifier"]).first().customer_id

        self.notifier.notify(
            user_id,
            {"order_identifier": serializer.data["order_identifier"], "order_status": "Completed"}
        )

        return Response({"detail": "ok"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def mark_given(self, request, *args, **kwargs):
        serializer = OrderStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self._mark_orders("Given", serializer.data["order_identifier"])

        user_id = Order.objects.get(order_identifier=serializer.data["order_identifier"]).customer_id

        self.notifier.notify(
            user_id,
            {"order_identifier": serializer.data["order_identifier"], "order_status": "Given"}
        )

        return Response({"detail": "ok"}, status=status.HTTP_200_OK)

    def _mark_orders(self, status, identifier):
        orders = self.queryset.filter(order_identifier=identifier)

        for order in orders:
            order.status = status

        Order.objects.bulk_update(orders, fields=["status"])
