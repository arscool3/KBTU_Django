from django.http import JsonResponse
from django.shortcuts import render

def health(request):
    return JsonResponse({
        "message": "OK"
    })

def getCategories(request):
    categories = ["Еда", "Техника", "Книги", "Одежда"]
    return JsonResponse({
        "categories": categories
    })

def getCategoryById(request, id):
    categories = ["Еда", "Техника", "Книги", "Одежда"]
    try:
        category = categories[id - 1]
        return JsonResponse({
            "category": category
        })
    except:
        return JsonResponse({
            "error": "Такой категории тут нет"
        })



