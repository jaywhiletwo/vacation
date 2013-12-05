from django.http import HttpResponse
from .models import KeyGoal, KeyActivity


def kat(request):
    response = ''
    for g in KeyGoal.objects.all():
        response = ''.join((response, unicode(g), '<ul>'))
        for a in g.keyactivity_set.all():
            response = ''.join((response, '<li>', unicode(a), '</li>'))
            pass
        response = ''.join((response, '</ul>'))
    return HttpResponse(response)
