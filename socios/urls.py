from socios.views import crear_socio
from django.urls import path

app_name = 'socios'
urlpatterns = [
    path('crear/', crear_socio, name='crear_socio'),
]
