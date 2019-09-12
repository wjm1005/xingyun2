# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class StoDepartment(models.Model):
    dep_id = models.IntegerField(blank=True, null=True)
    dep_name = models.CharField(primary_key=True, max_length=100)
    dep_level = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sto_department'


class StoEmployee(models.Model):
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    emp_name = models.CharField(primary_key=True, max_length=50)
    emp_idcard = models.CharField(db_column='emp_idCard', max_length=18, blank=True, null=True)  # Field name made lowercase.
    emp_sex = models.CharField(max_length=8, blank=True, null=True)
    emp_nativeplace = models.CharField(db_column='emp_nativePlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emp_education = models.CharField(max_length=255, blank=True, null=True)
    emp_marriage = models.CharField(max_length=8, blank=True, null=True)
    emp_phone = models.CharField(max_length=20, blank=True, null=True)
    emp_address = models.CharField(max_length=255, blank=True, null=True)
    emp_departmentone = models.CharField(db_column='emp_departmentOne', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_department = models.ForeignKey(StoDepartment, models.DO_NOTHING, db_column='emp_department', blank=True, null=True)
    emp_position = models.CharField(max_length=50, blank=True, null=True)
    emp_entrydate = models.DateTimeField(db_column='emp_entryDate', blank=True, null=True)  # Field name made lowercase.
    emp_state = models.CharField(max_length=8, blank=True, null=True)
    emp_level = models.CharField(max_length=8, blank=True, null=True)
    emp_relation = models.CharField(max_length=8, blank=True, null=True)
    emp_adddate = models.DateTimeField(db_column='emp_addDate', blank=True, null=True)  # Field name made lowercase.
    emp_modifydate = models.DateTimeField(db_column='emp_modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sto_employee'


class StoWtOp(models.Model):
    billno = models.CharField(db_column='billNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    scantype = models.CharField(db_column='scanType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scandate = models.DateTimeField(db_column='scanDate', blank=True, null=True)  # Field name made lowercase.
    inputdept = models.CharField(db_column='inputDept', max_length=50, blank=True, null=True)  # Field name made lowercase.
    upornextstation = models.CharField(db_column='upOrNextStation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scanemp = models.ForeignKey(StoEmployee, models.DO_NOTHING, db_column='scanEmp', blank=True, null=True)  # Field name made lowercase.
    inputdate = models.DateTimeField(db_column='inputDate', blank=True, null=True)  # Field name made lowercase.
    operdate = models.DateTimeField(db_column='operDate', blank=True, null=True)  # Field name made lowercase.
    sendsite = models.CharField(db_column='sendSite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    piece = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    goodstype = models.CharField(db_column='goodsType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    belongno = models.CharField(db_column='belongNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dispatchreciper = models.CharField(db_column='dispatchReciper', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bagunid = models.CharField(db_column='baGunId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sto_wt_op'


class XyCusSend(models.Model):
    cus_name = models.CharField(max_length=255, blank=True, null=True)
    weight_section = models.CharField(max_length=255, blank=True, null=True)
    dep_name = models.CharField(max_length=255, blank=True, null=True)
    date_time = models.CharField(max_length=255, blank=True, null=True)
    ticket_number = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    turnover = models.FloatField(blank=True, null=True)
    avg_weight = models.FloatField(blank=True, null=True)
    avg_weight_price = models.FloatField(blank=True, null=True)
    avg_day_ticket = models.FloatField(blank=True, null=True)
    avg_day_turnover = models.FloatField(blank=True, null=True)
    avg_day_weight = models.FloatField(blank=True, null=True)
    avg_ticket_price = models.FloatField(blank=True, null=True)
    test = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_cus_send'


class XyMenu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    menu_level = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_menu'


class XyMenuLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=255, blank=True, null=True)
    menu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_menu_level'


class XyUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    user_name = models.CharField(max_length=16)
    user_password = models.CharField(max_length=24)
    level = models.ForeignKey(XyMenuLevel, models.DO_NOTHING)
    token = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xy_users'
