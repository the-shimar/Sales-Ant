from django.contrib import admin
from .models import Subscription, Apikey

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Apikey)