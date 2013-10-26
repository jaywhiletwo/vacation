from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from vacation.models import Widget

def launch(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)
    widgets = Widget.objects.filter(widgetpick__user=user)
    context = {
        'user': user, 
        'widgets': widgets.order_by('widgetpick__order'),
    }
    return render_to_response('launch.html', context)
