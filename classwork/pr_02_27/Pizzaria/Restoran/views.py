from django.shortcuts import render
from .models import *
# Query sets

All_food = Food.objects.all()
All_cat = Category.objects.all()

#Queryset methods

#Return Category name and list of food in Category
def Food_from_cat(cat_id):
    return [Category.objects.get(pk = cat_id), Food.objects.filter(cat=cat_id)]

#Return list of Purchases by Customer Id
def Client_PurchaseList(client_id):
    return Purchase.objects.filter(pk=client_id)

#Return list of PurchasedFood by Purchase id
def Purchased_Food(P_id):
    return PurchasedFood.objects.filter(pk=P_id)

#Return Food by Id
def GetFood(F_id):
    return Food.objects.get(pk=F_id)

#Return Category by Id
def GetCategory(C_id):
    return Category.objects.get(pk=C_id)

#Return Food more expensive than Cost
def GetMoreExpensive(Cost):
    return Food.objects.filter(cost_gte=Cost)





