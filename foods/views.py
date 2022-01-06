from django.shortcuts import render
from . import models

# Create your views here.

def index(req):
    foods = models.food.objects.all()[:1]
    return render(req, "foods/index.html",{
        "foods": foods
    })