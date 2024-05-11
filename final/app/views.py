from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Worker, Customer, Stock, Product, ProductsInStock, Order, Delivery
from .serializers import *


class CreateWorkerView(CreateAPIView):
    serializer_class = CreateWorkerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = Worker.objects.filter(user=serializer.save()).all()[0]
        return Response({"customer": WorkerSerializer(customer).data})


class WorkerViewSet(ReadOnlyModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.filter()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Worker.objects.filter(user=self.request.user).all()

    @action(detail=False, methods=["get"])
    def is_workers_enough(self, request):
        stock_area_counter = 0
        for stock in Stock.objects.all():
            stock_area_counter += int(stock.area)

        total_workers = Worker.objects.count()
        working_areas = stock_area_counter // 20
        if total_workers >= working_areas:
            return Response("Workers is enough")
        return Response("Workers isn't enough, we need another " + str(working_areas - total_workers))

class CreateCustomerView(CreateAPIView):
    serializer_class = CreateCustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = Customer.objects.filter(user=serializer.save()).all()[0]
        return Response({"customer": CustomerSerializer(customer).data})


class CustomerViewSet(ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if Worker.objects.filter(user=self.request.user).exists():
            return Customer.objects.all()
        return Customer.objects.filter(user=self.request.user).all()

    @action(detail=False, methods=["get"])
    def do_we_need_advertising(self, request):
        stock_area_counter = 0
        for stock in Stock.objects.all():
            stock_area_counter += int(stock.area)

        total_customers = Customer.objects.count()
        customer_areas = stock_area_counter // 5
        if total_customers >= customer_areas:
            return Response("Advertising is enough")
        return Response("Advertising is enough, we lacks another " + str(customer_areas - total_customers) + " customers")

    @action(detail=False, methods=["get"])
    def is_workers_enough(self, request):
        stock_area_counter = 0
        for stock in Stock.objects.all():
            stock_area_counter += int(stock.area)

        total_workers = Worker.objects.count()
        if total_workers >= stock_area_counter / 20:
            return Response("Workers is enough")


class StockViewSet(ReadOnlyModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductsInStockViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductsInStockSerializer
    queryset = ProductsInStock.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if Worker.objects.filter(user=self.request.user).exists():
            return Order.objects.all()
        return Order.objects.filter(customer__user=self.request.user).all()

    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)
        obj = ProductsInStock.objects.filter(product__pk=request.data['products']).filter(stock__pk=request.data['stock']).all()[0]
        obj.quantity -= int(request.data['quantity'])
        obj.save()
        return result


class DeliveryViewSet(ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Delivery.objects.filter(worker__user=self.request.user).all()

    def create(self, request, *args, **kwargs):
        result = super().create(request, *args, **kwargs)
        obj = ProductsInStock.objects.filter(product__pk=request.data['products']).filter(stock__pk=request.data['stock']).all()[0]
        obj.quantity += int(request.data['quantity'])
        obj.save()
        return result
