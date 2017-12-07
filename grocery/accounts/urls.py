#encoding:utf-8

from django.conf.urls import url
from grocery.accounts import views



urlpatterns = [
    url(r'^create/$', views.create_user),
    url(r'^login/$', views.user_login),
]