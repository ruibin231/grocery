from django.conf.urls import url
from grocery.properties import views

urlpatterns = [
    url(r'^add', views.categroy_add, name='categroy_add'),
    # url(r'^login/$', views.user_login),
]