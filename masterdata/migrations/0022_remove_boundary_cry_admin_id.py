# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-10-26 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0021_auto_20180830_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boundary',
            name='cry_admin_id',
        ),
    ]