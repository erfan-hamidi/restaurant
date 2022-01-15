from django.shortcuts import render
from .forms import ReservationForm

# Create your views here.

def index(req):
    #foods = models.food.objects.all()[:1]
    reveform = ReservationForm()
    if req.method == "POST":
        reveform = ReservationForm(req.POST)
        if reveform.is_valid():
            reveform.save()
    else:
        reveform = ReservationForm()


    return render(req, "reservation/reservation.html")