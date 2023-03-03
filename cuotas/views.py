from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cuota_extra, Cuota_social
from django.shortcuts import render
def registrar_cuota_social(request):
  if request.method == 'GET':
    meses = Cuota_social.meses
    años = Cuota_social.years
    cuotas_s = Cuota_social.objects.all().order_by('nombre')
    return render(request, 'registrar_cuota_social.html',
                  {'meses':meses,'años':años, 'cuotas':cuotas_s})
  
  elif request.method == 'POST':
    try:
      cuota = Cuota_social()
      cuota.año = request.POST['año']
      cuota.mes = request.POST['mes']
      cuota.monto = request.POST['monto']
      cuota.nombre = request.POST['año'] + "/" + request.POST['mes']
      cuota.save()

    except:
      meses = Cuota_social.meses
      años = Cuota_social.years
      cuotas_s = Cuota_social.objects.all().order_by('nombre')
      return render(request, 'registrar_cuota_social.html', {
        'meses':meses,
        'años':años,
        'error': "Esta cuota social ya existe!",
        'cuotas':cuotas_s})

    else:
      if request.POST['boton']=="registrar":
        return HttpResponseRedirect(reverse('home'))
      elif request.POST['boton']=="registrar_y_añadir_otro":
        cuotas_s = Cuota_social.objects.all().order_by('nombre')
        meses = Cuota_social.meses
        años = Cuota_social.years
        return render(request, 'registrar_cuota_social.html', {
        'meses':meses,
        'años':años,
        'mensaje': "Cuota "+cuota.nombre+" registrado correctamente",
        'cuotas':cuotas_s})
      
def registrar_cuota_extra(request):
  if request.method == 'GET':
    cuotas_e = Cuota_extra.objects.all()
    return render(request, 'registrar_cuota_extra.html',
                  { 'cuotas':cuotas_e})
  
  elif request.method == 'POST':
    try:
      cuota = Cuota_extra()
      cuota.nombre = request.POST['nombre']
      cuota.fecha_vencimiento = request.POST['fecha_v']
      cuota.monto = request.POST['monto']
      cuota.descripcion = request.POST['descripcion']
      cuota.mora = request.POST['mora']
      cuota.save()

    except:
      
      cuotas_s = Cuota_extra.objects.all()
      return render(request, 'registrar_cuota_extra.html', {
        'error': "Esta cuota extra ya existe!",
        'cuotas':cuotas_s})

    else:
      if request.POST['boton']=="registrar":
        return HttpResponseRedirect(reverse('home'))
      elif request.POST['boton']=="registrar_y_añadir_otro":
        cuotas_s = Cuota_extra.objects.all()
        return render(request, 'registrar_cuota_extra.html', {
        'mensaje': cuota.nombre+" registrado correctamente",
        'cuotas':cuotas_s})