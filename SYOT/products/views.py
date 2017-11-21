from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Product, Catagory, ReviewProduct
from carts.models import Basket
from favorite.models import Account,Favorite
from account.models import Applicant
from django import forms
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


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
    count = 0
    pointPro = 0
    err = False
    data = request.POST
    rev = ReviewProduct.objects.all()
    product = Product.objects.get(id = product_id)
    quantityWarning = 20
    if request.method == 'POST':
        try:
            uid = request.session['user_id']
        except KeyError:
            err = "please login before comment!"
            context = {
                'err' : err,
                'reviews' : rev,
                'getProduct' : product,
                'quantityWarning' : quantityWarning,
            }
            return render(request, 'Product-page.html', context)

        try:
            reviews = ReviewProduct(
                proId = product_id,
                comment = data['review'],
                point = int(data['rating'])
            )
            reviews.set_by_id(uid)
            reviews.save()
        except KeyError:
            err = "Please rate product!"

    for i in rev:
        if(product_id == i.proId):
            count += 1
            pointPro += i.point

    if count != 0:
        product.point = pointPro/count
        product.save()

    context = {
        'err' : err,
        'reviews' : rev,
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
    try:
        # uid = force_text(urlsafe_base64_decode(user_id))
        user = Applicant.objects.get(pk=user_id)
    except(TypeError, ValueError, OverflowError, Applicant.DoesNotExist):
        user = None
    product = Product.objects.get(id=product_id)
    try:
        itemtocart = Basket.objects.get(userId=user, productID=product)
    except (KeyError, Basket.DoesNotExist):
        Basket.objects.create(userId=user, productID=product)

    product = Product.objects.get(id=product_id)
    quantityWarning = 20
    return HttpResponseRedirect(reverse('detail'))





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
