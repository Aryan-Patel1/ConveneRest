# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-13 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0012_auto_20170509_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundary',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_boundary_region', to='masterdata.MasterLookUp'),
        ),
    ]
