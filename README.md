# Sistema de Biblioteca - CRUD Django

Aplicación web para gestionar libros utilizando Django.

## Requisitos

- Python 3.8 o superior
- Django 5.2.17

## Instalación

1. Asegúrate de tener Django instalado:
```bash
pip install django
```

## Ejecución

1. Navega a la carpeta del proyecto:
```bash
cd proyecto
```

2. Ejecuta el servidor:
```bash
python manage.py runserver
```

3. Abre tu navegador en: `http://127.0.0.1:8000`

## Acceso al Admin

- URL: `http://127.0.0.1:8000/admin`
- Usuario: `admin`
- Contraseña: `admin123`

## Funcionalidades

- **Listar libros**: Ver todos los libros registrados
- **Crear libro**: Agregar un nuevo libro con título, autor, género y año
- **Editar libro**: Modificar información de un libro existente
- **Eliminar libro**: Eliminar un libro del sistema

## Estructura del Proyecto

```
proyecto/
├── manage.py
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── biblioteca/
    ├── models.py       (Modelo Libro)
    ├── views.py        (Vistas CRUD)
    ├── forms.py        (Formulario LibroForm)
    ├── urls.py         (Rutas de la aplicación)
    ├── admin.py        (Registro en admin)
    └── templates/
        └── biblioteca/
            ├── base.html
            ├── listar.html
            ├── formulario.html
            └── confirmar_eliminacion.html
```

## Modelo de Datos

**Libro**
- titulo: CharField (200 caracteres)
- autor: CharField (100 caracteres)
- genero: CharField (50 caracteres)
- anio_publicacion: IntegerField
