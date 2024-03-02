from django.shortcuts import render, redirect
from .models import Store, Category, Manufacturer, Product


def store_list(request):
    stores_with_products = Store.objects.all().has_products()
    ordered_stores = Store.objects.all().ordered_by_location()

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        Store.objects.create(name=name, location=location)
        return redirect('store_list')
    return render(request, 'store_list.html',
                  {'stores_with_products': stores_with_products, 'ordered_stores': ordered_stores})


def category_list(request):
    popular_categories = Category.objects.all().popular()
    ordered_categories = Category.objects.all().ordered_by_description()

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        new_description = request.POST.get('new_description')
        category = Category.objects.get(id=category_id)
        category.description = new_description
        category.save()
        return redirect('category_list')
    return render(request, 'category_list.html',
                  {'popular_categories': popular_categories, 'ordered_categories': ordered_categories})


def manufacturer_list(request):
    manufacturers_with_products = Manufacturer.objects.all().with_products_in_category('Some Category')
    ordered_manufacturers = Manufacturer.objects.all().ordered_by_country()

    if request.method == 'POST':
        manufacturer_id = request.POST.get('manufacturer_id')
        manufacturer = Manufacturer.objects.get(id=manufacturer_id)
        manufacturer.delete()
        return redirect(
            'manufacturer_list')
    return render(request, 'manufacturer_list.html', {'manufacturers_with_products': manufacturers_with_products,
                                                      'ordered_manufacturers': ordered_manufacturers})


def product_list(request):
    products_available_in_store = Product.objects.all().available_in_store('Some Store')
    ordered_products = Product.objects.all().ordered_by_price()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_price = request.POST.get('new_price')
        product = Product.objects.get(id=product_id)
        product.price = new_price
        product.save()
        return redirect('product_list')
    return render(request, 'product_list.html',
                  {'products_available_in_store': products_available_in_store, 'ordered_products': ordered_products})
