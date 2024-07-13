from django.db import models

# Create your models here.
class TmpUser(models.Model):
    email = models.EmailField(verbose_name='email', unique=True)
    verification_code = models.TextField(verbose_name='verification_code', max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(verbose_name='is_verified', default=False)

