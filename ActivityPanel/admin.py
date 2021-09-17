from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['login_no', 'user_id', 'webiste_id', 'ip', 'city',
                    'state', 'country', 'date_time', 'security_status', 'medium']


# Register your models here.
