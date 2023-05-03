from django.db import models
from datetime import date
from socios.models import Socio

# Create your models here.
class Cuota_social(models.Model):
  meses = [
    ('01', 'Enero'),
    ('02', 'Febrero'),
    ('03', 'Marzo'),
    ('04', 'Abril'),
    ('05', 'Mayo'),
    ('06', 'Junio'),
    ('07', 'Julio'),
    ('08', 'Agosto'),
    ('09', 'Setiembre'),
    ('10', 'Octubre'),
    ('11', 'Noviembre'),
    ('12', 'Diciembre'),
  ]
  years = [
    ('2020', 2020),
    ('2021', 2021),
    ('2022', 2022),
    ('2023', 2023),
    ('2024', 2024),
    ('2025', 2025),
  ]
  nombre = models.CharField(max_length=7, unique=True)
  mes = models.CharField(max_length=2, choices=meses)
  año = models.CharField(max_length=4, choices=years, default=('2023'))
  monto = models.PositiveSmallIntegerField(default=10)
  est_reg = models.BooleanField(default=True)

  def __str__(self):
    return self.mes +" - "+ self.año

class Cuota_extra(models.Model):
  monto = models.DecimalField(max_digits=5, decimal_places=2)
  nombre = models.CharField(max_length=64, default="Cuota extraordinaria para ", unique=True)
  descripcion = models.TextField()
  fecha_creacion = models.DateField(default=date.today)
  fecha_vencimiento = models.DateField()
  mora = models.DecimalField(max_digits=5, decimal_places=2)
  est_reg = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre
  
class Pago_cuota(models.Model):
  TIPO = [
    ('CS', 'Cuota Social'),
    ('CE', 'Cuota Extra'),
  ]
  tipo_de_cuota = models.CharField(max_length=2, choices=TIPO)
  cod_cuota = models.PositiveSmallIntegerField()
  #cuota_social = models.ForeignKey(Cuota_social, on_delete=models.SET_NULL, null=True)
  socio = models.ForeignKey(Socio, on_delete=models.SET_NULL, null=True)
  monto_cobrado = models.SmallIntegerField()
  fecha = models.DateField()
  recibo = models.CharField(max_length=10)
  exonerado = models.BooleanField(default=False)

class Ingreso_extra(models.Model):
  nombre = models.CharField(max_length=120)
  descripcion = models.TextField()
  monto = models.PositiveIntegerField()
  fecha = models.DateField()

class Egreso(models.Model):
  nombre = models.CharField(max_length=120)
  descripcion = models.TextField()
  monto = models.PositiveIntegerField()
  fecha = models.DateField()