from django.contrib import admin
from .models import Feature, FeatureLike, FeatureComment
# Register your models here.
admin.site.register(Feature)
admin.site.register(FeatureLike)
admin.site.register(FeatureComment)