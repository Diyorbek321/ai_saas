from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.IntegerField()
    bio = models.TextField()
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=50)


class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"


class GeneratedCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    title = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, default='python')  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title or 'Untitled Code'}"
