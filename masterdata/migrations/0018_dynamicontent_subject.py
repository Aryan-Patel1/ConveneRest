# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0017_dynamicontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicontent',
            name='subject',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
