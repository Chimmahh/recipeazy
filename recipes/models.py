from django.db import models
from ..static import units

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    yield_quantity = models.IntegerField()
    # yield_unit = 

class Ingredient(models.Model):
    name = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
    unit = models.Choices(max_length=4, choices=units.UNIT_CHOICES, default=units.UNIT_EACH)

class RecipeBuildItem(models.Model):
    master_recipe = models.ManyToManyRel(Recipe, on_delete=models.CASCADE)
    build_recipe = models.ManyToManyRel(Recipe, on_delete=models.PROTECT, null=True)
    build_ingredient = models.ManyToManyRel(Ingredient, on_delete=models.PROTECT, null=True)
    build_quantity = models.FloatField()