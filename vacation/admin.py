from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from vacation.models import Gallery, Image, Video, Message, Widget, WidgetPage
import subprocess


class WidgetInline(admin.StackedInline):
    model = Widget
    ordering = ('order', )
    extra = 1


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )


class PageAdmin(admin.ModelAdmin):
    inlines = [
        WidgetInline,
    ]


class WidgetAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title_link', 'columns', 'order', 'page', )
    list_editable = ('columns', 'order', 'page', )
    list_filter = ('page', )
    ordering = ('order', )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(WidgetPage, PageAdmin)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Message)
