from django.shortcuts import render
from .models import KeyGoal, KeyActivity


def kat(request):
    context = {
        'key_goals': KeyGoal.objects.all(),
    }
    return render(request, 'index.html', context)
