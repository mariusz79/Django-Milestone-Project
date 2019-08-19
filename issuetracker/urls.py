"""issuetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import urls as home_urls
from accounts import urls as accounts_urls
from posts import urls as posts_urls
from bugs import urls as bugs_urls
from features import urls as features_urls
from contact import urls as contact_urls
from django.views.static import serve
from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^posts/', include(posts_urls)),
    url(r'^bugs/', include(bugs_urls)),
    url(r'^features/', include(features_urls)),
    url(r'^contact/', include(contact_urls)),
]
