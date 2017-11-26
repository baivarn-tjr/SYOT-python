import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
from products.models import Product
from account.models import Applicant
# class CartItem(models.Model):
#     cart = models.ForeignKey('Basket')
#     product = models.ForeignKey(Product,null=False,default=0)
#     quantity = models.IntegerField(default=1)
#     def __str__(self):
#         try:
#             return str(self.cart.id)
#         except:
#             return self.product.title

#temp database
# class User(models.Model):
#     username = models.CharField(max_length=13)
#     myBasket = models.ManyToManyField(Product,through='Basket')
#     def __str__(self):
#         return str(self.username)

class Basket(models.Model):
    time = models.DateTimeField(auto_now_add=True, auto_now=False)
    userId = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, db_column='ProductID')
    quantity = models.IntegerField( null=False,default=1)
    def __str__(self):
        return str(self.id)

class CompanyMoney(models.Model):
    money = models.FloatField(null=False)
    def __str__(self):
        return str(self.money)
