from django.shortcuts import render
from .models import Drinks
from django.http import HttpResponse
# Create your views here.

def drinks_detail_view(request):
    obj = Drinks.objects.get(id=2)
    context = {
        "name": obj.name,
        "description": obj.description,
        "price": obj.price
    }
    return render(request, "drinks/detail.html", context)
