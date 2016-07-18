#!/bin/bash
#coding=utf-8
#停止uWsgi程序

ps -ef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9
