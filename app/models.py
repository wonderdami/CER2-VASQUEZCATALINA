from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre Especie")
    descripcion = models.TextField(verbose_name="Descripción")

class Mascota(models.Model):
    SEXO_OPCIONES = [
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
    ]
    nombre = models.CharField(max_length=50, verbose_name="Nombre Mascota")
    descripcion = models.TextField(verbose_name="Descripción")
    sexo = models.CharField(max_length=10, choices=SEXO_OPCIONES,  verbose_name="Sexo")
    edad = models.PositiveIntegerField(verbose_name="Edad")
    imagen = models.URLField(blank=True, null=True, verbose_name="URL de la Imagen")
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name="Especie")
