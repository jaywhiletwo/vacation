from django.shortcuts import render
from .models import KeyGoal, KeyActivity


def kat(request):
    if request.method == 'POST':
	save_activity(request.POST['name'], request.POST['goal_id'])

    context = {
        'key_goals': KeyGoal.objects.all(),
    }
    return render(request, 'index.html', context)

def save_activity(name, goal_id):
    KeyActivity.objects.create(name=name, key_goal=KeyGoal.objects.get(id=goal_id))
