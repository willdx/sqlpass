# -*- coding: utf-8 -*-
import sys

sys.path.insert(0,sys.path[0]+"/spa")

def format_cls(filename, cls):
    """字符串方式导入模块,并返回类"""
    dirs = __import__('core.'+filename)
    module = getattr(dirs, filename)
    cls = getattr(module, cls)
    return cls
