from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from kat.urls import urlpatterns as kat_urls
from vacation.views.launch import launch, launch_page
from vacation.views.static_views import *
from vacation.views.upload_views import UploadImage
from vacation.views.reboot_views import RebootView
from vacation.views.profile_views import login_user, show_widgets
from vacation.models import Gallery


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', launch, name='launch'),
    url(r'^gallery/$', show_home, name='show_home'),
	url(r'list_images/(?P<gallery_id>\d+)/$', list_images, name='list_images'),
	url(r'^show_image/(?P<gallery_id>\d+)/(?P<image_id>\d+)/$', show_image, name='show_image'),
	url(r'^show_video/(?P<video_id>\d+)/$', show_video, name='show_video'),
	url(r'^show_message/(?P<message_id>\d+)/$', show_message, name='show_message'),
    url(r'^login/$', login_user, name='login_user'),
    url(r'^launch/(?P<page_id>\d+)/$', launch_page, name='launch_page'),
    url(r'^launch/$', launch, name='launch'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}), 
    url(r'^widgets/$', login_required(show_widgets), name='show_widgets'),
    url(r'^upload/$', login_required(UploadImage.as_view(), login_url='/vacation/admin'), name='upload_image'),
    url(r'^reboot/$', login_required(RebootView.as_view(), login_url='/vacation/admin'), name='reboot'),
    url(r'^kat/', include(kat_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
