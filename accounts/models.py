from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
