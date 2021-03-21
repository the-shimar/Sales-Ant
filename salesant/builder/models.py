from django.db import models

# Create your models here.
class Build(models.Model):
    user = models.CharField(max_length=200, default='BuildUser')
    build_name = models.CharField(max_length=200, default='BuildName')
    build = models.TextField(default='<h1>Hi!<h1>')

    def __str__(self):
        return self.build_name
