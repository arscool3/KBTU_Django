from rest_framework import viewsets
from .models import Category, Product, Order, OrderItem, Review, Address
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, OrderItemSerializer, ReviewSerializer, AddressSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .tasks import update_product_stock
from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductFilter
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']

    @action(detail=True, methods=['post'])
    def set_price(self, request, pk=None):
        product = self.get_object()
        new_price = request.data.get('price')
        product.price = new_price
        product.save()
        return Response({'status': 'price set'})

    @action(detail=False)
    def low_stock(self, request):
        products = Product.objects.filter(stock__lt=10)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

def product_list(request):
    product_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'shop/product_list.html', {'filter': product_filter, 'products': product_filter.qs})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def product_reviews(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_reviews', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'shop/product_reviews.html', {'product': product, 'form': form, 'reviews': reviews})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        product = self.get_object()
        reviews = Review.objects.filter(product=product)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_products.html', {'category': category, 'products': products})

#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    reviews = Review.objects.filter(product=product)
#    if request.method == 'POST':
#        form = ReviewForm(request.POST)
#        if form.is_valid():
#            review = form.save(commit=False)
#            review.product = product
#            review.user = request.user
#            review.save()
#            return redirect('product_reviews', pk=pk)
#    else:
#        form = ReviewForm()
#    return render(request, 'shop/product_reviews.html', {'product': product, 'form': form, 'reviews': reviews})