# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumas', '0010_auto_20171130_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.CharField(default='--', max_length=50),
        ),
    ]