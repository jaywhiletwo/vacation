from django.conf.urls import patterns, include, url

from project import urls as project_urls


urlpatterns = patterns('',
    url(r'^vacation/', include(project_urls)),
)
