from django.conf.urls import url
from .views import index, stats



urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^home/$',index, name='home'),
    url(r'^home/stats/$',stats, name='stats'),
]