from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Catagory
from carts.models import User,Basket
from favorite.models import Account,Favorite

import django.contrib.postgres.search

def index(request):
    context = {
        }
    template = 'index.html'
    return render(request, template , context)

def catalog(request):
    products = Product.objects.all()
    context = {
            'products' : products,
        }
    template = 'product.html'
    return render(request, template , context)

#
def detail(request, product_id):
    product = Product.objects.get(id = product_id)
    quantityWarning = 20
    context = {
        'getProduct' : product,
        'quantityWarning' : quantityWarning,
    }
    return render(request, 'Product-page.html', context)


def search(request):
    data = request.POST
    name = data['search_name']
    count = 0

    toys = Product.objects.filter(name__contains = name)

    for i in toys:
        count = count + 1

    context = {
        'toyPro' : toys,
        'Name' : name,
        'Count' : count,
    }
    return render(request, 'product_search.html' ,context)

def addtocart(request, user_id , product_id):
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    try:
        itemtocart = Basket.objects.get(userId=user, productID=product)
    except (KeyError, Basket.DoesNotExist):
        Basket.objects.create(userId=user, productID=product)

    product = Product.objects.get(id = product_id)
    quantityWarning = 20
    context = {
        'getProduct' : product,
        'quantityWarning' : quantityWarning,
    }
    return render(request, 'Product-page.html', context)




def addtofav(request, user_id , product_id):
    user = Account.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    try:
        itemtocart = Favorite.objects.get(userId=user, productID=product)
    except (KeyError, Favorite.DoesNotExist):
        Favorite.objects.create(userId=user, productID=product)

    product = Product.objects.get(id = product_id)
    quantityWarning = 20
    context = {
        'getProduct' : product,
        'quantityWarning' : quantityWarning,
    }
    return render(request, 'Product-page.html', context)

# def product(request):
#     context = locals()
#     template = 'start.html'
#     return render(request, template , context)

# def product(request):
#     return HttpResponse("<h1></>")
# def catagory(request):
#     # catagory = Catagory.objects.get(id = int(catagory_id))
#     products = Product.objects.all
#     context = {
#         # 'catagory' : catagory,
#         'products' : products,
#     }
#     return render(request, 'product.html', context)
