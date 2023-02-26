from django.db import models

# Create your models here.
class Terreno(models.Model):
  manzanas=[
    ('A', 'Mz A, no existe'),
    ('B', 'Mz B'),
    ('G', 'Mz G'),
    ('H', 'Mz H'),
    ('H\'', 'Mz H prima'),
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
  
  nombre = models.CharField(max_length=4, unique=True)
  manzana = models.CharField(max_length=2, choices=manzanas)
  lote = models.CharField(max_length=2)
  area = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  riesgo = models.BooleanField(default=False)
  otros_usos = models.BooleanField(default=False)
  vivencia = models.BooleanField(default=False)
  observaciones = models.TextField(default="Ninguna")
  disponible = models.BooleanField(default=True)
  est_reg = models.BooleanField(default=True)

  def __str__(self):
    return self.manzana +" - "+ self.lote

