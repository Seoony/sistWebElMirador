from .views import registrar_cuota_social, registrar_cuota_extra
from django.urls import path

app_name = 'cuotas'
urlpatterns = [
    path('registrar_cuota_social/', registrar_cuota_social, name='registrar_cuota_social'),
    path('registrar_cuota_extra/', registrar_cuota_extra, name='registrar_cuota_extra'),
]