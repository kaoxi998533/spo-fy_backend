from django.urls import path
from .views import *

urlpatterns = [
    path('decompose/to_vocals', decompose_to_vocals),
    path('decompose/to_drums', decompose_to_drums),
    path('decompose/to_bass', decompose_to_bass),
    path('decompose/to_others', decompose_to_others),
    path('get_song/<int:index>/<int:song_id>', get_song),
]

