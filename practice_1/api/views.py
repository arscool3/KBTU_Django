from django.http import JsonResponse
from django.shortcuts import render

def health(request):
    return JsonResponse({
        "message": "OK"
    })

def getCategories(request):
    categories = ["Продукты", "Техника", "Одежда"]
    return JsonResponse({
        "categories": categories
    })

def getCategoryById(request, id):
    categories = ["Продукты", "Техника", "Одежда"]
    try:
        category = categories[id - 1]
        return JsonResponse({
            "category": category
        })
    except:
        return JsonResponse({
            "error": "Категории не существует"
        })



