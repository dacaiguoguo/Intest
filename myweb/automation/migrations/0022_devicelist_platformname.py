# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-24 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0021_devicelist_in_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicelist',
            name='platformName',
            field=models.CharField(blank=True, default='Android', max_length=10),
        ),
    ]