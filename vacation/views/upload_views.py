from django.views.generic import View
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.conf import settings
from vacation.views.static_views import append_menu_items, list_images
from vacation.forms import UploadImageForm
from vacation.models import Image, Message
import logging

logger = logging.getLogger(__name__)


class UploadImage(View):
    def get(self, request, errors=''):
        form = UploadImageForm()
        context = {
            'form_title': 'Upload Image',
            'form_action': '/upload/',
            'form_enctype': 'multipart/form-data',
            'form': form,
            'errors': errors,
        }
        context.update(csrf(request))
        return render_to_response('base_form.html', append_menu_items(context, request))

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            image_file = data['image_file']
            dot_pos = image_file.name.find('.') 
            extension = image_file.name[dot_pos+1:]
            image_obj = self.create_image_object(data['filename'], extension, data['gallery'])
            self.copy_image_to_directory(data['filename'], extension, image_file, data['gallery'])
            self.create_message(data['message_name'], data['message_text'], image_obj)
            return list_images(request, form.cleaned_data['gallery'].id)
        else:
            return self.get(request, errors=form.errors)

    def create_image_object(self, filename, extension, gallery):
        return Image.objects.create(filename=filename, extension=extension, gallery=gallery)

    def copy_image_to_directory(self, filename, extension, image_file, gallery):
        internal_filename = filename + '.' + extension
        destination = settings.LOCAL_RESOURCE + gallery.dir_name + '/' 
        tn_destination = destination + 'tn/'
        with open(destination + internal_filename, 'w') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        with open(tn_destination + internal_filename, 'w') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

    def create_message(self, name, text, image_obj):
        if not name and not text:
            pass
        else:
            return Message.objects.create(name=name, text=text, image=image_obj)
