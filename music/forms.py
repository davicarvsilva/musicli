from django import forms
from .models import Song
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("title", "release_date", "visibility", "file", )

        widgets = {
            'release_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(SongForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        inst = super(SongForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst