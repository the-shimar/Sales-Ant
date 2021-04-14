from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.apiGenerate, name='apigenerate'),
    path('', views.apiManage, name='apimanage'),   
]