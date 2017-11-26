from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from products.models import Product

from .models import Basket
from account.models import Applicant

def calMoney(userBasket,usercart,carts):
    money = 0
    for item in usercart:
        itemCart = Basket.objects.get(productID = item, userId = userBasket)
        money += (item.cost*itemCart.quantity)
    return money

def calShipping(userBasket,usercart,carts):
    ship = 5
    for item in usercart:
        itemCart = Basket.objects.get(productID = item, userId = userBasket)
        ship += (3*itemCart.quantity)
    ship -= 3
    return ship

def cart(request,user_id):
    userBasket = Applicant.objects.get(id=user_id)
    usercart = userBasket.myBasket.all()
    carts = Basket.objects.all()
    money = calMoney(userBasket,usercart,carts)
    ship = calShipping(userBasket,usercart,carts)
    context = {
        'user' : userBasket,
        'usercart' : usercart,
        'carts' : carts,
        'money' : money,
        'ship' : ship,
    }
    template = 'carts/basket.html'
    return render(request,template,context)

def checkout(request, user_id, totalmoney):
    # totalmoney = request.POST.get('totalmoney')
    # user_id = request.POST.get('user_id')
    context = {
        'totalmoney' : totalmoney,
        'user_id' : user_id,
    }
    template = 'payment.html'
    return render(request,template,context)

def delete(request, user_id, product_id):
    user = Applicant.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    item = get_object_or_404(Basket, userId=user, productID=product)
    item.delete()

    userBasket = Applicant.objects.get(id=user_id)
    usercart = userBasket.myBasket.all()
    carts = Basket.objects.all()
    money = calMoney(userBasket,usercart,carts)
    ship = calShipping(userBasket,usercart,carts)
    context = {
        'user' : userBasket,
        'usercart' : usercart,
        'carts' : carts,
        'money' : money,
        'ship' : ship,
    }
    template = 'carts/basket.html'
    return render(request,template,context)

def addminusQuantity(request, user_id , product_id):
    user = Applicant.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    item = get_object_or_404(Basket, userId=user, productID=product)

    if 'inc' in request.POST:
        item.quantity += 1
    else:
        item.quantity -= 1
    item.save()

    userBasket = Applicant.objects.get(id=user_id)
    usercart = userBasket.myBasket.all()
    carts = Basket.objects.all()
    money = calMoney(userBasket,usercart,carts)
    ship = calShipping(userBasket,usercart,carts)
    context = {
        'user' : userBasket,
        'usercart' : usercart,
        'carts' : carts,
        'money' : money,
        'ship' : ship,
    }
    template = 'carts/basket.html'
    return render(request,template,context)
