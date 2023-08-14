from django.db import models


# Create your models here.

class Perfil(models.Model):
    username =models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.username}, {self.apellido}, {self.nombre}"