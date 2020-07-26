from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(max_length=5000)
    author = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="set_author", default = 1, on_delete = models.CASCADE)
    