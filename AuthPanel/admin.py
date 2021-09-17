from django.contrib import admin

from .models import PassitUser, User, WebsiteOwner


# Register your models here.
admin.site.register(User)
admin.site.register(PassitUser)
admin.site.register(WebsiteOwner)