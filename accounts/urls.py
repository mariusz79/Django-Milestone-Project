from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from accounts.views import registration

urlpatterns = [
     
    url(r'^register/', registration, name="registration"),
   
]