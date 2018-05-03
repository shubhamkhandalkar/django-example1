from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'login/$', views.user_login, name='login'),
    url(r'^special/$', views.special, name='special'),
]
