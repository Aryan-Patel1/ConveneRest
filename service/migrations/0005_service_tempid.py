# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-28 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20170926_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='tempid',
            field=models.IntegerField(default=0),
        ),
    ]
