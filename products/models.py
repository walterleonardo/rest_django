from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    title       = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image       = models.CharField(max_length=1000, blank=True, null=True, default='/static/no_image.png')
    updated     = models.DateTimeField(auto_now=True)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File title: {self.title}"