from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.

class Category(OrderedModel):
    category = models.CharField(max_length=100)
    active = active = models.BooleanField(default=True)

    def __str__(self):
        return self.category

class MenuItem(OrderedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title