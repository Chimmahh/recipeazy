from typing import Any
from django.db import models
from static import units
from datetime import datetime, timezone

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    yield_quantity = models.IntegerField()  

    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

    # price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super(Recipe, self).save(*args, **kwargs)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    unit = models.CharField(max_length=4, choices=units.UNIT_CHOICES, default=units.UNIT_EACH)

    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super(Recipe, self).save(*args, **kwargs)
class RecipeBuildItem(models.Model):
    master_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    build_recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, null=True, related_name ='+')
    build_ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, null=True, related_name ='+')
    quantity = models.FloatField()
    unit = models.CharField(max_length=4, choices=units.UNIT_CHOICES, default=units.UNIT_EACH)