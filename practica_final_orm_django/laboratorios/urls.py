from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('listar/', listar_laboratorios, name='listar_laboratorios'),
    path('crear/', crear_laboratorio, name='crear_laboratorio'),
    path('ver/<int:pk>/', ver_laboratorio, name='ver_laboratorio'),
    path('editar/<int:pk>/', editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:pk>/',eliminar_laboratorio, name='eliminar_laboratorio'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('catalogo/',catalogo_productos,name="catalogo")
]