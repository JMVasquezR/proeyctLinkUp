from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from app_linkup.models.tipo_documento import TipoDocumento
from app_linkup.utilitarios.genericos import CleanCharField


def solo_texto(value):
    if not value.isspace():
        raise ValidationError(
            _('%(value)s debe contener solo letras'),
            params={'value': value},
        )


class UsuarioAbstract(models.Model):
    class Meta:
        abstract = True

    cuenta_de_usuario = models.ForeignKey(get_user_model(), blank=True, on_delete=models.CASCADE)
    nombre = CleanCharField(blank=False, null=False, max_length=200)
    apellido = CleanCharField(blank=False, null=False, max_length=100)
    fecha_de_nacimiento = models.DateField(blank=False, null=True)
    tipo_documento = models.ForeignKey(TipoDocumento, null=False, blank=False, on_delete=False)
    numero_de_documento = CleanCharField(max_length=25, unique=True)
    correo = models.EmailField(blank=False, null=False, unique=True)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)

    @property
    def nombre_completo(self):
        return ' '.join([self.nombre, self.apellido])

    @transaction.atomic()
    def save(self, **kwargs):
        if self.pk:
            self.update(**kwargs)
        else:
            self.create(**kwargs)

    @transaction.atomic()
    def create(self, **kwargs):
        extra_data_from_here = {
            'first_name': self.nombre,
            'last_name': '%s' % (self.apellido,),
        }
        usuario = get_user_model().objects.create_user(
            self.correo,
            password=None,
            **({**extra_data_from_here})
        )
        self.cuenta_de_usuario = usuario
        super(UsuarioAbstract, self).save(**kwargs)

    @transaction.atomic()
    def update(self, **kwargs):
        self.cuenta_de_usuario.first_name = self.nombre
        self.cuenta_de_usuario.last_name = '%s' % (self.apellido,)
        self.cuenta_de_usuario.save()
        super(UsuarioAbstract, self).save(**kwargs)
