# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-11-06 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financedetail',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active'), (1, 'Migrated')], default=2),
        ),
        migrations.AlterField(
            model_name='issue',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active'), (1, 'Migrated')], default=2),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active'), (1, 'Migrated')], default=2),
        ),
        migrations.AlterField(
            model_name='meetinggroup',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active'), (1, 'Migrated')], default=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='active',
            field=models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active'), (1, 'Migrated')], default=2),
        ),
    ]