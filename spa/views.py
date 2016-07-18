# -*- coding: utf-8 -*-
'''
File Name: views.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年06月26日 星期五 15时55分35秒
'''
import sys
import time
import json
import datetime

from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication

from formatcls import format_cls
from models import Power,Error,Pass
from spa.serializers import SqlpassPowerSerializer
from spa.serializers import SqlpassPassSerializer
from spa.serializers import SqlpassErrorSerializer
from core.clog import log
from core.resp import get_resp
from core.recordb import record_write
from core.settings import check_step,black_log,write_log

class SpaViewSet(ListCreateAPIView):
    """进行SQLPASS认证"""
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    paginate_by = 100000
    model = Error
    queryset = model.objects.all()
    serializer_class = SqlpassErrorSerializer
    filter_fields = ('auth_user', 'token', 'project', 'sql')


    def get(self, request):
        """重写get方法，返回不支持GET方法信息"""
        if request.method == "GET":
            dic = {}
            dic["auth_status"] = False
            dic["errorinfo"] = "不支持GET方法"
            dic["description"] = "spa接口仅支持POST方法验证SQL"
            return Response(get_resp(**dic))

    def post(self, request,):
        #p_query = request.POST
        #p_dict = p_query.dict()
        #print "p_dict:",p_dict
        p_dict = request.data
        data = self.check(**p_dict)
        return Response(data)

    def check(self, **kwargs):
        """验证逻辑"""
        for cls in check_step.keys():
            cls = format_cls('check', cls)
            obj = cls(**kwargs)
            resp = obj.check()
            if resp:
                return resp
        #所有规则都验证通过后返回验证通过信息
        kwargs["auth_status"] = True
        kwargs["description"] = "验证通过"
        #所有规则通过后记录白名单
        record_write(**kwargs)
        return get_resp(**kwargs)



class ViewApiViewBase(ListAPIView):
    '''定义基类，基类继承ListAPIView'''
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    paginate_by = 100000


class PowerViewSet(ListCreateAPIView):
    """获取授权表的规则"""
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    paginate_by = 100000

    model = Power
    queryset = model.objects.all()
    serializer_class = SqlpassPowerSerializer
    filter_fields = ('auth_user', 'project', 'token')


class ErrorViewSet(ViewApiViewBase):
    """获取黑名单表：sqlpass_error的内容"""
    model = Error
    queryset = model.objects.all()
    serializer_class = SqlpassErrorSerializer
    filter_fields = ('auth_user', 'project', 'sql')


class PassViewSet(ViewApiViewBase):
    """获取白名单表：sqlpass_pass 的内容"""
    model = Pass
    queryset = model.objects.all()
    serializer_class = SqlpassPassSerializer
    filter_fields = ('sql_type', 'sql')

