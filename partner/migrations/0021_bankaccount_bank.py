# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-17 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0019_auto_20171130_1114'),
        ('partner', '0020_partnerreportfile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_bank', to='masterdata.MasterLookUp'),
        ),
    ]
