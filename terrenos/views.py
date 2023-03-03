from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Terreno
from django.shortcuts import render
def registrar_terreno(request):
  if request.method == 'GET':
    manzanas = Terreno.manzanas
    terrenos = Terreno.objects.all().order_by('nombre')
    return render(
      request, 'registrar_terreno.html', {
      'manzanas':manzanas,
      'terrenos':terrenos})
  
  elif request.method == 'POST':
    try:
      terreno = Terreno()
      terreno.manzana = request.POST['manzana']
      terreno.lote = request.POST['lote']
      if len(request.POST['lote'])==2:
        terreno.nombre = request.POST['manzana'] + request.POST['lote']
      else:
        terreno.nombre = request.POST['manzana'] + "0" + request.POST['lote']
      terreno.save()

    except:
      manzanas = Terreno.manzanas
      terrenos = Terreno.objects.all().order_by('nombre')
      return render(request, 'registrar_terreno.html', {
        'manzanas':manzanas,
        'error': "Ese terreno ya existe!",
        'terrenos':terrenos})

    else:
      if request.POST['boton']=="registrar":
        return HttpResponseRedirect(reverse('home'))
      elif request.POST['boton']=="registrar_y_añadir_otro":
        terrenos = Terreno.objects.all().order_by('nombre')
        manzanas = Terreno.manzanas
        return render(request, 'registrar_terreno.html', {
        'manzanas':manzanas,
        'mensaje': "Terreno "+terreno.nombre+" registrado correctamente",
        'terrenos':terrenos})
