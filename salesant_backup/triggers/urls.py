from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.newTrigger, name='newTrigger'),
    path('manage/', views.manageTriggers, name='manageTriggers'),
    path('triggerdelete', views.triggerDelete, name='triggerdelete'),
]