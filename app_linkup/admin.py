from django.contrib import admin
from django import forms

from app_linkup.models.categoria import Categoria
from app_linkup.models.cliente import Cliente
from app_linkup.models.encuesta import Encuesta
from app_linkup.models.tipo_documento import TipoDocumento


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
    list_display = ['nombre', 'apellido', 'correo']


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = '__all__'


class TipoDocumentoAdmin(admin.ModelAdmin):
    form = TipoDocumentoForm
    list_display = ['nombre_corto', 'nombre_largo', 'longitud']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm
    list_display = ['id', 'nombre', 'descripcion']


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'


class EncuestaAdmin(admin.ModelAdmin):
    form = EncuestaForm
    list_display = ['cliente', 'categoria', 'motivo_o_porque']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Encuesta, EncuestaAdmin)
