from django.conf.urls import url
from grocery.note.views import (note_detail, new_note)

urlpatterns = [
    url(r'^new/$', new_note, name='new_note'),
    url(r'^(?P<note_id>\d+)/$', note_detail,
        name='note_detail'),
]
