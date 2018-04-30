from rest_framework import serializers

from .models import AlbumArt, Genre, Style, Artist, Album, Track


class AlbumArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumArt
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
