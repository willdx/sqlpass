# -*- coding: utf-8 -*-
'''
File Name: recordb.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 日  7/17 21:58:49 2016
'''
from spa.models import Error,Pass

def record_black(**kwargs):
    print "kwargs:",kwargs
    line = {
    "auth_user":kwargs["auth_user"],
    "project":kwargs["project"],
    "sql":kwargs["sql"],
    "error_info":kwargs["error_info"],
    "auth_status":kwargs["auth_status"],
    "description":kwargs["description"],
    }
    error = Error(**line)
    error.save() #记录到黑名单库

def record_write(**kwargs):
    line = {
    "auth_user":kwargs["auth_user"],
    "project":kwargs["project"],
    "sql":kwargs["sql"],
    "auth_status":kwargs["auth_status"],
    "description":kwargs["description"],
    }
    pas = Pass(**line)
    pas.save() #记录白名单库
