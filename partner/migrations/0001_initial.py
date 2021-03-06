# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-05-02 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterdata', '0010_auto_20170502_1256'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(blank=True, choices=[(1, 'Primary'), (2, 'Secondary'), (3, 'Others')], null=True)),
                ('account_type', models.IntegerField(blank=True, choices=[(1, 'CURRENT DEPOSITS / ACCOUNTS'), (2, 'SAVING BANK / Saving Fund  DEPOSITS / ACCOUNTS'), (3, 'RECURRING DEPOSITS / ACCOUNTS'), (4, 'FIXED DEPOSITS / ACCOUNTS OR TERM DEPOSITS')], null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=15, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('partner_id', models.CharField(blank=True, max_length=100, null=True)),
                ('support_since', models.DateField(blank=True, null=True)),
                ('admin_id', models.CharField(blank=True, max_length=100, null=True)),
                ('nature_of_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_nature', to='masterdata.MasterLookUp')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_region', to='masterdata.MasterLookUp')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masterdata.Boundary')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_status', to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('other_legal_registration', models.BooleanField(default=False)),
                ('legal_name', models.CharField(blank=True, max_length=200, null=True)),
                ('legal_number', models.CharField(blank=True, max_length=200, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_community', to='masterdata.MasterLookUp')),
                ('disbursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_disbursal', to='masterdata.MasterLookUp')),
                ('fla_grm_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_fla_grm_team', to='masterdata.MasterLookUp')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Partner')),
                ('pre_funding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_funding', to='masterdata.MasterLookUp')),
                ('prominent_issues', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_issue', to='masterdata.MasterLookUp')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masterlookup_theme', to='masterdata.MasterLookUp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectuserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_type', models.IntegerField(blank=True, choices=[(1, 'CEO/HOLDER'), (2, 'CO-ORDINATOR')], null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partner.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('act', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_registered', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'OPEN'), (2, 'CLOSED')], null=True)),
                ('priority', models.IntegerField(blank=True, choices=[(1, 'Primary'), (2, 'Secondary'), (3, 'Others')], null=True)),
                ('pan', models.CharField(blank=True, max_length=100, null=True)),
                ('tan', models.CharField(blank=True, max_length=100, null=True)),
                ('tin', models.CharField(blank=True, max_length=100, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='static/%Y/%m/%d')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
