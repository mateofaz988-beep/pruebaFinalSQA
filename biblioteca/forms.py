from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'anio_publicacion']
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'genero': 'Género',
            'anio_publicacion': 'Año de Publicación'
        }
