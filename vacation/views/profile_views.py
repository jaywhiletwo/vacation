from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from vacation.views.static_views import append_menu_items
 

widgets = [
    '<iframe height=400px src="http://m.weatherbug.com/VA/Arlington-weather/local-forecast"></iframe>',
    '<iframe height=400px src="http://m.people.com"></iframe>', 
]

def show_widgets(request):
    title = 'Welcome back, %s' % (request.user, )
    context = {
        'title': title,
        'description': '',
        'widgets': widgets,
    }
    return render_to_response('show_widgets.html', append_menu_items(context, request=request))


def login_user(request):
        logout(request)
        username = password = ''
        if request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                        if user.is_active:
                                login(request, user)
                                return HttpResponseRedirect('/widgets')
        context = {
            'form_title': 'Login', 
            'form_action': '/login/',
            'form': AuthenticationForm(),
        }
        return render_to_response('login.html', append_menu_items(context, request=request))


