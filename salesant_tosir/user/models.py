from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Domains(models.Model):
    website = models.CharField(primary_key=True, max_length=200, default='None')
    username = models.CharField(max_length=200, default='None')
    plan = models.CharField(max_length=50, default='Free')

    def __str__(self):
        return self.website
