import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profile_pictures/', default ='profile_pictures/user_default.png')
    social_twitter = models.CharField(max_length=500, blank=True, null=True)
    social_github = models.CharField(max_length=500, blank=True, null=True)
    social_youtube = models.CharField(max_length=500, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user.username)


class skill(models.Model):
    owner = models.ForeignKey(profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)


