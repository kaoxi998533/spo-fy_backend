from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile, Follower
from .models import Comment, Video, Like

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'video']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date']

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
        fields = ['id', 'username', 'email', 'profile', 'followers', 'following']

    # these two functions below might not be necessary
    def get_followers(self, obj):
        followers = Follower.objects.filter(user_to=obj)
        return FollowerSerializer(followers, many=True).data

    def get_following(self, obj):
        following = Follower.objects.filter(user_from=obj)
        return FollowerSerializer(following, many=True).data

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.bio = profile_data.get('bio', profile.bio)
        profile.save()

        return instance

class VideoSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = ['id', 'song', 'user', 'title', 'description', 'video_path', 'duration', 'likes', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Like
       fields = ['id', 'video', 'user', 'created_at']