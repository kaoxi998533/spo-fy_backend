from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, LikeViewSet, UserViewSet, FollowerViewSet


router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'followers', FollowerViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('decompose/to_vocals/<song_id>', decompose_to_vocals),
    path('decompose/to_drums/<song_id>', decompose_to_drums),
    path('decompose/to_bass/<song_id>', decompose_to_bass),
    path('decompose/to_others/<song_id>', decompose_to_others),
    path('get_song/<index>/<song_id>', get_song),
    path('get_album_cover/<album_id>', get_album_cover),
    path('db/load_from_database/<type>', load_from_database),
    path('', include(router.urls))
]

