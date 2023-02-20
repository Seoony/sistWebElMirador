from django.db import models
from django.utils import timezone
from .managers import CustomSocioManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Socio(AbstractBaseUser, PermissionsMixin):
  dni = models.CharField(max_length=8, unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  fecha_de_ingreso = models.DateTimeField(default=timezone.now)
  nombres = models.CharField(max_length=63)
  primer_apellido = models.CharField(max_length=31)
  segundo_apellido = models.CharField(max_length=31)
  celular = models.CharField(max_length=9, null=True)
  vivencia = models.BooleanField(default=False)
  fecha_de_nacimiento = models.DateField()
  agua = models.BooleanField(default=False)
  luz = models.BooleanField(default=False)

  USERNAME_FIELD = 'dni'
  REQUIRED_FIELDS = ['nombres', 'primer_apellido', 'segundo_apellido', 'fecha_de_nacimiento']

  objects = CustomSocioManager()

  def __str__(self):
    return self.nombres +" "+ self.primer_apellido