from django.contrib import admin
from .models import Evento, Items_de_evento, Asistencia, Cobro_de_multa
# Register your models here.
admin.site.register(Evento)
admin.site.register(Items_de_evento)
admin.site.register(Asistencia)
admin.site.register(Cobro_de_multa)