# Generated by Django 3.2.13 on 2022-06-30 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_auto_20220629_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('release_date', models.DateField()),
                ('visibility', models.BooleanField(default=True)),
                ('posted_date', models.DateField(default=django.utils.timezone.now)),
                ('favorites', models.ManyToManyField(related_name='album_favorites', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='album_likes', to=settings.AUTH_USER_MODEL)),
                ('songs', models.ManyToManyField(to='music.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
