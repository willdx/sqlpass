# -*- coding: utf-8 -*-
'''
File Name: sql_parse.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年11月30日 星期一 22时36分00秒
'''
import sys
import sqlparse

def parse(sql):
    '''将sql格式化用于分析是否满足自定义规则'''
    lis =  []
    sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
    parsed = sqlparse.parse(sql)[0].tokens
    sql_type = sqlparse.sql.Statement(tokens=parsed).get_type().lower()
    for i in parsed:
        if not i.is_whitespace():
            if isinstance(i, sqlparse.sql.Where): 
                for j in i.tokens:
                    lis.append(unicode(j))
            else:
                lis.append(unicode(i))
    return sql_type,lis

if __name__ == "__main__":
    sql="""select id from res_users as r left join res_partner as p on \
p.id=r.partner_id where name = (select name from res_partner where id = 1) limit 3"""
    print "待分析SQL:",sql
    types,formats = parse(sql)
    print "类型:",types
    print "格式化结果:",formats
