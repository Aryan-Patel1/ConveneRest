# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-14 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0016_auto_20170913_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Denied'), (1, 'Approved'), (2, 'Final State'), (3, 'Completed')], null=True),
        ),
        migrations.AlterField(
            model_name='workflowbatch',
            name='current_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkFlowSurveyRelation'),
        ),
        migrations.AlterField(
            model_name='workflowcomment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Denied'), (1, 'Approved'), (2, 'Final State'), (3, 'Completed')], null=True),
        ),
    ]