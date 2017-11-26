# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171126_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pictureUrl1',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='pictureUrl2',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='pictureUrl3',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='pictureUrl4',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 9, 26, 16, 754881)),
        ),
    ]
