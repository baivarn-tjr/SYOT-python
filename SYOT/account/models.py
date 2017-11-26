import datetime

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password as check_hashed_password
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# from products.models import Product
# from carts.models import Basket
# from products.models import Product

class Applicant(models.Model):
    ACTIVE_TYPE = (
        ('AC', 'Active'),
        ('CL', 'Closed'),
        ('WT', 'Waiting'),
    )
    RESET_TYPE = (
        ('RS', 'Reset'),
        ('CL', 'Closed'),
    )
    username = models.CharField(default=None,max_length=50,unique=True)
    email = models.EmailField(default=None, max_length=128,unique=True)
    firstname = models.CharField(default=None, max_length=128)
    lastname = models.CharField(default=None, max_length=128)
    hashed_password = models.CharField(default=None,max_length=128)
    mobile = models.CharField(default=None,max_length=10)
    address = models.CharField(max_length=512, default=None)
    city = models.CharField(max_length=128, default=None)
    state = models.CharField(max_length=128, default=None)
    zipcode = models.CharField(max_length=5, default=None)
    is_activated = models.CharField(
        max_length=2,
        choices=ACTIVE_TYPE,
        default='WT'
    )
    reset_password = models.CharField(
        max_length=2,
        choices=RESET_TYPE,
        default='CL'
    )
    myBasket = models.ManyToManyField('products.Product',through='carts.Basket',related_name="BasketProduct")
    myFav = models.ManyToManyField('products.Product', through='favorite.Favorite', related_name="FavProduct")
    myShipping = models.ManyToManyField('products.Product', through='Shipping', related_name="ShippingProduct")
    # def __str__(self):
    #     return "%s %s (%s)" % (    self.username,
    #                                 self.tel,
    #                                 self.email)

    @staticmethod
    def find_by_username(username):
        try:
            applicant = Applicant.objects.get(username=username)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def find_by_email(email):
        try:
            applicant = Applicant.objects.get(email=email)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def set_password(self, password):
        self.hashed_password = make_password(password)

    def check_password(self, password):
        return check_hashed_password(password, self.hashed_password)

class Shipping(models.Model):
    time = models.DateTimeField(auto_now_add=True, auto_now=False)
    userId = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    productID = models.ForeignKey('products.Product', db_column='ProductID', null=True)
    status = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.id)
