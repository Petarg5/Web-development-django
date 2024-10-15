from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username