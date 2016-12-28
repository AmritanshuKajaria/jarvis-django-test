# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccessMasterGridView', '0002_auto_20161226_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessMaster',
            fields=[
                ('access_id', models.AutoField(primary_key=True, serialize=False)),
                ('access_name', models.CharField(blank=True, max_length=45, null=True)),
                ('alias_name', models.CharField(blank=True, max_length=45, null=True)),
                ('access_password', models.CharField(blank=True, max_length=100, null=True)),
                ('access_email', models.CharField(blank=True, max_length=100, null=True)),
                ('usa_phone', models.CharField(blank=True, max_length=45, null=True)),
                ('access_permission', models.CharField(blank=True, max_length=1, null=True)),
                ('department_id', models.IntegerField(blank=True, null=True)),
                ('sub_department_id', models.IntegerField(blank=True, null=True)),
                ('designation_id', models.IntegerField(blank=True, null=True)),
                ('suspension_count', models.IntegerField(blank=True, null=True)),
                ('manager_id', models.IntegerField(blank=True, null=True)),
                ('holding_capacity', models.IntegerField(blank=True, null=True)),
                ('holding_adjustment', models.IntegerField(blank=True, null=True)),
                ('pwd_modified_on', models.DateTimeField(blank=True, null=True)),
                ('pwd_modified_by', models.IntegerField(blank=True, null=True)),
                ('is_internal', models.CharField(blank=True, max_length=1, null=True)),
                ('access_state', models.CharField(blank=True, max_length=1, null=True)),
                ('calling_enabled', models.IntegerField(blank=True, null=True)),
                ('rtc_access', models.CharField(max_length=1)),
                ('fs_newsystem_access', models.IntegerField(blank=True, null=True)),
                ('fin_newsystem_access', models.IntegerField(blank=True, null=True)),
                ('fin_role_id', models.IntegerField(blank=True, null=True)),
                ('is_home', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'access_master',
            },
        ),
        migrations.DeleteModel(
            name='access_master',
        ),
    ]