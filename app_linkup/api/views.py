from rest_framework import mixins
from rest_framework import viewsets
from django.db.models import Count, Sum
from rest_framework.viewsets import GenericViewSet

from app_linkup.api.serializers import EncuestaSerializer, EncuestaListaSerializer
from app_linkup.models.encuesta import Encuesta


class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


class EncuestaDetalleView(mixins.ListModelMixin, GenericViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaListaSerializer
