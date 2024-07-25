from django.contrib.auth.models import User
from myapp.models import Song, Video
from django.core.files import File

# Assuming you have a Song instance and a User instance
song = Song.objects.get(id=3)  # Replace with the actual song ID
user = User.objects.get(id=23)  # Replace with the actual user ID

# Create the Video instance
video = Video(
    song=song,
    user=user,
    title="My Awesome Video",
    description="This is a great video of my favorite song!",
    duration=180,  # Duration in seconds
)

# Add the video file
with open('/home/parallels/myproject/file_example_MP4_640_3MG.mp4', 'rb') as video_file:
    video.video_file.save('my_video.mp4', File(video_file), save=False)

# Add the cover image
with open('/home/parallels/myproject/—Pngtree—hand painted chinese style golden_5460413.png', 'rb') as image_file:
    video.cover_image.save('cover_image.jpg', File(image_file), save=False)

# Save the Video instance to the database
video.save()