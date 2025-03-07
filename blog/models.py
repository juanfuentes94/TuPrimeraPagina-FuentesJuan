from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
