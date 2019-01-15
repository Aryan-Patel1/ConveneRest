# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-04 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('masterdata', '0010_auto_20170502_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(blank=True, choices=[(1, 'Primary'), (2, 'Secondary'), (3, 'Others')], null=True)),
                ('contact_no', models.CharField(blank=True, max_length=600, null=True, verbose_name='Contact Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('landline', models.CharField(blank=True, max_length=20, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
