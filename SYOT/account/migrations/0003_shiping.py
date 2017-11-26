# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171126_1601'),
        ('account', '0002_auto_20171125_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='shiping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('productID', models.ManyToManyField(to='products.Product')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Applicant')),
            ],
        ),
    ]
