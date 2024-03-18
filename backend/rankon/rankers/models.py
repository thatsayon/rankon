from django.db import models
from django.contrib.auth.models import User


class Ranker(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    full_name = models.CharField(max_length=120)
    facebook = models.URLField(max_length=200)
    image = models.ImageField(upload_to='image/')
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.full_name}"
