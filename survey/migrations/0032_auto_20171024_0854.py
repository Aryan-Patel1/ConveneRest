# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-24 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0031_auto_20171022_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequence',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(0, b'Overall'), (1, b'Current Week'), (2, b'Current Month'), (3, b'Current Quarter'), (4, b'Current Half-Yearly'), (5, b'Yearly'), (6, b'Fiscal Year')], null=True),
        ),
    ]