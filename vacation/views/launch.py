from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from vacation.models import Widget, WidgetPage


def launch_page(request, page):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)
    widgets = Widget.objects.filter(page=page)
    context = {
        'user': user, 
        'page': page,
        'banner_image': '/%s/%s.%s' % (page.banner_image.gallery.dir_name, page.banner_image.filename, page.banner_image.extension),
        'widgets': widgets.order_by('order'),
    }
    return render_to_response('launch.html', context)

def launch(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)
    
    default_page = WidgetPage.objects.filter(user=user)[0]

    return launch_page(request, default_page)
