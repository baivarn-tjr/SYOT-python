from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Catagory

def product(request):
    context = locals()
    template = 'product.html'
    return render(request, template , context)

# def product(request):
#     return HttpResponse("<h1></>")
def catagory(request):
    # catagory = Catagory.objects.get(id = int(catagory_id))
    products = Product.objects.all
    context = {
        # 'catagory' : catagory,
        'products' : products,
    }
    return render(request, 'product.html', context)
