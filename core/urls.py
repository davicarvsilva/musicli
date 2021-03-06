from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.IndexTemplateView.as_view(), name="index"),
    path('song/like/', core_views.LikeView, name="like_song"),
    path('song/favorite/', core_views.FavoriteSongView, name="favorite_song"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
