# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 04:26
from __future__ import unicode_literals

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
                ('count', models.PositiveIntegerField(default=0)),
                ('catagory', models.ManyToManyField(to='products.Catagory')),
            ],
        ),
    ]
