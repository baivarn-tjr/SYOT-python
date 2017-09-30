import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# from products.models import Product

class FavItem(models.Model):
    cart = models.ForeignKey('Favorite')
    # product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        # try:
        return str(self.cart.id)
        # except:
            # return self.product.title

class Favorite(models.Model):
    time = models.DateTimeField(auto_now_add=True, auto_now=False)
    userId = models.IntegerField(null=False)
    productID = models.IntegerField()
    def __str__(self):
        return str(self.id)
