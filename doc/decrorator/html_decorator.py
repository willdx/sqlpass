# -*- coding: utf-8 -*-
'''
File Name: html_decorator.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年07月02日 星期四 17时30分01秒
'''
def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"])
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator

@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"

print hello()
