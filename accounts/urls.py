from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import registration, logout
from accounts import url_reset
 

urlpatterns = [
    url(r'^register/', registration, name="registration"),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html') , name='user-login' ),
    url(r'^logout/', logout, name="logout"),
    url(r'^password-reset/', include(url_reset)),
    
   
]