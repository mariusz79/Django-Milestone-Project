from django.contrib import admin
from .models import Bug, BugLike, BugComment
# Register your models here.
admin.site.register(Bug)
admin.site.register(BugLike)
admin.site.register(BugComment)