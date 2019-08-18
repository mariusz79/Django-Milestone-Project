from django.conf.urls import url, include
from accounts.views import logout, registration, user_profile, other_user_profile
from accounts import url_reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html') , name='user-login' ),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^profiles/(?P<username>[\w\-]+)/$', other_user_profile, name="other_user_profile"),
    url(r'^password-reset/', include(url_reset))
]