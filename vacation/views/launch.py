from django.shortcuts import render_to_response
from vacation.models import Widget

def launch(request):
    widgets = Widget.objects.all()
    context = {
        'user': request.user, 
        'widgets': widgets,
    }
    return render_to_response('launch.html', context)
