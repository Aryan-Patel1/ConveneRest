# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-06-28 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0021_bankaccount_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='remarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]