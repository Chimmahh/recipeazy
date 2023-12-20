from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    yield_quantity = models.IntegerField()
    # yield_unit = 

class Ingredient(models.Model):
    UNIT_GRAM = 'g'
    UNIT_KILOGRAM = 'kg'
    UNIT_OUNCE_MASS = 'ozm'
    UNIT_POUND = 'lb'
    UNIT_LITER = 'l'
    UNIT_TEASPOON = 'tsp'
    UNIT_TABLESPOON = 'tbsp'
    UNIT_OUNCE_FLUID = 'oz'
    UNIT_CUP = 'c'
    UNIT_QUART = 'qt'
    UNIT_GALLON = 'gal'
    UNIT_EACH = 'ea'
    UNIT_PACK = 'pk'
    UNIT_CASE = 'cs'
    UNIT_CHOICES = [
        (UNIT_GRAM, 'gram'),
        (UNIT_KILOGRAM, 'kilogram'),
        (UNIT_OUNCE_MASS, 'ounce (mass)'),
        (UNIT_POUND, 'pound'), 
        (UNIT_LITER, 'liter'), 
        (UNIT_TEASPOON, 'teaspoon'), 
        (UNIT_TABLESPOON, 'tablespoon'), 
        (UNIT_OUNCE_FLUID, 'ounce (fluid)'), 
        (UNIT_CUP, 'cup'), 
        (UNIT_QUART, 'quart'), 
        (UNIT_GALLON, 'gallon'),
        (UNIT_EACH, 'each'),
        (UNIT_PACK, 'pack'),
        (UNIT_CASE, 'case')
    ]
    
    name = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(auto_now=True)
    unit = models.Choices(max_length=4, choices=UNIT_CHOICES, default=UNIT_EACH)

class RecipeBuildItem(models.Model):
    master_recipe = models.ManyToOneRel(Recipe, on_delete=models.CASCADE)
    # build_recipe = models.OneToOneField(Recipe,)
    # build_ingredient = models.CharField(Ingredient)