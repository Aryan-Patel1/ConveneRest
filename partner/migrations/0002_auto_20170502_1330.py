# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-02 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0010_auto_20170502_1256'),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='community',
        ),
        migrations.AddField(
            model_name='project',
            name='community',
            field=models.ManyToManyField(blank=True, null=True, related_name='masterlookup_community', to='masterdata.MasterLookUp'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='prominent_issues',
        ),
        migrations.AddField(
            model_name='project',
            name='prominent_issues',
            field=models.ManyToManyField(blank=True, null=True, related_name='masterlookup_issue', to='masterdata.MasterLookUp'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='theme',
        ),
        migrations.AddField(
            model_name='project',
            name='theme',
            field=models.ManyToManyField(blank=True, null=True, related_name='masterlookup_theme', to='masterdata.MasterLookUp'),
        ),
    ]