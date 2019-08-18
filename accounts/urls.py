from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from accounts.views import registration
from .views import logout
 

urlpatterns = [
    url(r'^register/', registration, name="registration"),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html') , name='user-login' ),
    url(r'^logout/', logout, name="logout"),
    
   
]