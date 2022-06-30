from django import forms
from .models import Song, Album
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

class DateInput(forms.DateInput):
    input_type = 'date'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("title", "release_date", "visibility", "songs", )

        widgets = {
            'release_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        songs = kwargs.pop('songs')
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['songs'].widget.choices=((song.pk, song) for song in songs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        inst = super(AlbumForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst