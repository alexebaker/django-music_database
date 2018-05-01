from rest_framework import serializers

from .models import AlbumArt, Genre, Style, Artist, Album, Track


class AlbumArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArt
        fields = ('id', 'image', 'album')


class GenreSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True,
                                                read_only=True,
                                                allow_null=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'albums')


class StyleSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True,
                                                read_only=True,
                                                allow_null=True)

    class Meta:
        model = Style
        fields = ('id', 'name', 'albums')


class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True,
                                                read_only=True,
                                                allow_null=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True,
                             read_only=True,
                             allow_null=True)
    album_art = AlbumArtSerializer(many=True,
                                   read_only=True,
                                   allow_null=True)
    genres = serializers.SlugRelatedField(many=True,
                                          allow_null=True,
                                          slug_field='name',
                                          queryset=Genre.objects.all())
    styles = serializers.SlugRelatedField(many=True,
                                          allow_null=True,
                                          slug_field='name',
                                          queryset=Style.objects.all())

    class Meta:
        model = Album
        fields = ('id', 'title', 'year', 'artist', 'genres', 'styles', 'tracks', 'album_art')

