# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-15 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userroles', '0002_auto_20170314_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userroles',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userroles',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userroles',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userroles',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roletypes',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True, verbose_name=b'SEO friendly url, use only aplhabets and hyphen'),
        ),
    ]