from django.db import models

# Create your models here.
class Tags(models.Model):
    trigger_name = models.CharField(primary_key=True,max_length=200, default='None')
    api_key = models.TextField(default='None')
    code = models.TextField(default='None')

    def __str__(self):
        return self.trigger_name
