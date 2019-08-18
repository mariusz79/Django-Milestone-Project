from django.conf.urls import url
from features.views import feature_detail, create_feature, edit_feature, liking_feature, sort_features

urlpatterns = [
    url(r'^$', sort_features, name='get_features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^(?P<pk>\d+)/like$', liking_feature, name='liking_feature'),
    url(r'^new/$', create_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', edit_feature, name='edit_feature')
]
