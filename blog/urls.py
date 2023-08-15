from django.urls import path, include
from blog.views import listar_publicaciones, detallar_publicacion

urlpatterns = [

    path("publicaciones/", listar_publicaciones),
    path("detalle/", detallar_publicacion),

]