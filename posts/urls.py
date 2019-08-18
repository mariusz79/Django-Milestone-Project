from django.conf.urls import url
from .views import  create_post



urlpatterns = [
  
    url(r'^new/$', create_post, name='new_post'),
     
]