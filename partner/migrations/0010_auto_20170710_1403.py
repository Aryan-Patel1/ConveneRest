# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-10 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('masterdata', '0013_boundary_region'),
        ('partner', '0009_projectuserdetail_holder_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('year', models.CharField(blank=True, max_length=200, null=True)),
                ('line_item', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('theme_budget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_budget_theme', to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConfigureThematic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('types_of_funding', models.IntegerField(blank=True, choices=[(0, 'Entire Project'), (1, 'Specific Year'), (2, 'Specific Custom')], null=True)),
                ('start_year', models.DateField(blank=True, null=True)),
                ('end_year', models.DateField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('donar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Donar')),
                ('probability_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_probability_status', to='masterdata.MasterLookUp')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_funding_status', to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='configurethematic',
            name='funding',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Funding'),
        ),
        migrations.AddField(
            model_name='configurethematic',
            name='funding_theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_funding_theme', to='masterdata.MasterLookUp'),
        ),
        migrations.AddField(
            model_name='configurethematic',
            name='thematic',
            field=models.ManyToManyField(blank=True, null=True, to='partner.BudgetConfig'),
        ),
    ]