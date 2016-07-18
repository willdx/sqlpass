# -*- coding: utf-8 -*-
'''
File Name: exception_handler.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 日  7/17 17:35:53 2016
'''
import sys
import json
import logging
import traceback
from sqlpass import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    f = sys._getframe().f_code.co_name
    response = exception_handler(exc, context)
    if response is None:
        err = traceback.format_exception(*sys.exc_info())
        print(json.dumps(err,indent=2,ensure_ascii=False))
        detail = exc.message if settings.DEBUG else '服务器内部错误'
        res = {
            "detail":detail,
            "err":err,
            }
        response = Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
