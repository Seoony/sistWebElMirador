from django.shortcuts import render, get_object_or_404
from socios.models import Socio
from terrenos.models import Terreno
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def registrar_socio(request):
  if request.method == 'GET':
    terrenos = Terreno.objects.all().order_by("nombre").filter(disponible=True)
    return render(request, 'registrar_socio.html', {'terrenos':terrenos})
  
  if request.method == 'POST':
    if not (request.POST['dni'].isnumeric() and len(request.POST['dni'])==8):
      terrenos = Terreno.objects.all().filter(disponible=True)
      return render(request, 'registrar_socio.html', {
        'terrenos':terrenos,
        'error':"DNI incorrectamente colocado, por favor coloque bien",
        'nombre':request.POST['nombres'],
        'primer_apellido':request.POST['primer_apellido'],
        'segundo_apellido':request.POST['segundo_apellido'],
        'dni':request.POST['dni'],
        'fecha_de_nacimiento':request.POST['fecha_de_nacimiento']})
    
    elif len(request.POST['nombres'])==0 or len(request.POST['primer_apellido'])==0 or len(request.POST['segundo_apellido'])==0:
      terrenos = Terreno.objects.all().filter(disponible=True)
      return render(request, 'registrar_socio.html', {
        'terrenos':terrenos,
        'error2':"Coloque correctamente los nombres y apellidos",
        'nombre':request.POST['nombres'],
        'primer_apellido':request.POST['primer_apellido'],
        'segundo_apellido':request.POST['segundo_apellido'],
        'dni':request.POST['dni'],
        'fecha_de_nacimiento':request.POST['fecha_de_nacimiento']})

    else:
      try:
        socio=Socio()
        socio.dni=request.POST['dni']
        socio.nombres=request.POST['nombres'].title()
        socio.primer_apellido=request.POST['primer_apellido'].title()
        socio.segundo_apellido=request.POST['segundo_apellido'].title()
        socio.fecha_de_nacimiento=request.POST['fecha_de_nacimiento']
        print("crea usuario")
        #socio = get_object_or_404(Socio, dni=request.POST['dni'])
        terreno = get_object_or_404(Terreno, nombre=request.POST['terreno'])
        socio.terreno = terreno
        socio.set_password(request.POST['dni'])
        socio.save()
        terreno.disponible=False
        terreno.save()
        
      except:
        terrenos = Terreno.objects.all().filter(disponible=True)
        return render(request, 'registrar_socio.html', {
          'terrenos':terrenos,
          'error2':"No se puede registrar",
          'nombre':request.POST['nombres'],
          'primer_apellido':request.POST['primer_apellido'],
          'segundo_apellido':request.POST['segundo_apellido'],
          'dni':request.POST['dni'],
          'fecha_de_nacimiento':request.POST['fecha_de_nacimiento']})
      
      else:
        if request.POST['boton']=="registrar":
          return HttpResponseRedirect(reverse('home'))