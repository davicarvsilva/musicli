from django.urls import path, include

from . import views as music_views

app_name = 'music'

urlpatterns = [
    path('save/', music_views.SongFormView.as_view(), name="save_song"),
]