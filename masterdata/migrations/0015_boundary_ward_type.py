# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-08-14 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0014_auto_20170814_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='boundary',
            name='ward_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_ward', to='masterdata.MasterLookUp'),
        ),
    ]
