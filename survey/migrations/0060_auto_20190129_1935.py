# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-01-29 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0059_auto_20190107_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionautofill',
            name='question_sequence',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='questionvalidation',
            name='validation_condition',
            field=models.CharField(blank=True, choices=[(b'>', b'Greather Than'), (b'<', b'Less Than'), (b'>=', b'Greather Than Equal'), (b'<=', b'Less Than Equal'), (b'==', b'Equals'), (b'!=', b'Not Equal'), (b'+', b'Addition'), (b'-', b'Subtraction'), (b'*', b'Multiplication'), (b'/', b'Division'), (b'past', b'Past Date'), (b'current', b'Current Date'), (b'future', b'Future Date'), (b'any date', b'Any Date')], max_length=255, null=True),
        ),
    ]