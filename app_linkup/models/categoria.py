from django.db import models
import os

from app_linkup.utilitarios.genericos import CleanCharField


class Categoria(models.Model):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        return os.path.join('categoria', 'foto-' + instance.nombre + file_extension)

    nombre = CleanCharField(blank=False, null=False, max_length=100)
    descripcion = CleanCharField(blank=False, null=False, max_length=200)
    imagen = models.ImageField(upload_to=image_path, null=True, blank=True, max_length=100)
    orden = models.IntegerField(null=True, blank=True)
    estado = models.BooleanField(null=True)
