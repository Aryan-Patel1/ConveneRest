# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-30 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0009_auto_20170926_0614'),
        ('masterdata', '0015_boundary_ward_type'),
        ('survey', '0033_dashboardresponse_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beneficiary.BeneficiaryType')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
