from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers

from music.models import Song

def LikeView(request):
    id_song = request.GET.get('id_song', None)
    id_user = request.GET.get('id_user', None)

    song = get_object_or_404(Song, pk=id_song)
    user = get_object_or_404(User, pk=id_user)

    if user in song.likes.all():
        song.likes.remove(user)
    else:
        song.likes.add(user)
    song.save()

    all_users = song.likes.all()

    return JsonResponse({'song_likes':len(song.likes.all()), 'all_users':serializers.serialize('json', all_users)})

def FavoriteSongView(request):
    id_song = request.GET.get('id_song', None)
    id_user = request.GET.get('id_user', None)

    song = get_object_or_404(Song, pk=id_song)
    user = get_object_or_404(User, pk=id_user)

    action = ''

    if user in song.favorites.all():
        song.favorites.remove(user)
        action = 'remove'
    else:
        song.favorites.add(user)
        action = 'add'
    song.save()

    return JsonResponse(action, safe=False)

class IndexTemplateView(ListView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        public_songs = Song.objects.filter(visibility=True)
        print(public_songs)
        context = {
            "public_songs":public_songs
        }
        return render(request, self.template_name, context) 