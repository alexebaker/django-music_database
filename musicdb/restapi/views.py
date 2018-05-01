from .serializers import AlbumArtSerializer, GenreSerializer, StyleSerializer, ArtistSerializer, AlbumSerializer, TrackSerializer
from .models import AlbumArt, Genre, Style, Artist, Album, Track

from rest_framework.viewsets import ModelViewSet


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


class TrackViewSet(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
