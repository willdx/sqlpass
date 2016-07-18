from django.conf.urls import patterns, include, url
from django.contrib import admin
import spa

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(spa.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
