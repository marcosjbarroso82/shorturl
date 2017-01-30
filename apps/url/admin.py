from django.contrib import admin
from .models import ShortUrl, DeviceUrl


class UrlModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShortUrl, UrlModelAdmin)
admin.site.register(DeviceUrl, admin.ModelAdmin)