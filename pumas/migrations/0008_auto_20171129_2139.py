# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumas', '0007_auto_20171129_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created_by',
        ),
        migrations.AddField(
            model_name='document',
            name='created_by',
            field=models.TextField(default='', max_length=50),
        ),
    ]
