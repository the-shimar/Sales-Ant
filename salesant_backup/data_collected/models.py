from django.db import models

# Create your models here.
class YNF_Form_List(models.Model):
    user = models.CharField(max_length=200, default='BuildUser')
    trigger_name = models.CharField(max_length=200, default='trigger_name')
    collected_email = models.CharField(max_length=200, default='collected_email')

    def __str__(self):
        return self.collected_email