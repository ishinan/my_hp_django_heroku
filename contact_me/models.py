from django.db import models
from django.utils import timezone

# Create your models here.
class ContactMeMessage(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=120)
        message = models.TextField()
        created_datetime = models.DateTimeField(default=timezone.now)