from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from .views import kat


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', kat, name='kat'),
    url(r'^admin/', include(admin.site.urls)),
)
