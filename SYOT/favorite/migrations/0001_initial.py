# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('userId', models.IntegerField()),
                ('productID', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='favitem',
            name='fav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite.Favorite'),
        ),
        migrations.AddField(
            model_name='favitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
