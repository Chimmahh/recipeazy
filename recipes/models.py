from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    yield_quantity = models.IntegerField()
    # yield_unit = 

class ingredient(models.Model):
    name = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
