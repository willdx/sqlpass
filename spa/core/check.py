# -*- coding: utf-8 -*-

from resp import get_resp
from spa.formatcls import format_cls
from recordb import record_black
from settings import check_step


class params_check(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def check(self):
        resp = None
        for name,cls in check_step[params_check.__name__].items():
            cls = format_cls('rule', cls)
            print "执行验证:",cls.__name__
            obj = cls(**self.kwargs)
            status = obj.status
            if not status:
                resp = get_resp(**obj.__dict__)
                print "[Faild]:",cls.__name__
                resp["auth_status"]=False
                return resp
            else:
                print("check_step:{}下{}验证通过".format(params_check.__name__,name))


class namelist_check(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def check(self):
        resp = None
        for name,cls in check_step[namelist_check.__name__].items():
            cls = format_cls('rule', cls)
            print "执行验证:",cls.__name__
            obj = cls(**self.kwargs)
            status = obj.status
            if not status:
                print("check_step:{}下{}验证通过".format(namelist_check.__name__,name))
            elif cls.__name__ == "namelist_check_write":
                resp = get_resp(**obj.__dict__)
                print "[Faild]:",cls.__name__
                resp["auth_status"]= True 
                return resp
            elif cls.__name__ == "namelist_check_black":
                resp = get_resp(**obj.__dict__)
                print "[Faild]:",cls.__name__
                resp["auth_status"]= False
                return resp

class rule_check(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def check(self):
        resp = None
        for name,cls in check_step[rule_check.__name__].items():
            cls = format_cls('rule', cls)
            print "执行验证:",cls.__name__
            obj = cls(**self.kwargs)
            status = obj.status
            if not status:
                resp = get_resp(**obj.__dict__)
                print "[Faild]:",cls.__name__
                resp["auth_status"]=False
                #自定义规则验证失败,记录黑名单库
                obj.__dict__["auth_status"]=False
                record_black(**obj.__dict__)
                return resp
            else:
                print("check_step:{}下{}验证通过".format(rule_check.__name__,name))
