from django.contrib import admin
from django.conf import settings
from .models import KeyGoal, KeyActivity


admin.site.register(KeyGoal)
admin.site.register(KeyActivity)
