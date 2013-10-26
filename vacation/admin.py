from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from vacation.models import Gallery, Image, Video, Message, Widget, WidgetPick
import subprocess

admin.site.unregister(User)



class UserInline(admin.TabularInline):
    model = WidgetPick
    ordering = ('order', )

class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', )


admin.site.register(User, UserAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Widget)
admin.site.register(WidgetPick)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Message)
