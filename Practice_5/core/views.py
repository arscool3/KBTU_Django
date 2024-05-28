from django.shortcuts import render, redirect
from .models import Shop, Section, Producer, Goods

def shop_list(request):
    shops_with_goods = Shop.managers.all().with_goods()
    ordered_shops = Shop.managers.all().sort_by_location()

    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        Shop.managers.create(name=name, location=location)
        return redirect('shop_list')
    return render(request, 'shop_list.html', {
        'shops_with_goods': shops_with_goods,
        'ordered_shops': ordered_shops
    })

def section_list(request):
    popular_sections = Section.managers.all().most_popular()
    ordered_sections = Section.managers.all().sort_by_description()

    if request.method == 'POST':
        section_id = request.POST.get('section_id')
        new_description = request.POST.get('new_description')
        section = Section.managers.get(id=section_id)
        section.description = new_description
        section.save()
        return redirect('section_list')
    return render(request, 'section_list.html', {
        'popular_sections': popular_sections,
        'ordered_sections': ordered_sections
    })

def producer_list(request):
    producers_with_goods_in_section = Producer.managers.all().goods_in_section('Some Section')
    ordered_producers = Producer.managers.all().sort_by_country()

    if request.method == 'POST':
        producer_id = request.POST.get('producer_id')
        producer = Producer.managers.get(id=producer_id)
        producer.delete()
        return redirect('producer_list')
    return render(request, 'producer_list.html', {
        'producers_with_goods_in_section': producers_with_goods_in_section,
        'ordered_producers': ordered_producers
    })

def goods_list(request):
    goods_available_in_shop = Goods.managers.all().available_in_shop('Some Shop')
    ordered_goods = Goods.managers.all().sort_by_price()

    if request.method == 'POST':
        goods_id = request.POST.get('goods_id')
        new_price = request.POST.get('new_price')
        goods = Goods.managers.get(id=goods_id)
        goods.price = new_price
        goods.save()
        return redirect('goods_list')
    return render(request, 'goods_list.html', {
        'goods_available_in_shop': goods_available_in_shop,
        'ordered_goods': ordered_goods
    })