# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-10 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0007_facility_btype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='btype',
            field=models.CharField(blank=True, choices=[('Household', 'Household'), ('Mother', 'Mother'), ('Child', 'Child')], max_length=100, null=True),
        ),
    ]
