# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-09-25 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0052_auto_20180921_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='samandmam',
            name='v_3',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='samandmam',
            name='v_4',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
