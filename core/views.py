from django.shortcuts import render
from django.views.generic import ListView


from music.models import Song


class IndexTemplateView(ListView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        public_songs = Song.objects.filter(visibility=True)
        print(public_songs)
        context = {
            "public_songs":public_songs
        }
        return render(request, self.template_name, context)