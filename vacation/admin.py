from django.contrib import admin
from django.conf import settings
from vacation.models import Gallery, Image, Video, Message, Widget
import subprocess


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )


admin.site.register(Widget, admin.ModelAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, admin.ModelAdmin)
admin.site.register(Video, admin.ModelAdmin)
admin.site.register(Message, admin.ModelAdmin)
