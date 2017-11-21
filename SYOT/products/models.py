from django.db import models
from account.models import Applicant
import os

def get_product_image_path(instance, filename):
    return os.path.join('product_image', str(instance.id), filename)

class Catagory(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key=True,db_column='ProductID')
    name = models.CharField(max_length = 250)
    description = models.TextField(blank = True)
    catagory = models.ManyToManyField(Catagory)
    supplier = models.CharField(max_length = 250)
    cost = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    pictureUrl = models.ImageField(upload_to = get_product_image_path, blank = True, null = True)
    count = models.PositiveIntegerField(default = 0)
    point = models.PositiveIntegerField(default=None, null = True)

    def __str__(self):
        return self.name

class ReviewProduct(models.Model):
    proId = models.PositiveIntegerField(default=None, null = True)
    userId = models.PositiveIntegerField(default=None, null = True)
    userName = models.CharField(max_length=100, null = True)
    comment = models.CharField(blank = True,max_length=250, null = True)
    point = models.PositiveIntegerField(default=None, null = True)


    def set_by_id(self,userId):
        applicant = Applicant.objects.get(id=userId)
        self.userId = applicant.id
        self.userName = applicant.username
