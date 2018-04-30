import os

from .serializers import AlbumArtSerializer, GenreSerializer, StyleSerializer, ArtistSerializer, AlbumSerializer, TrackSerializer
from .models import AlbumArt, Genre, Style, Artist, Album, Track

from django.http import HttpResponse

from wsgiref.util import FileWrapper

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action


class AlbumArtViewSet(ModelViewSet):
    serializer_class = AlbumArtSerializer
    queryset = AlbumArt.objects.all()


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class StyleViewSet(ModelViewSet):
    serializer_class = StyleSerializer
    queryset = Style.objects.all()


class ArtistViewSet(ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    @action(detail=True,
            methods=['post', 'put'],
            parser_classes=(FileUploadParser,))
    def upload(self, request, pk=None):
        album = Album.objects.get(pk=pk)
        album.album_art.create(image=request.FILES['file'])
        album.save()
        return Response()

    @action(detail=True,
            methods=['get'])
    def download(self, request, pk=None):
        album = Album.objects.get(pk=pk)
        filename = os.path.basename(album.album_art.name)
        response = HttpResponse(FileWrapper(album.album_art),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = 'atachment; filename=%s' % filename
        return response


class TrackViewSet(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
