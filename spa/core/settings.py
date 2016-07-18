# -*- coding: utf-8 -*-
import json
# 白名单日志
write_log = "./logs/sqlpass_pass_recode.log"
black_log = "./logs/uwsgi/sqlpass_error_recode.log"

# 验证步骤
check_step = {
  "params_check": {
    "complete": "params_check_complete",
    "permission": "params_check_permission",
  },
  "namelist_check": {
    "black": "namelist_check_black",
    "write": "namelist_check_write",
  },
  "rule_check": {
    "syntax": "rule_check_syntax",
    "custom": "rule_check_custom",
  }
}

# 自定义规则负责人
custom_rule_charge = "jingyi.li;xiang.dai"

# mysql语法验证测试库
mysql_syntax_testdb = {
    "db_host":"10.211.55.5", 
    "db_user":"root",
    "db_pass":"redhat",
    "db_name":"mysql",
    "port": 3306,
}

