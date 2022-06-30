from django.urls import path, include

from . import views as music_views

app_name = 'music'

urlpatterns = [
    path('song/save/', music_views.SongFormView.as_view(), name="save_song"),
    path('album/save/', music_views.AlbumFormView.as_view(), name="save_album"),
    path('<pk>/delete/', music_views.SongDeleteView.as_view(), name="delete_song"),
    path('most-popular/', music_views.MostPopularView.as_view(), name="most_popular"),
]   