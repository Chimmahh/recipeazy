from django.shortcuts import render
from django.http import HttpResponse

def ingredient_list(request):
    return render(request, 'ingredients.html', { 'name': 'Tim' })