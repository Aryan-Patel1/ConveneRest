# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-12 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('facilities', '0013_auto_20170926_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeContentCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('financial_year', models.CharField(blank=True, max_length=100, null=True)),
                ('content_count', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codecontent_ctype', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
