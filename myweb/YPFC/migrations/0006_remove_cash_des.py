# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-29 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YPFC', '0005_auto_20161229_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cash',
            name='des',
        ),
    ]
