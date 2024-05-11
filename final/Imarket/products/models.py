from django.core.exceptions import ValidationError
from django.db import models


def validate_rating(value):
    if 0 <= value <= 5:
        return value
    else:
        raise ValidationError("This field accepts rating between 0 and 5")


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f'subcat: {self.name} -> from cat: {self.category.name}'

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active ?')
    description = models.TextField(null=True, verbose_name='Description')
    rating = models.FloatField(null=True, validators=[validate_rating], default=5.0)
    rate_cnt = models.IntegerField(null=True, default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ('-created_at', )

    def __str__(self):
        return f"id: {self.pk}, {self.name} ({self.subcategory.name})"


