from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomSocioManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, dni, nombres=None, primer_apellido=None, segundo_apellido=None, fecha_de_nacimiento=None, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not dni or len(dni)!=8:
            raise ValueError(_('Introduce el DNI correctamente'))
        try:
          dni_int = int(dni)
          socio = self.model(
            dni=dni, nombres=nombres, 
            primer_apellido=primer_apellido, 
            segundo_apellido=segundo_apellido, 
            fecha_de_nacimiento=fecha_de_nacimiento, **extra_fields)
          socio.set_password(password)
          socio.save()
          return socio
        
        except ValueError:
          raise ValueError(_('El DNI debe contener solo números.'))

    def create_superuser(self, dni, nombres, primer_apellido, segundo_apellido, fecha_de_nacimiento, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(dni, nombres, primer_apellido, segundo_apellido, fecha_de_nacimiento, password, **extra_fields)