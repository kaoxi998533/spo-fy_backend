from django.urls import path
from .views import *

urlpatterns = [
    path('decompose/to_vocals/<song_id>', decompose_to_vocals),
    path('decompose/to_drums/<song_id>', decompose_to_drums),
    path('decompose/to_bass/<song_id>', decompose_to_bass),
    path('decompose/to_others/<song_id>', decompose_to_others),
    path('get_song/<index>/<song_id>', get_song),
]

