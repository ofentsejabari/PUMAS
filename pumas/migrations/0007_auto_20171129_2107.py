# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 05:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pumas', '0006_auto_20171129_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='created_by',
        ),
        migrations.AddField(
            model_name='document',
            name='created_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
