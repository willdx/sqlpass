# -*- coding: utf-8 -*-
'''
File Name: spa/urls.py
Author: WillDX
mail: xiang.dai@shuyun.com
Created Time: 2015年06月29日 星期一 11时29分27秒
'''
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from spa.views  import *

urlpatterns = patterns('spa.views',
        url(r'^error/$', ErrorViewSet.as_view()),
        url(r'^pass/$', PassViewSet.as_view()),
        url(r'^power/$', PowerViewSet.as_view()),
        url(r'^spa/$', SpaViewSet.as_view()),
        )

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
)


