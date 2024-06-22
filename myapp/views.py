import os
import demucs.separate
import shlex
import tempfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
import logging

# Configure logging
logger = logging.getLogger(__name__)

def decompose(request, dest_track_type):
    try:
        if 'file' not in request.FILES:
            return Response({'error': 'No file uploaded'}, status=400)

        file = request.FILES['file']
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_input:
            for chunk in file.chunks():
                temp_input.write(chunk)
            temp_input_path = temp_input.name

        output_dir = tempfile.mkdtemp()
        demucs_command = f'--mp3 --two-stems {dest_track_type} -o {output_dir} -n htdemucs {temp_input_path}'
        demucs.separate.main(shlex.split(demucs_command))

        logger.info(f"Contents of the output directory: {os.listdir(output_dir)}")

        track_path = os.path.join(output_dir, 'htdemucs', os.path.basename(temp_input_path).replace('.mp3', ''), f'{dest_track_type}.mp3')

        if os.path.exists(track_path):
            response = FileResponse(open(track_path, 'rb'), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{dest_track_type}.mp3"'

            # Clean up the temporary files
            os.remove(track_path)
            os.remove(temp_input_path)

            return response
        else:
            logger.error(f"Vocal path not found: {track_path}")
            return Response({'error': 'Decomposition failed'}, status=500)

    except Exception as e:
        logger.exception("An error occurred during decomposition")
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def decompose_to_vocals(request): 
    return decompose(request, 'vocals')

@api_view(['POST'])
def decompose_to_bass(request):
    return decompose(request, 'bass')

@api_view(['POST'])
def decompose_to_drums(request):
    return decompose(request, 'drums')

@api_view(['POST'])
def decompose_to_others(request):
    return decompose(request, 'others')
