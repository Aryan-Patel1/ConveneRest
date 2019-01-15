# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-09-21 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0051_auto_20180919_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamAndMam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('height', models.CharField(max_length=5)),
                ('v_1', models.CharField(max_length=5)),
                ('v_2', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='validation',
            field=models.IntegerField(blank=True, choices=[(0, b'Digit'), (1, b'Number'), (2, b'Alphabet'), (3, b'Alpha Numeric'), (4, b'No Validation'), (6, b'Mobile Number'), (7, b'Landline'), (8, b'Date'), (9, b'Time'), (10, b'Only Alpha Numeric'), (11, b'QuestionBased Validation'), (12, b'Auto Calculate'), (13, b'Api Call')], null=True),
        ),
    ]