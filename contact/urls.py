from django.conf.urls import url
from .views import contact, contact_success

urlpatterns = [
    url(r'^$', contact, name='contact'),
    url(r'^success/$', contact_success, name='contact_success'),
]