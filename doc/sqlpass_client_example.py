# -*- coding: utf-8 -*-
'''
File Name: sqlpass_client_example.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年07月24日 星期五 16时46分25秒
'''
from sqlpass_client.sqlpass_client import *

auth_user = "autops" 
project = "ccms"
sql = "kill 2348961"
token = "7db4de4ca6b448ae4a7969a4abe398bbc7a2adee"
if __name__ == "__main__":
    sqlpass_check(auth_user,project,sql,token)
