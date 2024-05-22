from django.db.models import Avg
from rest_framework import viewsets, status
from rest_framework.response import Response
from users.permissions import IsAdminOrReadOnly
from shop.models import WarehouseItem, Shop
from .models import Category, Product, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAdminOrReadOnly,)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    # permission_classes = (IsAdminOrReadOnly,)

    def get_subcategories_of_category(self, req, category_id):
        queryset = SubCategory.objects.all().filter(category_id=category_id)
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#     permission_classes = (IsAdminOrReadOnly,)

    def get_products_avg_price(self, request, product_id):
        warehouse_items = WarehouseItem.objects.filter(product_id=product_id)

        res = warehouse_items.aggregate(Avg('price'))
        return Response(res)
    def get_subcategory_name(self, request, sabcategory_id):
        subcat = SubCategory.objects.get(id=sabcategory_id)
        return Response({"subcat_name": subcat.name})
    def get_products_of_shop(self, request, shop_id):
        warehouse_items = WarehouseItem.objects.filter(shop_id=shop_id)

        products = Product.objects.filter(pk__in=warehouse_items)

        serializer = ProductSerializer(data=products, many=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def get_category_products_rating_price(self,
                                           request,
                                           category_id,
                                           min_rating: int = 0,
                                           min_price: int = 0,
                                           max_price: int = 1e9):
        subcategories = SubCategory.objects.filter(category_id=category_id)
        products = Product.objects.filter(subcategory__in=subcategories)

    def get_category_subcategory_products_rating_price(self,
                                                       request,
                                                       category_id,
                                                       subcategory_id,
                                                       min_rating: int = 0,
                                                       min_price: int = 0,
                                                       max_price: int = 1e9):
        pass

    def get_category_products(self, request, category_id):
        subcategories = SubCategory.objects.all().filter(category_id=category_id)
        queryset = Product.objects.filter(subcategory__in=subcategories)

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_products_min_rating(self, request, min):
        queryset = Product.objects.all().filter(rating__gte=min)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_popular_products(self, request):
        queryset = Product.objects.all().order_by('-rating')
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def search_by_name(self, request):
        pattern = request.data['name']
        queryset = Product.objects.filter(name__icontains=pattern)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def searching(self, request, query):
        results_by_name = Product.objects.filter(name__icontains=query)
        results_by_descr = Product.objects.filter(description__icontains=query)
        results_by_subcat = Product.objects.filter(subcategory__name__icontains=query)
        results_by_cat = Product.objects.filter(subcategory__category__name__icontains=query)
        results = results_by_name.union(results_by_descr).union(results_by_subcat).union(results_by_cat)

        serializer = ProductSerializer(results, many=True)
        return Response(serializer.data)

    def searching_trigram(self, request, query):
        pass

    def put_rating_to_product(self, request, product_id):
            rating = request.data['rating']

            product = Product.objects.get(id=product_id)
            product.rate_cnt = product.rate_cnt + 1
            product.rating = (product.rating + rating) / product.rate_cnt
            product.save()
            return Response(data=product.rating, status=status.HTTP_200_OK)

    def get_subcategory_products(self, req, category_id, subcat_id):
        queryset = Product.objects.all().filter(subcategory_id=subcat_id)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
