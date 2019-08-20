from django.conf.urls import url
from .views import search, search_results

urlpatterns = [
    url(r'^$', search_results, name='search'),
    url(r'^results/$', search, name='search_results'),
]