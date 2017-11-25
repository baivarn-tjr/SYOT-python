from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from products.models import Product
from django.forms.models import model_to_dict

from .models import Favorite
from account.models import Applicant

from rest_framework import serializers

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

def favorite(request,user_id):
    userr = Applicant.objects.get(id=user_id)
    userFav = userr.myFav.all()
    # userFav_dict = model_to_dict(userFav)
    # userr_json = json.dumps(userr, cls=DjangoJSONEncoder)
    # print(userFav_dict)
    # userfav_json = json.dumps(userFav_dict)
    # allFav = Favorite.objects.all()
    context = {
        'user' : userr,
        'userfav' : userFav,
        # 'allFav' : allFav,
    }
    template = 'favorite/favorite.html'
    return render(request,template,context)

def deletefav(request):
    if request.method == 'POST':
        response_data = { }
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')
        user = Applicant.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        item = get_object_or_404(Favorite, userId=user, productID=product)
        item.delete()
        userr = Applicant.objects.get(id=user_id)
        userFav = userr.myFav.all()
        # allFav = Favorite.objects.all()
        # context = {
        #     'user' : userr,
        #     'userfav' : userFav,
        #     # 'allFav' : allFav,
        # }
        # template = 'favorite/favorite.html'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")
