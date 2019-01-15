# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-09 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_project_boundary'),
        ('beneficiary', '0002_auto_20170424_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beneficiary_partner', to='partner.Partner'),
        ),
    ]