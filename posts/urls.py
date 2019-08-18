from django.conf.urls import url
from .views import  create_post, post_detail, liking, edit_post, sort_by



urlpatterns = [
    url(r'^$', sort_by, name='sort_by'),
    url(r'^new/$', create_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/like$', liking, name='liking_post'),
]