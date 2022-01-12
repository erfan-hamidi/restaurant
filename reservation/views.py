from django.shortcuts import render

# Create your views here.

def index(req):
    #foods = models.food.objects.all()[:1]
    return render(req, "reservation/reservation.html")