from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.dc, name='dc_index'),
    path('fny_f', views.dc_ynf, name='ynf_f'),
]