# -*- coding: utf-8 -*-
'''
File Name: serializers.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年06月26日 星期五 10时00分53秒
'''
from models import *
from rest_framework import serializers
from rest_framework import fields


class SqlpassPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        #fields = ('project', 'power', 'is_valid')


class SqlpassPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        #fields = ('sql','sql_type')


class SqlpassErrorSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Error
        #fields = ('project', 'power', 'is_valid')
        read_only_fields = ('power', 'sql_list', 'status', 'errorinfo',
'description')
