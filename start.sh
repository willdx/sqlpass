#!/bin/bash
#coding=utf-8
#重启uWsgi程序

source /home/sqlpass/.virtualenvs/sqlpass/bin/activate
uwsgi --ini uwsgi.ini
echo "Start completed!"
