# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171121_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='point',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
