# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-03 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0002_auto_20170502_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
