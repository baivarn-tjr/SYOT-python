from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from products.models import Product

from .models import Favorite,Account

def favorite(request):
    userr = Account.objects.get(id=1)
    userFav = userr.myFav.all()
    # allFav = Favorite.objects.all()
    context = {
        'user' : userr,
        'userfav' : userFav,
        # 'allFav' : allFav,
    }
    template = 'favorite/favorite.html'
    return render(request,template,context)

def deletefav(request, user_id, product_id):
    user = Account.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    item = get_object_or_404(Favorite, userId=user, productID=product)
    item.delete()

    userr = Account.objects.get(id=1)
    userFav = userr.myFav.all()
    # allFav = Favorite.objects.all()
    context = {
        'user' : userr,
        'userfav' : userFav,
        # 'allFav' : allFav,
    }
    template = 'favorite/favorite.html'
    return render(request,template,context)
