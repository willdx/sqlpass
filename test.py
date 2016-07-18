# -*- coding: utf-8 -*-
'''
File Name: test.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 日  7/17 17:26:16 2016
'''
import os
import sys
import json 
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

def check(data):
    '''验证SQL实例'''
    headers = {"Content-type" : "application/json",
    "Authorization" : "Token 60ed5875a1658d2d957cbafc26b9c77cc4260065",}
    url = "http://127.0.0.1:8080/api/spa/"
    resp = requests.post(url,headers=headers,data=data)
    json_data = json.loads(resp.text) 
    return json_data

if __name__=="__main__":
    info = {"project": "xiang.dai", "auth_user": "xiang.dai", "sql": "select * from a;"}
    print check(json.dumps(info))

