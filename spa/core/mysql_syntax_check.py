# -*- coding: utf-8 -*-
'''
File Name: mysql_syntax_check.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 日  7/17 21:01:49 2016
'''

from db import *

def runsql(sql,db_host,db_user,db_pass,db_name,port=3306,**kwargs):
    '''
    返回tuple类型结果,tuple内的元素为dict字典类型
    '''
    with DatabaseOperation(db_host,db_user,db_pass,db_name,port) as mysql:
        cur = mysql.get_dict_cursor()
        results = mysql.run(cur, sql)
        return  results
