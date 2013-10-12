from django.views.generic import View
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseGone
from subprocess import call
from vacation.views.static_views import append_menu_items, show_home
from vacation.forms import RebootForm, REBOOT_CHOICES


class RebootView(View):
    def get(self, request):
        form = RebootForm()
        context = {
            'form_title': 'Reboot Options',
            'form_action': '/reboot/',
            'form_enctype': 'application/x-www-form-urlencoded',
            'form': form,
        }
        context.update(csrf(request))
        return render_to_response('base_form.html', append_menu_items(context, request))

    def post(self, request):
        if request.POST['reboot_type'] == 'to_windows':
            call(["/home/jlee/boot_windows.sh"])
        elif request.POST['reboot_type'] == 'to_linux':
            call(["shutdown -r now"])
        else:
            return self.get(request)
        return show_home(request, banner="Rebooting!")
