# -*- coding: utf-8 -*-
'''
File Name: hello.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年07月02日 星期四 17时16分19秒
'''
def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

@hello
def foo():
    a= "I am foo"
    return a

if __name__ == "__main__":
    a = foo()

