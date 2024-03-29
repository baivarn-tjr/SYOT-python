# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171126_1846'),
        ('favorite', '0003_auto_20171126_1846'),
        ('account', '0003_remove_applicant_myfav'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='myFav',
            field=models.ManyToManyField(related_name='FavProduct', through='favorite.FavoriteItem', to='products.Product'),
        ),
    ]
