# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_productos')
    return render(request, 'crear.html', {'form': form})

# Editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('lista_productos')
    return render(request, 'editar.html', {'form': form, 'producto': producto})

# Eliminar producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar.html', {'producto': producto})
