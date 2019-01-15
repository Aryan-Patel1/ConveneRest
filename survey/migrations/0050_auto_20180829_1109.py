# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-08-29 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0049_auto_20180803_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_auto_fill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_auto_fill_question', to='survey.Question'),
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_auto_fill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_fill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fill_survey', to='survey.Survey'),
        ),
    ]