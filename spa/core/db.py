# -*- coding: utf-8 -*-
'''
File Name: db.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 日  7/17 21:13:17 2016
'''
import os
import sys
import json
import MySQLdb
import MySQLdb.cursors
from warnings import filterwarnings

class DatabaseOperation:
    '''
    数据库相关操作
    '''
    def __init__(self, host, user, passwd, dbname, port, **kwargs):
        '''
        初始化数据库连接

        :param  sql:    待执行SQL 
        :param  host:   数据库地址 
        :param  user:   数据库连接用户
        :param  passwd: 数据库连接密码
        :param  dbname: 数据库库名
        :param  port:   数据库连接端口,若不传递默认为3306
        :param  **kwargs: 可变长参数,后续可能添加超时时间之类的参数,暂未使用
        '''
        filterwarnings('error', category = MySQLdb.Warning)
        self.conn = MySQLdb.connect(
                host = host,
                user = user, 
                passwd = passwd, 
                db = dbname,
                port = port,
                use_unicode = 0, 
                charset = 'utf8', 
                **kwargs)

    def get_cursor(self):
        '''
        此函数返回默认游标;
        若使用该游标执行SQL,返回tuple类型结果,tuple内的元素为tuple元组类型

        :return: :MySQLdb.cursors.Cursor: 默认游标 
        :rtype: MySQLdb.cursors.Cursor 
        '''
        return self.conn.cursor()

    def get_dict_cursor(self):
        '''
        此函数返回字典游标;
        若使用该游标执行SQL,返回tuple类型结果,tuple内的元素为dict字典类型

        :return: :MySQLdb.cursors.DictCursor: 字典游标
        :rtype:  MySQLdb.cursors.DictCursor
        '''
        return self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def run(self, cursor, sql):
        '''
        执行SQL,返回执行结果；其中cursor为游标:
        若为默认游标,返回tuple类型结果,tuple内的元素为tuple元组类型
        若为字典游标,返回tuple类型结果,tuple内的元素为dict字典类型
        
        :param cursor: 游标
        :param sql: 待执行SQL
        :return: :tuple: SQL执行结果
        :rtype: tuple
        '''
        cursor.execute(sql)
        return cursor.fetchall()

    def __enter__(self):
        '''
        内置的__enter__方法;在实例化对象时自动会先调用该方法
        '''
        return self

    def __exit__(self, type, value, traceback):
        '''
        内置的__exit__方法;在最终return结果前自动调用该方法
        '''
        self.conn.commit()
        self.conn.close()


