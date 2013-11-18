from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.context_processors import csrf
from vacation.models import Widget, WidgetPage
from vacation.forms import NotesWidgetForm


def launch_page(request, page_id):
    if request.method == 'POST':
        widget = Widget.objects.get(id=request.POST['widget_id'])
        form = NotesWidgetForm(request.POST, instance=widget)
        form.save()

    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)
    page = WidgetPage.objects.get(pk=page_id)
    widgets = Widget.objects.filter(pages=page)
    context = {
        'user': user, 
        'page': page,
        'widgets': widgets.order_by('order'),
    }

    try:
        context['banner_image'] = '/%s/%s.%s' % (page.banner_image.gallery.dir_name, page.banner_image.filename, page.banner_image.extension)
    except AttributeError:
        pass

    context.update(csrf(request))
    return render(request, 'launch.html', context)

def launch(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)
    
    default_page = WidgetPage.objects.filter(user=user).order_by('id')[0]

    return launch_page(request, default_page.id)
