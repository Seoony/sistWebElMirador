from django.contrib import admin

# Register your models here.
from .models import Cuota_extra, Cuota_social, Pago_cuota

admin.site.register(Cuota_social)
admin.site.register(Cuota_extra)
admin.site.register(Pago_cuota)