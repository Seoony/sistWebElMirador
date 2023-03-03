from django.db import models
from socios.models import Socio

class Items_de_evento(models.Model):
  item = models.CharField(max_length=200)

class Evento(models.Model):
  EVENTOS=[
    ('AG', 'Asamblea General'),
    ('AE', 'Asamblea Extraordinaria'),
    ('FA', 'Faena'),
    ('RI', 'Reunión Informativa'),
    ('MP', 'Marcha Pacífica')
  ]
  tipo_de_evento = models.TextField(max_length=2, choices=EVENTOS)
  contenido = models.TextField()
  fecha = models.DateField()
  hora = models.TimeField()
  lugar = models.CharField(max_length=200)
  agenda = models.ManyToManyField(Items_de_evento)
  multa = models.PositiveSmallIntegerField()

class Asistencia(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True)
  socio = models.ForeignKey(Socio, on_delete=models.SET_NULL, null=True)
  exonerado = models.BooleanField(default=False)
  tardanza = models.BooleanField(default=False)

class Cobro_de_multa(models.Model):
  evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True)
  socio = models.ForeignKey(Socio, on_delete=models.SET_NULL, null=True)
  monto_cobrado = models.PositiveSmallIntegerField()
  fecha = models.DateField()