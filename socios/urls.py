from socios.views import registrar_socio, iniciar_sesion, cerrar_sesion
from django.urls import path

app_name = 'socios'
urlpatterns = [
    path('registrar/', registrar_socio, name='registrar_socio'),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]
