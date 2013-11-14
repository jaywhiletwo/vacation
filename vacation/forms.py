from django import forms
from django.core.validators import RegexValidator
from vacation.models import Image, Gallery


class UploadImageForm(forms.Form):
    filename = forms.CharField(max_length=255, validators=[RegexValidator(regex='[A-Za-z0-9_-]+', message='invalid characters')])
    image_file = forms.FileField()
    gallery = forms.ModelChoiceField(queryset=Gallery.objects.all().order_by('order'), empty_label=None)
    message_name = forms.CharField(max_length=255, required=False)
    message_text = forms.CharField(max_length=2048, required=False, widget=forms.Textarea)


REBOOT_CHOICES = (('to_windows', 'To Windows'),
                  ('to_linux', 'To Linux'),
                 )

class RebootForm(forms.Form):
    reboot_type = forms.ChoiceField(choices=REBOOT_CHOICES)

