# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-27 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userroles', '0007_auto_20170322_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroles',
            name='organization_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userroles.OrganizationUnit'),
        ),
    ]