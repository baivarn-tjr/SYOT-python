from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Shipping(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.product_name
