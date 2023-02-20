from django.contrib import admin

# Register your models here.
from .models import cuota_extra, cuota_social

admin.site.register(cuota_social)
admin.site.register(cuota_extra)