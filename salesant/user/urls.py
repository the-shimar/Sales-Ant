from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('profile', views.profile_view, name='profile'),
    path('purchase_domain', views.purchase_domain, name='purchase_domain'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),

]