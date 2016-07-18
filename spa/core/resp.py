# -*- coding: utf-8 -*-
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

def get_resp(auth_user='',project='',sql='',auth_status='',error_info='',description='',*args,**kwargs):
    """返回消息体模型"""
    resp = {
        'auth_user': auth_user if auth_user else '' ,
        'project': project if project else '',
        'sql': sql if sql else '',
        'auth_status':auth_status if auth_status else '',
        'error_info': error_info if error_info else '',
        'description': description if description else '' ,
        }
    return resp
