from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/listar.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro agregado.')
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/formulario.html', {'form': form, 'accion': 'Crear'})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado.')
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/formulario.html', {'form': form, 'accion': 'Editar'})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado.')
        return redirect('listar_libros')
    return render(request, 'biblioteca/confirmar_eliminacion.html', {'libro': libro})
