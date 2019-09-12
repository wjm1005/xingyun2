# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-08-26 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoDepartment',
            fields=[
                ('dep_id', models.IntegerField(blank=True, null=True)),
                ('dep_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dep_level', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sto_department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoEmployee',
            fields=[
                ('emp_id', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('emp_idcard', models.CharField(blank=True, db_column='emp_idCard', max_length=18, null=True)),
                ('emp_sex', models.CharField(blank=True, max_length=8, null=True)),
                ('emp_nativeplace', models.CharField(blank=True, db_column='emp_nativePlace', max_length=255, null=True)),
                ('emp_education', models.CharField(blank=True, max_length=255, null=True)),
                ('emp_marriage', models.CharField(blank=True, max_length=8, null=True)),
                ('emp_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('emp_address', models.CharField(blank=True, max_length=255, null=True)),
                ('emp_departmentone', models.CharField(blank=True, db_column='emp_departmentOne', max_length=100, null=True)),
                ('emp_position', models.CharField(blank=True, max_length=50, null=True)),
                ('emp_entrydate', models.DateTimeField(blank=True, db_column='emp_entryDate', null=True)),
                ('emp_state', models.CharField(blank=True, max_length=8, null=True)),
                ('emp_level', models.CharField(blank=True, max_length=8, null=True)),
                ('emp_relation', models.CharField(blank=True, max_length=8, null=True)),
                ('emp_adddate', models.DateTimeField(blank=True, db_column='emp_addDate', null=True)),
                ('emp_modifydate', models.DateTimeField(blank=True, db_column='emp_modifyDate', null=True)),
            ],
            options={
                'db_table': 'sto_employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StoWtOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.CharField(blank=True, db_column='billNo', max_length=30, null=True)),
                ('scantype', models.CharField(blank=True, db_column='scanType', max_length=50, null=True)),
                ('scandate', models.DateTimeField(blank=True, db_column='scanDate', null=True)),
                ('inputdept', models.CharField(blank=True, db_column='inputDept', max_length=50, null=True)),
                ('upornextstation', models.CharField(blank=True, db_column='upOrNextStation', max_length=50, null=True)),
                ('inputdate', models.DateTimeField(blank=True, db_column='inputDate', null=True)),
                ('operdate', models.DateTimeField(blank=True, db_column='operDate', null=True)),
                ('sendsite', models.CharField(blank=True, db_column='sendSite', max_length=50, null=True)),
                ('piece', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('goodstype', models.CharField(blank=True, db_column='goodsType', max_length=255, null=True)),
                ('belongno', models.CharField(blank=True, db_column='belongNo', max_length=50, null=True)),
                ('dispatchreciper', models.CharField(blank=True, db_column='dispatchReciper', max_length=255, null=True)),
                ('bagunid', models.CharField(blank=True, db_column='baGunId', max_length=50, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sto_wt_op',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_column='user_id', max_length=8)),
                ('user_name', models.CharField(db_column='user_name', max_length=16)),
                ('user_password', models.CharField(db_column='user_password', max_length=24)),
                ('user_power', models.IntegerField()),
            ],
            options={
                'db_table': 'xy_users',
                'managed': False,
            },
        ),
    ]