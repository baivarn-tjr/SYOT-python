from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# from products.models import Product

from .models import Basket, CartItem

def cart(request):
    context = {}
    template = 'carts/basket.html'
    return render(request,template,context)

# def
