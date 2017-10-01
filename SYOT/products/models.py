from django.db import models
import os

def get_product_image_path(instance, filename):
    return os.path.join('product_image', str(instance.id), filename)

class Catagory(models.Model):
    # CATAGORY_TYPE = (
    #     ('MV', 'Moive'),
    #     ('KD', 'Kids'),
    #     ('GL', 'Girls'),
    #     ('VC', 'Vehicles'),
    #     ('CT', 'Kids'),
    # )
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # COVER_TYPE = (
    #     ('PD', 'Paperback'),
    #     ('HC', 'Hardcover'),
    # )
    #
    # PAPER_TYPE = (
    #     ('NS', 'Newsprint'),
    #     ('CP', 'Coated Paper'),
    #     ('UP', 'Uncoated Paper'),
    #     ('BP', 'Bond Paper'),
    #     ('GR', 'Green Read Paper'),
    # )

    id = models.AutoField(primary_key=True)
    # idpro = models.DecimalField(max_digits = 13, decimal_places = 0, unique = True)
    name = models.CharField(max_length = 250)
    description = models.TextField(blank = True)
    # author = models.CharField(max_length = 250)
    catagory = models.ManyToManyField(Catagory)
    supplier = models.CharField(max_length = 250)
    cost = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    # isMonocrome = models.BooleanField(default = True)
    # paperType = models.CharField(max_length = 2, choices=PAPER_TYPE)
    # coverType = models.CharField(max_length = 2, choices=COVER_TYPE)
    # size_height = models.FloatField()
    # size_width = models.FloatField()
    # size_thickness = models.FloatField()
    # description = models.TextField(blank = True)
    pictureUrl = models.ImageField(upload_to = get_product_image_path, blank = True, null = True)
    count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name
