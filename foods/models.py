from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class food(models.Model):
    name = CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    
