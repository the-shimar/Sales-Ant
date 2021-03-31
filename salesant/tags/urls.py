from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tags, name='tags'),
    path('generate', views.tagGenerate, name='taggenerate'),
    path('codedelete', views.tagCodeDelete, name='tagdeletecode'),
    path('<str:triggers_selected>/', views.tagsTrigger, name='tagsTrigger'),
    path('<str:triggers_selected>/<str:fortriggers_selected>', views.tagsForTrigger, name='tagsForTrigger'),
]