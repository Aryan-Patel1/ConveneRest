# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-09-28 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0010_beneficiary_tempid'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='cry_admin_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]