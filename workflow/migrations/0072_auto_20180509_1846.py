# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-05-09 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0071_auto_20180509_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflowbatch',
            name='current_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkFlowSurveyRelation'),
        ),
    ]