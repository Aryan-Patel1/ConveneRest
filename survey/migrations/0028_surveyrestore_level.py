# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-05 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0027_auto_20171005_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyrestore',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
