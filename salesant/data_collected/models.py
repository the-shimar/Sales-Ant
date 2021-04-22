from django.db import models

# Create your models here.
class YNF_Form_List(models.Model):
    user = models.CharField(max_length=200, default='BuildUser')
    website = models.CharField(max_length=200, default='Website')
    trigger_name = models.CharField(max_length=200, default='trigger_name')
    collected_email = models.CharField(max_length=200, default='collected_email')

    def __str__(self):
        return self.collected_email

class DC_mail_user(models.Model):
    user = models.CharField(max_length=200, default='BuildUser')
    name = models.CharField(max_length=200, default='BuildUser')
    subject = models.CharField(max_length=200, default='BuildUser')
    date = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=200, default='Website')
    trigger_name = models.CharField(max_length=200, default='trigger_name')
    message = models.TextField(default='None')
    promo_code = models.TextField(default='None')

    def __str__(self):
        return self.trigger_name

class DC_new_subscriber(models.Model):
    user = models.CharField(max_length=200, default='BuildUser')
    subject = models.CharField(max_length=200, default='BuildUser')
    date = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=200, default='Website')
    trigger_name = models.CharField(max_length=200, default='trigger_name')
    message = models.TextField(default='None')
    promo_code = models.TextField(default='None')

    def __str__(self):
        return self.trigger_name
