from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

def user_song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users_data/user_{0}/songs/{1}'.format(instance.user.id, filename)

class Song(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to=user_song_directory_path)
    release_date = models.DateField()
    visibility = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=CASCADE)



    

