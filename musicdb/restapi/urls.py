from django.conf.urls import include, url

from rest_framework import routers

from .views import AlbumArtViewSet, GenreViewSet, StyleViewSet, ArtistViewSet, AlbumViewSet, TrackViewSet


router = routers.DefaultRouter()
router.register(r'albumart', AlbumArtViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'style', StyleViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
