from django.db import models

from app_linkup.models.categoria import Categoria
from app_linkup.models.cliente import Cliente
from app_linkup.utilitarios.genericos import CleanCharField


class Encuesta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=False)
    categoria = models.ForeignKey(Categoria, on_delete=False)
    motivo_o_porque = CleanCharField(blank=False, null=False, max_length=250)

    def catidad_categoria(self):
        return Encuesta.objects.filter(categoria=self.categoria).count()
