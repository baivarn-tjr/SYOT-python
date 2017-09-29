from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    context = {}
    template = 'carts/basket.html'
    return render(request,template,context)
