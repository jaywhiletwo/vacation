from django.contrib import admin
from django.conf import settings
from .models import KeyGoal, KeyActivity


class KeyActivityAdmin(admin.ModelAdmin):
    pass
    #list_display = ('__unicode__', 'interval', 'last_time', )
    #list_editable = ('interval', 'last_time', )


admin.site.register(KeyGoal)
admin.site.register(KeyActivity)
