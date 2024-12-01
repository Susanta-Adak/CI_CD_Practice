from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    hobbies = models.TextField()

    def __str__(self):
        return self.name
