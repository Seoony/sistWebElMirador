from django.db import models
from socios.models import Socio

# Create your models here.
class Terreno(models.Model):
  manzanas=[
    ('G', 'Mz G'),
    ('H', 'Mz H'),
    ('h', 'Mz H prima'),
    ('I', 'Mz I'),
    ('J', 'Mz J'),
    ('K', 'Mz K'),
    ('M', 'Mz M'),
    ('Ñ', 'Mz Ñ'),
    ('O', 'Mz O'),
    ('P', 'Mz P'),
    ('Q', 'Mz Q'),
    ('R', 'Mz R'),
    ('S', 'Mz S'),
    ('T', 'Mz T'),
    ('U', 'Mz U'),
    ('V', 'Mz V'),
    ('X', 'Mz X'),
  ]
  def get_default_socio():
    return Socio.objects.get(dni="12345678")
  manzana = models.CharField(max_length=1, choices=manzanas)
  lote = models.CharField(max_length=2)
  area = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  propietario = models.ForeignKey(
    Socio,
    default=get_default_socio,
    on_delete=models.SET_DEFAULT)
  riesgo = models.BooleanField(default=False)
  otros_usos = models.BooleanField(default=False)
  vivencia = models.BooleanField(default=False)
  observaciones = models.TextField(default="Ninguna")

  est_reg = models.BooleanField(default=True)

  def __str__(self):
    return self.manzana +" - "+ self.lote

