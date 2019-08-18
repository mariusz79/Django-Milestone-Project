from django.conf.urls import url
from .views import bug_detail, create_bug, edit_bug, liking_bug, sort_bugs



urlpatterns = [
    url(r'^$', sort_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^(?P<pk>\d+)/like$', liking_bug, name='liking_bug'),
    url(r'^new/$', create_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', edit_bug, name='edit_bug')
]