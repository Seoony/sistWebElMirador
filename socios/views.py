from django.shortcuts import render
from socios.models import Socio


def crear_socio(request):
  if request.method == 'GET':
    return render(request, 'crear_socio.html')
