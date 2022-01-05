from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class category(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

class food(models.Model):
    name = CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="media", null= True)
    category = ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    
