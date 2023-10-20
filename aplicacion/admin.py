from django.contrib import admin
from .models import Autor, Libro, Usuario, Prestamos

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'autor_id', 'isbn', 'editorial', 'numpags')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('NumUsuario', 'nif', 'nombre', 'direccion', 'telefono')

class PrestamosAdmin(admin.ModelAdmin):
    list_display = ('libro_id', 'usuario_id', 'FecPrestamo', 'FecDevolucion')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Prestamos, PrestamosAdmin)
