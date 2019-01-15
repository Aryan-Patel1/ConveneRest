# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-08-29 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20170829_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveybeneficiarymap',
            name='content_type1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='surveybeneficiarymap',
            name='object_id1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
