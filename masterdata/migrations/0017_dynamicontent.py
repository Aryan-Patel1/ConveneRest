# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0016_masterlookup_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamiContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.IntegerField(blank=True, choices=[(1, 'Master Locations')], null=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]