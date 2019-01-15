# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0017_bankaccount_fund_type'),
        ('survey', '0022_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyPartnerExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('expiry_age', models.PositiveIntegerField(default=0)),
                ('partner', models.ManyToManyField(to='partner.Partner')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]