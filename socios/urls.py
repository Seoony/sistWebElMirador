from socios.views import registrar_socio
from django.urls import path

app_name = 'socios'
urlpatterns = [
    path('registrar/', registrar_socio, name='registrar_socio'),
]
