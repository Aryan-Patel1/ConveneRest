# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-07-25 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0024_partneruserinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partneruserinfo',
            old_name='contact_number',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='partneruserinfo',
            name='adhar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='partneruserinfo',
            name='department',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='partneruserinfo',
            name='designation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='partneruserinfo',
            name='pan',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='partneruserinfo',
            name='remarks',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]