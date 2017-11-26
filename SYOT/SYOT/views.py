from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def index(request):
    products = Product.objects.all().order_by('?')[:4]
    count = 0
    context = {
        'product' : products,
        'count' : count,
    }
    return render(request, 'homepage.html' , context)
