from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.builder, name='build'),
    path('savebuild', views.saveBuildJS, name='savebuild'),
    path('builds', views.allBuilds, name='builds'),
    path('builddelete', views.buildDelete, name='builddelete'),
    path('templates_made', views.templates_made, name='templates_made'),
]