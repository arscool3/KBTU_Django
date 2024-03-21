from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class StoreManager(models.Manager):
    def get_queryset(self):
        return StoreQuerySet(self.model, using=self._db)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)


class ManufacturerManager(models.Manager):
    def get_queryset(self):
        return ManufacturerQuerySet(self.model, using=self._db)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Store(Base):
    location = models.CharField(max_length=200)
    objects = StoreManager()


class Category(Base):
    description = models.TextField()
    objects = CategoryManager()


class Manufacturer(Base):
    country = models.CharField(max_length=100)
    objects = ManufacturerManager()


class Product(Base):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    store = models.ManyToManyField(Store)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    objects = ProductManager()


class StoreQuerySet(models.QuerySet):
    def ordered_by_location(self):
        return self.order_by('location')

    def has_products(self):
        return self.filter(product__isnull=False).distinct()


class CategoryQuerySet(models.QuerySet):
    def ordered_by_description(self):
        return self.order_by('description')

    def popular(self):
        return self.annotate(num_products=models.Count('product')).order_by('-num_products')


class ManufacturerQuerySet(models.QuerySet):
    def ordered_by_country(self):
        return self.order_by('country')

    def with_products_in_category(self, category_name):
        return self.filter(product__category__name=category_name).distinct()


class ProductQuerySet(models.QuerySet):
    def ordered_by_price(self):
        return self.order_by('price')

    def available_in_store(self, store_name):
        return self.filter(store__name=store_name)
