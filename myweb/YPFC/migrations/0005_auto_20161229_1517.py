# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-29 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YPFC', '0004_auto_20161227_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
