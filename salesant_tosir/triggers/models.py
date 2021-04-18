from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Triggers(models.Model):
    trigger_type = models.CharField(primary_key=True, max_length=200, default='None')
    js_file = models.FileField(upload_to='triggers/')
    css_file = models.FileField(upload_to='triggers/')

    def __str__(self):
        return self.trigger_type

class UserTriggers(models.Model):
    name = models.CharField(primary_key=True, max_length=200, default='None')
    user = models.CharField(max_length=200, default='None')
    # trigger_type = ForeignKey(Triggers, on_delete=models.CASCADE)
    # build = ForeignKey('builder.Build', on_delete=models.CASCADE)
    trigger_type = models.CharField(max_length=200, default='None')
    build = models.CharField(max_length=200, default='None')
    limit = models.IntegerField(default='10')
    website = models.CharField(max_length=200, default='None')
    STATUS_OPTIONS = [
        ('EN', 'Enable'),
        ('DS', 'Disable'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_OPTIONS, default='EN')

    def __str__(self):
        return self.name
