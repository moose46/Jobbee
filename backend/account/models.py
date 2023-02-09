from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )
    # FIXME UserProfile
    # resume = models.FileField(null=True)
    resume = models.CharField(max_length=100, null=True)
