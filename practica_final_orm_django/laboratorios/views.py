from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import LaboratorioForm
from django.conf import settings
import os

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Ruta de la carpeta de imágenes de productos
    carpeta_imagenes = os.path.join('laboratorios', 'static', 'image')

    # Asignar una imagen según el ID del producto
    nombre_imagen = f"{producto_id}.jpg"  # o .png según el formato de tus imágenes
    ruta_imagen = os.path.join(carpeta_imagenes, nombre_imagen)
    
    # Verificar si la imagen existe antes de asignarla al producto
    if os.path.exists(ruta_imagen):
        producto.imagen_ruta = ruta_imagen
    else:
        # Si la imagen no existe, asignar una imagen predeterminada
        producto.imagen_ruta = os.path.join(carpeta_imagenes, 'default.jpg')

    return render(request, 'detalle_producto.html', {'producto': producto})



def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar_laboratorios.html', {'laboratorios': laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm()

    return render(request, 'crear_laboratorio.html', {'form': form})

def ver_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'ver_laboratorio.html', {'laboratorio': laboratorio})

def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('ver_laboratorio', pk=laboratorio.pk)
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form, 'laboratorio': laboratorio})

def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('listar_laboratorios')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})

def index(request):

    return render(request,'index.html')


def catalogo_productos(request):
    productos = Producto.objects.all()
    fotos_productos = {}
    for i, producto in enumerate(productos):
        fotos_productos[producto] = f'image/{i + 1}.jpg'
    return render(request, 'catalogo.html', {'productos': productos, 'fotos_productos': fotos_productos})
