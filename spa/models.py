# -*- coding: utf-8 -*-
'''
File Name: models.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年06月26日 星期五 15时19分34秒
'''
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Power(models.Model):
    '''
    授权表，记录授权信息
    '''
    id = models.IntegerField(db_column='Id', primary_key=True)
    auth_user = models.CharField(max_length=10, blank=True)
    project = models.CharField(max_length=10, blank=True)
    token = models.CharField(max_length=100, blank=True)
    power = models.CharField(max_length=1,blank=True)
    sql_list = models.CharField(max_length=200, blank=True)
    licensed_user = models.CharField(max_length=200, blank=True)
    description = models.CharField(db_column='Description', max_length=250, blank=True)
    status = models.CharField(db_column='Status', max_length=1, blank=True)
    is_valid = models.NullBooleanField()
    class Meta:
        db_table = 'sqlpass_power'
        unique_together =  ('auth_user','token','project','power','sql_list')

class Error(models.Model):
    '''
    黑名单表，记录SQL语法验证和注入测试未通过的SQL信息
    '''
    auth_user = models.CharField(max_length=10, blank=True)
    project = models.CharField(max_length=10, blank=True)
    sql = models.CharField(max_length=1000, primary_key=True)
    power = models.CharField(max_length=1, blank=True)
    error_info = models.CharField(max_length=1000, blank=True)
    auth_status = models.CharField(max_length=10, blank=True)
    description = models.CharField(db_column='Description', max_length=250, blank=True)

    class Meta:
        db_table = 'sqlpass_error'
        unique_together =  ('auth_user','project','sql')


class Pass(models.Model):
    '''
    白名单SQL表,记录自定义规则，权限验证，语法验证和注入测试都通过的SQL信息
    '''
    auth_user = models.CharField(max_length=10, blank=True)
    project = models.CharField(max_length=10, blank=True)
    sql = models.CharField(max_length=1000, blank=True,primary_key=True) 
    sql_type = models.CharField(max_length=10, blank=True)
    auth_status = models.CharField(max_length=10, blank=True)
    description = models.CharField(db_column='Description', max_length=250, blank=True)
    class Meta:
        db_table = 'sqlpass_pass'
        unique_together =  ('auth_user','project','sql')

