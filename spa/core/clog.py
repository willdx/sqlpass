# -*- coding: utf-8 -*-
'''
File Name: clog.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年11月19日 星期四 16时52分11秒
'''
import os
import sys
import logging
 
class Logger():
    def __init__(self,path,clevel=logging.DEBUG,Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        #设定日志输入格式
        logfmt = '[%(asctime)s] [%(levelname)s] [file:%(pathname)s] [line:%(lineno)d] %(message)s'
        datefmt = '%Y%m%d %H:%M:%S'
        fmt = logging.Formatter(logfmt,datefmt)
        #cmd日志输入配置
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        self.logger.addHandler(sh)
        #输入日志到指定文件配置
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(fh)
 
    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)
    def warn(self,message):
        self.logger.warn(message)
    def error(self,message):
        self.logger.error(message)
    def cri(self,message):
        self.logger.critical(message)

def log(log_file):
    log_obj = Logger(log_file,logging.ERROR,logging.DEBUG)
    return log_obj

if __name__ =='__main__':
    log_obj = custom('test.log')
    log_obj.debug('一个debug信息')
    log_obj.info('一个info信息')
    log_obj.warn('一个warning信息')
    log_obj.error('一个error信息')
    log_obj.cri('一个致命critical信息')
