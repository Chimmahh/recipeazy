from django.urls import path
from . import views

urlpatterns = [
    path('ingredient_list/', views.ingredient_list)
]