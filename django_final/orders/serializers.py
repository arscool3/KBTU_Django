from rest_framework import serializers

from foods.models import Food
from foods.serializers import FoodSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("status", "order_identifier")

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        # representation["customer"] = instance.customer.id

        return representation


class OrderGetSerializer(serializers.ModelSerializer):
    food = FoodSerializer()
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("status", "order_identifier")


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("amount", "special_wishes")


class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("order_identifier", )

