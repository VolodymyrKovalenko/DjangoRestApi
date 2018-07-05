from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=60)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

    def __str__(self):

        return f"{self.title} {self.author}"
