from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from products.models import Product

from .models import Basket,User

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
        ship += 3
    ship -= 3
    return ship

def cart(request):
    userBasket = User.objects.get(username="varn")
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



# def
