from rest_framework import serializers
from django.db import transaction

from app_linkup.models.categoria import Categoria
from app_linkup.models.cliente import Cliente
from app_linkup.models.encuesta import Encuesta


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'tipo_documento', 'numero_de_documento', 'correo']


class EncuestaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(write_only=True)
    categoria = serializers.IntegerField(required=True)
    motivo_o_porque = serializers.CharField(required=True)

    class Meta:
        model = Encuesta
        fields = ['cliente', 'categoria', 'motivo_o_porque']

    @transaction.atomic()
    def save(self, **kwargs):
        cliente_object = dict(self.validated_data['cliente'])
        categoria = self.validated_data['categoria']
        motivo_o_porque = self.validated_data['motivo_o_porque']

        nombre = cliente_object['nombre']
        apellido = cliente_object['apellido']
        fecha_de_nacimiento = cliente_object['fecha_de_nacimiento']
        tipo_documento = cliente_object['tipo_documento'].id
        numero_de_documento = cliente_object['numero_de_documento']
        correo = cliente_object['correo']

        cliente = Cliente(nombre=nombre, apellido=apellido, fecha_de_nacimiento=fecha_de_nacimiento,
                          tipo_documento_id=tipo_documento, numero_de_documento=numero_de_documento, correo=correo)
        cliente.save()

        encuesta = Encuesta(cliente_id=cliente.id, categoria_id=categoria, motivo_o_porque=motivo_o_porque)
        encuesta.save()


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EncuestaListaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    categoria = CategoriaSerializer()
    motivo_o_porque = serializers.CharField(required=True)

    class Meta:
        model = Encuesta
        fields = ['cliente', 'categoria', 'motivo_o_porque', 'catidad_categoria']
