from django.db import models


class AlbumArt(models.Model):
    image = models.ImageField(upload_to='album_art')


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Style(models.Model):
    name = models.CharField(max_length=50)


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Album(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField()
    album_art = models.ForeignKey(AlbumArt,
                                  on_delete=models.CASCADE,
                                  related_name='album')
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               related_name='albums')
    genres = models.ManyToManyField(Genre,
                                    blank=True,
                                    related_name='albums')
    styles = models.ManyToManyField(Style,
                                    blank=True,
                                    related_name='albums')


class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.TimeField()
    position = models.IntegerField()
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='tracks')
