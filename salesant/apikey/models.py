from django.db import models
from django.contrib.auth.models import User
import secrets


# Create your models here.
class Subscription(models.Model):
    user = models.CharField(max_length=200, default='None')
    website = models.CharField(primary_key=True,max_length=200, default='None')

    def __str__(self):
        return self.website

class Apikey(models.Model):
    user = models.CharField(max_length=200, default='None')
    key_name = models.CharField(primary_key=True,max_length=200, default='None')
    website = models.CharField(max_length=200, default='None')
    key = models.TextField(default=secrets.token_urlsafe(18))

    def __str__(self):
        return self.key_name
