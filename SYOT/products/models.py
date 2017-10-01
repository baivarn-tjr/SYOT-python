from django.db import models
from django.contrib.postgres.fields import JSONField
import os

def get_product_image_path(instance, filename):
    return os.path.join('product_image', str(instance.id), filename)

class Catagory(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return self.name

class ReviewPro(models.Model):
    userId = models.PositiveIntegerField()
    productId = models.PositiveIntegerField()
    comment = models.TextField(blank = True)
    point = models.PositiveIntegerField()

    def __str__(self):
        return self.name
