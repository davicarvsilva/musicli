from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

from music.models import Song

from .forms import SongForm

class MostPopularView(View):
    template_name = 'music/most_popular.html'

    def get(self, request, *args, **kwargs):
        most_popular_songs = Song.objects.all().order_by('-likes')
        
        context = {
            'most_popular_songs':most_popular_songs
        }

        return render(request, self.template_name, context)

class SongFormView(View):
    form_class = SongForm
    template_name = 'music/save_song_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, user=request.user)
        if request.method == 'POST' and request.FILES['file']:
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    
            return redirect('music:save_song')
        

        return render(request, self.template_name, {'form': form})
