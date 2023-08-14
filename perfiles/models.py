from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='profile_photos', blank=True)

    def __str__(self):
        return self.usuario.username
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    foto = models.ImageField(upload_to='avatars/', default='usuarios/img/fotodeperfil.jpg')