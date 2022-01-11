from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id_food>/', views.detail, name="detail-food")
    
]