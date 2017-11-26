# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 11:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='ProductID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('supplier', models.CharField(max_length=250)),
                ('cost', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('length', models.FloatField()),
                ('pictureUrl', models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path)),
                ('pictureUrl1', models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path)),
                ('pictureUrl2', models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path)),
                ('pictureUrl3', models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path)),
                ('pictureUrl4', models.ImageField(blank=True, null=True, upload_to=products.models.get_product_image_path)),
                ('count', models.PositiveIntegerField(default=0)),
                ('point', models.PositiveIntegerField(default=0, null=True)),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2017, 12, 26, 18, 30, 39, 364424))),
                ('catagory', models.ManyToManyField(to='products.Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proId', models.PositiveIntegerField(default=None, null=True)),
                ('userId', models.PositiveIntegerField(default=None, null=True)),
                ('userName', models.CharField(max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=250, null=True)),
                ('point', models.PositiveIntegerField(default=None, null=True)),
            ],
        ),
    ]
