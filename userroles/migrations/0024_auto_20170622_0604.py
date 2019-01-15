# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-22 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0009_projectuserdetail_holder_user'),
        ('userroles', '0023_auto_20170619_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroles',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Partner'),
        ),
        migrations.AddField(
            model_name='userroles',
            name='user_type',
            field=models.IntegerField(choices=[(1, b'Normal User'), (2, b'Partner')], default=1),
        ),
    ]