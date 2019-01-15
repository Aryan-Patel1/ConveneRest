# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-03 08:50
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_listing', '0004_dynamicfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicfilter',
            name='filtering_query',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
