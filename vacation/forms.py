from django import forms
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from vacation.models import Image, Gallery, Widget


class NotesWidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ['value', ]
        widgets = {'value': forms.Textarea(attrs={'rows': '15', 'onfocus': 'inputFocus()', 'onblur': 'inputBlur()', }), }

    def clean(self, *args, **kwargs):
        user_tag = '[note from %s]' % self.data['user']
        val = self.cleaned_data['value'].split('\n')
        if val[0].startswith('[') and val[0].strip().endswith(']'):
            val[0] = user_tag
        else:
            val.insert(0, user_tag)
        self.cleaned_data['value'] = '\n'.join(val)
        return super(NotesWidgetForm, self).clean(*args, **kwargs)


class UploadImageForm(forms.Form):
    filename = forms.CharField(max_length=255, label="Filename (e.g. 'ryan_napping')", validators=[RegexValidator(regex='[A-Za-z0-9_-]+', message='invalid characters')])
    image_file = forms.FileField()
    gallery = forms.ModelChoiceField(queryset=Gallery.objects.all().order_by('order'), empty_label=None)
    message_name = forms.CharField(max_length=255, required=False, label="Message name (optional)")
    message_text = forms.CharField(max_length=2048, required=False, widget=forms.Textarea, label="Message text (optional)")


REBOOT_CHOICES = (('to_windows', 'To Windows'),
                  ('to_linux', 'To Linux'),
                 )

class RebootForm(forms.Form):
    reboot_type = forms.ChoiceField(choices=REBOOT_CHOICES)

