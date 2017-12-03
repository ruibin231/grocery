from django.conf.urls import url
from grocery.property.views import home

urlpatterns = [
    url(r'^$', new_note, name='home'),
]