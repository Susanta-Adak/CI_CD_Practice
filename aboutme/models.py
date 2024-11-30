from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    hobbies = models.TextField()

    def __str__(self):
        return self.name
