# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-01-30 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0040_auto_20180119_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequence',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(0, b'Current Week'), (1, b'Current Month'), (2, b'Current Quarter'), (3, b'Current Half-Yearly'), (4, b'Yearly'), (5, b'Financial Year')], null=True),
        ),
    ]