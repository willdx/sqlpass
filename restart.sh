#!/bin/bash
#coding=utf-8
#重启uWsgi程序

log_path='/data/uwsgi'
[ -d $log_path ] || mkdir -p $log_path

echo "Will Kill uWsgi."
ps -ef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9
echo "Killed! Will start uWsgi."
source /home/sqlpass/.virtualenvs/sqlpass/bin/activate
uwsgi --ini uwsgi.ini
echo "Start completed!"
