from .views import registrar_terreno
from django.urls import path

app_name = 'terrenos'
urlpatterns = [
    path('registrar/', registrar_terreno, name='registrar_terreno'),
]
