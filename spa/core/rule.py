# -*- coding: utf-8 -*-
'''
File Name: spa/rules.py
Author: WillDX
mail: xiang.dai@shuyun.com
'''
import mysql_syntax_check
from settings import mysql_syntax_testdb
from sql_parse import parse
from spa.models import Power,Error,Pass
from spa.serializers import SqlpassPowerSerializer

class SqlRuleBase(object):
    """定义基类,status 返回True表示通过验证,False表示未通过验证"""

    def __init__(self, *args, **kwargs):
        self.sql = kwargs.get("sql")
        self.auth_user = kwargs.get("auth_user")
        self.project = kwargs.get("project")
        self.sql_type, self.sql_format = parse(self.sql)

    @property
    def status(self):
        return True


class params_check_complete(SqlRuleBase):
    """验证参数完整性"""

    def __init__(self,*args, **kwargs):
        super(params_check_complete, self).__init__(*args, **kwargs)
        self.error_info = u"验证输入参数完整性失败,请验证参数是否完整"
        self.description = None

    @property
    def status(self):
        if self.sql and self.auth_user and self.project:
            return True
        else:
            return False


class params_check_permission(SqlRuleBase):
    """验证权限规则"""

    def __init__(self,*args, **kwargs):
        super(params_check_permission, self).__init__(*args, **kwargs)
        self.error_info = u"权限验证未通过,请验证用户是否有权限进行该SQL操作"
        self.description = None

    @property
    def status(self):
        line = {'auth_user':self.auth_user,
            'project':self.project,
            "is_valid": True,"status":"A"}
        try:
            power = Power.objects.get(**line)
            serializer = SqlpassPowerSerializer(power)
            power_info = serializer.data
            description = power_info['description']
            sql_list = power_info['sql_list'].split(',')
            self.description = u"SQL类型:%s;授权SQL为:%s""" % (self.sql_type.lower(),sql_list)
            if  self.sql_type.lower() in sql_list or self.sql_format[0] == u'kill':
                return True
            else:
                return False
        except Exception as e:
            print "[Faild]params_check_permission:",e
            self.description = "信息输入有误,没有查询到权限条目"
            return False


class namelist_check_black(SqlRuleBase):
    """黑名单验证"""

    def __init__(self, *args, **kwargs):
        super(namelist_check_black, self).__init__(*args, **kwargs)
        self.error_info = u"匹配到黑名单条目"
        self.description = None

    @property
    def status(self):
        line = {
            "auth_user" : self.auth_user,
            "project" : self.project,
            "sql" : self.sql
        }
        try:
            Error.objects.get(**line)
            return True # 匹配到黑名单条目
        except Exception as e:
            return False


class namelist_check_write(SqlRuleBase):
    """白名单验证"""
    def __init__(self, *args, **kwargs):
        super(namelist_check_write, self).__init__(*args, **kwargs)
        self.error_info = u"匹配到白名单条目"
        self.description = None

    @property
    def status(self):
        line = {
            "auth_user" : self.auth_user,
            "project" : self.project,
            "sql" : self.sql,
        }
        try:
            Pass.objects.get(**line)
            return True
        except Exception as e:
            return False


class rule_check_syntax(SqlRuleBase):
    '''检查SQL语法是否有误'''
    def __init__(self, *args, **kwargs):
        super(rule_check_syntax, self).__init__(*args, **kwargs)
        self.error_info = u"SQL语法错误,请检查"
        self.description = None

    @property
    def status(self):
        mysql_syntax_testdb["sql"]  = self.sql
        try:
            result = mysql_syntax_check.runsql(**mysql_syntax_testdb)
        except Exception as e:
            syntax_error = "You have an error in your SQL syntax"
            if syntax_error in str(e):
                self.description = syntax_error
                return False
            else:
                return True


class rule_check_custom(SqlRuleBase):
    '''自定义规则'''
    def __init__(self, *args, **kwargs):
        super(rule_check_custom, self).__init__(*args, **kwargs)
        self.error_info = None
        self.description = "自定义规则未通过"

    @property
    def status(self):
        sql_type_list = ['select','delete','update','insert','create','alter','drop','truncate']
        if self.sql_type not in sql_type_list:
            if self.sql_format[0] == u'kill':
                return True
            else:
                self.error_info = "待执行的SQL语句类型不在自定义的规则列表中"
                return False
        else:
            #在授权允许的情况下select,create,alter,truncate,drop允许执行
            if self.sql_type in ['select','insert','create','alter','drop','truncate']:
                return True
            #update,delete 必须有where
            if self.sql_type in ['delete','update',]:
                if u'WHERE' in self.sql_format:
                    return True
                else:
                    self.error_info = "%s语句当有where条件时才允许执行" % self.sql_type
                    return False


class rule_check_inject(SqlRuleBase):
    '''检查SQL是否有注入危险'''
    pass

