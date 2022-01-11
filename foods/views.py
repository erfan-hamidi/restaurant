from django.shortcuts import render
from . import models

# Create your views here.

def index(req):
    foods = models.food.objects.all()[:1]
    return render(req, "foods/index.html",{
        "foods": foods
    })

def detail(req, id_food):
    foods = models.food.objects.get(id=id_food)
    print(foods)
    return render(req, "foods/detail.html",{
        "food" : foods
    })