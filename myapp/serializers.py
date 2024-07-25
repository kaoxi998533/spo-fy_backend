from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile, Follower
from .models import Comment, Video, Like, Artist, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'artist_name', 'album']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'video']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'portrait_path',  'username']

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['user_from', 'user_to', 'created']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_followers(self, obj):
        followers = Follower.objects.filter(user_to=obj)
        return FollowerSerializer(followers, many=True).data

    def get_following(self, obj):
        following = Follower.objects.filter(user_from=obj)
        return FollowerSerializer(following, many=True).data

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        if validated_data.get('username'): 
            profile.username = validated_data.get('username', instance.username)
            profile.save()

        if validated_data.get('bio'):
            profile.bio = profile_data.get('bio', profile.bio)
            profile.save()

        return instance

class VideoSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    song = SongSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = ['id', 'song', 'user', 'title', 'likes_count', 'description', 'video_file', 'duration', 'created_at', 'comments', 'cover_image']

    def get_likes_count(self, obj):
        return Like.objects.filter(video=obj).count()
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Like
       fields = ['id', 'video', 'user', 'created_at']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'