from django.shortcuts import render_to_response
from django.template import RequestContext
from subprocess import check_output
from vacation.models import Gallery, Image, Video, Message


def append_menu_items(context, request):
    menu_context = {
        'messages_list': Message.objects.all(),
        'collections_list': Gallery.objects.all(),
        'videos_list': Video.objects.all(),
    }
    if not request:
        return dict(context.items() + menu_context.items())
    else:
        return RequestContext(request, dict(context.items() + menu_context.items()))


def show_home(request, banner=None):
    title = 'The #1 spot for pictures of Ryan, Tobias, etc...'
    context = {
        'title': banner or title,
        'description': '',
    }
    return render_to_response('base.html', append_menu_items(context, request))


def list_images(request, gallery_id):
    gallery = Gallery.objects.get(id=gallery_id)
    context = {
        'title': gallery.name,
        'path': gallery.dir_name,
        'image_list': Image.objects.filter(gallery_id=gallery_id),
        'active_id': gallery.id,
        'active_type': u'gallery', 
    }
    return render_to_response('image_list.html', append_menu_items(context, request))


def show_image(request, gallery_id, image_id):
    gallery = Gallery.objects.get(id=gallery_id)
    image = Image.objects.get(id=image_id)
    context = {
        'title': gallery.name,
        'active_id': gallery.id,
        'active_type': u'gallery', 
        'path': gallery.dir_name,
        'file': image.filename + '.' + image.extension,
        'next_image_id': image.id + 1,
        'prev_image_id': image.id - 1,
    }
    return render_to_response('show_image.html', append_menu_items(context, request))


def show_video(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        'title': video.filename,
        'active_id': video.id,
        'active_type': u'video', 
        'path': video.dir_name,
        'file': video.filename + '.' + video.extension,
    }
    return render_to_response('show_video.html', append_menu_items(context, request))


def show_message(request, message_id):
    message = Message.objects.get(id=message_id)
    context = {
        'title': '',
        'active_id': message.id,
        'active_type': u'message', 
        'text': message.text,
        'posted': message.posted,
        'image': message.image,
        'video': message.video,
    }
    return render_to_response('show_message.html', append_menu_items(context, request))



