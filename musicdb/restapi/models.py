from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Style(models.Model):
    name = models.CharField(max_length=50)


class Artist(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               related_name='albums')
    genres = models.ManyToManyField(Genre,
                                    blank=True,
                                    related_name='albums')
    styles = models.ManyToManyField(Style,
                                    blank=True,
                                    related_name='albums')


class AlbumArt(models.Model):
    image = models.ImageField(upload_to='album_art')
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='album_art')


class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.TimeField()
    position = models.CharField(max_length=3)
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='tracks')
