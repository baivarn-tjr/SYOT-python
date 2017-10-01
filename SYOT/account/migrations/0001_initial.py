# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('hashed_password', models.CharField(blank=True, max_length=130)),
            ],
        ),
    ]
