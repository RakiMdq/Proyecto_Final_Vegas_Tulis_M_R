from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import Blogs, EditarPublicacion, Comentario

# Create your views here.

def listar_publicaciones(request):
    publicaciones = Blogs.objects.all()
    if publicaciones:
        context = {'publicaciones': Blogs}
    else:
        mensaje = 'No hay publicaciones creadas.'
        context = {'mensaje': mensaje}
    return render(request, 'blog/lista_publicaciones.html', context)

def detallar_publicacion(request, pk):
    publicacion = get_object_or_404(Blogs, pk=pk)
    creador = publicacion.creador
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion, 'creador': creador})