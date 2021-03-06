# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-04 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobra', '0003_auto_20161215_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_id', models.IntegerField()),
                ('channel', models.CharField(default='NONE', max_length=50)),
                ('count', models.IntegerField()),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(default='', max_length=50)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('day', models.DateField()),
            ],
        ),
    ]
