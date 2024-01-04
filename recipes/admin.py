from django.contrib import admin
from . import models
from static.units import *

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    ordering = ['name']
@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'unit_group']
    list_editable = ['unit']
    ordering = ['name']

    @admin.display(ordering='unit')
    def unit_group(self, ingredient):
        weight_list = [UNIT_GRAM, UNIT_KILOGRAM, UNIT_OUNCE_MASS, UNIT_POUND]
        fluid_list = [UNIT_LITER, UNIT_TEASPOON, UNIT_TABLESPOON, UNIT_OUNCE_FLUID, UNIT_CUP, UNIT_QUART, UNIT_GALLON]
        if ingredient.unit in weight_list:
            return 'weight'
        elif ingredient.unit in fluid_list:
            return 'fluid'
        return 'other'



# UNIT_GRAM = 'g'
# UNIT_KILOGRAM = 'kg'
# UNIT_OUNCE_MASS = 'ozm'
# UNIT_POUND = 'lb'
# UNIT_LITER = 'l'
# UNIT_TEASPOON = 'tsp'
# UNIT_TABLESPOON = 'tbsp'
# UNIT_OUNCE_FLUID = 'oz'
# UNIT_CUP = 'c'
# UNIT_QUART = 'qt'
# UNIT_GALLON = 'gal'
# UNIT_EACH = 'ea'
# UNIT_PACK = 'pk'
# UNIT_CASE = 'cs'
# UNIT_CHOICES = (
#     (UNIT_GRAM, 'gram'),
#     (UNIT_KILOGRAM, 'kilogram'),
#     (UNIT_OUNCE_MASS, 'ounce (mass)'),
#     (UNIT_POUND, 'pound'), 
#     (UNIT_LITER, 'liter'), 
#     (UNIT_TEASPOON, 'teaspoon'), 
#     (UNIT_TABLESPOON, 'tablespoon'), 
#     (UNIT_OUNCE_FLUID, 'ounce (fluid)'), 
#     (UNIT_CUP, 'cup'), 
#     (UNIT_QUART, 'quart'), 
#     (UNIT_GALLON, 'gallon'),
#     (UNIT_EACH, 'each'),
#     (UNIT_PACK, 'pack'),
#     (UNIT_CASE, 'case')
# )