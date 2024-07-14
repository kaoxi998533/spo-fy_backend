from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    portrait_path = models.TextField(max_length=255,)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance)

models.signals.post_save.connect(create_profile, sender=User)


class Follower(models.Model):
    user_from = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to')

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
