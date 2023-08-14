from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Blogs(models.Model):
    titulo= models.CharField(max_length=255)
    slog = models.SlugField(unique=True)
    subtitulo= models.CharField(max_length=255)
    contenido = models.TextField()
    
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='publicaciones/')
    

    def __str__(self):
        return self.titulo

class EditarPublicacion(models.Model):
    publicacion = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    contenido = models.TextField(blank=True, null=True)
    fecha_edicion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.publicacion.titulo} - {self.fecha_edicion}'

class Comentario(models.Model):
    publicacion = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de '{self.autor.username}' en '{self.publicacion.titulo}'"