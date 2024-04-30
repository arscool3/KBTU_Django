from django.db import models

class CoreModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class ShopManager(models.Manager):
    def get_query_set(self):
        return ShopQuerySet(self.model, using=self._db)

class SectionManager(models.Manager):
    def get_query_set(self):
        return SectionQuerySet(self.model, using=self._db)

class ProducerManager(models.Manager):
    def get_query_set(self):
        return ProducerQuerySet(self.model, using=self._db)

class GoodsManager(models.Manager):
    def get_query_set(self):
        return GoodsQuerySet(self.model, using=self._db)

    def available_in_shop(self, shop_name):
        return self.get_queryset().available_in_shop(shop_name)

class Shop(CoreModel):
    location = models.CharField(max_length=200)
    managers = ShopManager()

class Section(CoreModel):
    description = models.TextField()
    managers = SectionManager()

class Producer(CoreModel):
    country = models.CharField(max_length=100)
    managers = ProducerManager()

class Goods(CoreModel):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    stores = models.ManyToManyField(Shop)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    managers = GoodsManager()

class ShopQuerySet(models.QuerySet):
    def sort_by_location(self):
        return self.order_by('location')

    def with_goods(self):
        return self.filter(goods__isnull=False).distinct()

class SectionQuerySet(models.QuerySet):
    def sort_by_description(self):
        return self.order_by('description')

    def most_popular(self):
        return self.annotate(total_goods=models.Count('goods')).order_by('-total_goods')

class ProducerQuerySet(models.QuerySet):
    def sort_by_country(self):
        return self.order_by('country')

    def goods_in_section(self, section_name):
        return self.filter(goods__section__name=section_name).distinct()

class GoodsQuerySet(models.QuerySet):
    def sort_by_price(self):
        return self.order_by('price')

    def available_in_shop(self, shop_name):
        return self.filter(stores__name=shop_name)