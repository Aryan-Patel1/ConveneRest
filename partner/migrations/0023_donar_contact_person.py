# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-04 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0022_bankaccount_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='donar',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]