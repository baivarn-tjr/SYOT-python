from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from products.models import Product

from .models import Favorite
from account.models import Applicant

def favorite(request,user_id):
    userr = Applicant.objects.get(id=user_id)
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
    user = Applicant.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    item = get_object_or_404(Favorite, userId=user, productID=product)
    item.delete()

    userr = Applicant.objects.get(id=user_id)
    userFav = userr.myFav.all()
    # allFav = Favorite.objects.all()
    context = {
        'user' : userr,
        'userfav' : userFav,
        # 'allFav' : allFav,
    }
    template = 'favorite/favorite.html'
    return render(request,template,context)
