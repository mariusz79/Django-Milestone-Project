from django.conf.urls import url
from .views import donate, charge

urlpatterns = [
    url(r'^donate/$', donate, name='donate'),
    url(r'^charge/$', charge, name='charge'), 
]