# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-24 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userroles', '0013_adtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roletypes',
            name='code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
