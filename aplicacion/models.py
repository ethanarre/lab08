from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    autor_id = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numpags = models.SmallIntegerField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    NumUsuario = models.IntegerField()
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Prestamos(models.Model):
    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FecPrestamo = models.DateField('Inicio')
    FecDevolucion = models.DateField('Fin')
    list_display = '__all__'
