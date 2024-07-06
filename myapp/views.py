import os
import demucs.separate
import shlex
import tempfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse, HttpResponseNotFound
import logging
from django.http import JsonResponse
from .models import *
import random

# Configure logging
logger = logging.getLogger(__name__)

def decompose(request, dest_track_type, song_id):
    try:
        # if 'file' not in request.FILES:
        #    return Response({'error': 'No file uploaded'}, status=400)

        #file = request.FILES['file']
        #with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_input:
        #    for chunk in file.chunks():
        #        temp_input.write(chunk)
        #    temp_input_path = temp_input.name

        formatted_id = str(song_id).zfill(6)
        directory = formatted_id[:3]
        file_path = "music/songs/{}/{:06}.mp3".format(directory, song_id)
        output_dir = tempfile.mkdtemp()
        demucs_command = f'--mp3 --two-stems {dest_track_type} -o {output_dir} -n htdemucs {file_path}'
        demucs.separate.main(shlex.split(demucs_command))

        logger.info(f"Contents of the output directory: {os.listdir(output_dir)}")

        track_path = os.path.join(output_dir, 'htdemucs', os.path.basename(file_path).replace('.mp3', ''), f'{dest_track_type}.mp3')

        if os.path.exists(track_path):
            response = FileResponse(open(track_path, 'rb'), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{dest_track_type}.mp3"'

            # Clean up the temporary files
            os.remove(track_path)

            return response
        else:
            logger.error(f"Vocal path not found: {track_path}")
            return Response({'error': 'Decomposition failed'}, status=500)

    except Exception as e:
        logger.exception("An error occurred during decomposition")
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def decompose_to_vocals(request, song_id): 
    return decompose(request, 'vocals', song_id)

@api_view(['POST'])
def decompose_to_bass(request, song_id):
    return decompose(request, 'bass', song_id)

@api_view(['POST'])
def decompose_to_drums(request, song_id):
    return decompose(request, 'drums', song_id)

@api_view(['POST'])
def decompose_to_others(request, song_id):
    return decompose(request, 'others', song_id)

@api_view(['POST'])
def get_song(request, index, song_id):
    song_path = f'music/songs/{index}/{song_id}.mp3'
    if(os.path.exists(song_path)):
        return FileResponse(open(song_path, 'rb'), content_type='audio/mpeg')
    else:
        return HttpResponseNotFound('File not found')

@api_view(['GET'])
def get_album_cover(request, album_id):
    album_path = f'album_covers/{album_id}.jpg'
    if(os.path.exists(album_path)):
        return FileResponse(open(album_path, 'rb'), content_type='image/jpeg')
    else:
        return HttpResponseNotFound('File not found')

@api_view(['GET'])
def load_from_database(request, type):
    try:
        if type == 'albums':
            albums = Album.objects.all().values('name', 'album_id', 'artist_name')
            data = [{"name": album["name"], "album_id": album["album_id"], "artist_name": album["artist_name"]} for album in albums]
            return JsonResponse(data, safe=False)
        
        elif type == 'artists':
            artist_names = Song.objects.values_list('artist_name', flat=True).distinct()
            data = [{"artist_name": name} for name in artist_names]
            return JsonResponse(data, safe=False)
        
        elif type == 'songs':
            songs = Song.objects.all().values('song_id', 'duration', 'name', 'album_id', 'artist_name')
            data = [{'song_id': song['song_id'], 'duration': song['duration'], 'name': song['name'], 
                     'album_id': song['album_id'], 'artist_name' : song['artist_name']} for song in songs]
            return JsonResponse(data, safe=False)
        
        else:
            return JsonResponse({"error": "Invalid type parameter"}, status=400)
    
    except Exception as e:
        print(str(e))
        return JsonResponse({"error": str(e)}, status=500)

