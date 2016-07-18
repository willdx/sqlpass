
#SQLPASS系统

##简介
    
    基于线上执行SQL语句的安全性考虑,需要对SQL进行验证,降低误操作风险,提供API形式的调用,并绑定到产品和个人

##验证流程

    1.验证输入参数完整性 (ps: 输入参数: 用户名 项目名 SQL)

    2.权限验证 (ps: 使用用户名,项目名进行赋权，将权限控制在什么用户在什么项目上能执行那些命令)

    3.SQL自定义规则验证 

        ##自定义规则暂时添加如下内容,后续可自行扩展

        3.1.需要进行自定义规则检查的SQL类型列表['SELECT','DELETE','UPDATE','INSERT','CREATE','ALTER','DROP','TRUNCATE'],不在列表中的SQL类型会直接报错，其中kill例外,意思是如果sql命令为kill也允许执行；

        3.2.在授权允许的情况下select,create,alter,truncate,drop允许执行

        3.3.update,delete 必须有where才允许执行,否则不允许执行

    4.是否存在白名单库 (ps:使用白名单机制,只允许特定的SQL执行)

    5.是否存在黑名单库

    6.SQL语法验证 (ps:需要测试Mysql数据库,验证逻辑为先去测试数据库执行,若不是语法错误则通过,依赖测试MYSQL数据库,spa/core/settings.py的mysql_syntax_testdb选项配置)


##流程图地址 

[流程图地址](https://www.processon.com/diagraming/55a5cface4b0e611cd3fb319)

##日志记录

    1.uwsgi访问日志： ./uwsgi_sqlpass.log (ps:可以自行设定)

##安装 
	
    git clone 本项目地址
    mkvirtualenv sqlpass (ps:Python 2.7.10)
    cd sqlpass
    pip install -r requirement.txt
    安装完成启动

##服务启动与停止

-启动
	
	runserver:

	python manage.py runserver 127.0.0.1:8080
	
	uwsgi:
    1.开发环境:sh restart_dev.sh (ps:需要自行设定环境配置信息)
    
    2.线上环境:sh restart.sh (ps:需要自行设定环境配置信息)

-停止

    sh stop.sh



##调用方式

>1.Django Rest Framework WEB界面 登录后可运行
    
[sqlpass_spa](http://7xj7fg.com1.z0.glb.clouddn.com/sqlpass_spa.png)

>2.命令行 
	
	(ps:token需要去admin后台生成,添加token方式自行百度哦!)
	➜  ~ curl -XPOST -H "Content-type: application/json"   -H 'Authorization: Token 60ed5875a1658d2d957cbafc26b9c77cc4260065' "http://127.0.0.1:8080/api/spa/" -d '{"project": "xiang.dai", "auth_user": "xiang.dai", "token": "60ed5875a1658d2d957cbafc26b9c77cc4260065", "sql": "select * from a;"}'

>3.python程序
	
	# -*- coding: utf-8 -*-
	import os
	import sys
	import json·
	import requests
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	def check(data):
	    '''验证SQL实例'''
	    headers = {"Content-type" : "application/json",
	    "Authorization" : "Token 60ed5875a1658d2d957cbafc26b9c77cc4260065",}
	    url = "http://127.0.0.1:8080/api/spa/"
	    resp = requests.post(url,headers=headers,data=data)
	    json_data = json.loads(resp.text)·
	    return json_data
	
	if __name__=="__main__":
	    info = {"project": "xiang.dai", "auth_user": "xiang.dai", "sql": "select * from a;"}
	    print check(json.dumps(info))

	结果:
	{"description":"","error_info":"匹配到白名单条目","project":"xiang.dai","sql":"select * from a;","auth_user":"xiang.dai","auth_status":true}

	

##其他

    1.查看黑名单库
    
[sqlpass_error](http://7xj7fg.com1.z0.glb.clouddn.com/sqlpass_error.png)

    2.查看白名单库
    
[sqlpass_pass](http://7xj7fg.com1.z0.glb.clouddn.com/sqlpass_pass.png)

    3.查看权限库
    
[sqlpass_power](http://7xj7fg.com1.z0.glb.clouddn.com/sqlpass_power.png)

