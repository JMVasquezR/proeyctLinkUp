from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url, render, redirect
from django.views import View
from django.urls import reverse
from django.db.models import Count

# Create your views here.
from app_linkup.forms import LoginForm
from app_linkup.models.categoria import Categoria
from app_linkup.models.encuesta import Encuesta
from app_linkup.models.tipo_documento import TipoDocumento
from app_linkup.task.obtener_categorias import task_guardar_categorias


class ClienteLogin(LoginView):

    def get_success_url(self):
        url = self.get_redirect_url()
        task_guardar_categorias()
        return url or resolve_url('app-linkup:encuesta')


class LoginView(ClienteLogin):
    form_class = LoginForm
    template_name = 'login.html'


class EncuestaViewSet(View):

    def __init__(self):
        self.contexto = {}

    def get_contexto(self, **kwargs):
        '''
        Retornar el contexto para retornar la vista
        :return: dict
        '''
        self.contexto['ls_tipo_documento'] = TipoDocumento.objects.all()
        self.contexto['ls_categoria'] = Categoria.objects.all()
        self.contexto['ls_encuesta_categoria'] = Encuesta.objects.values('categoria__id', 'categoria__nombre').annotate(
            total=Count('categoria__nombre'))
        self.contexto['ls_encuesta'] = Encuesta.objects.all()
        return self.contexto

    def get(self, request):
        usuario = request.user
        if usuario.is_anonymous:
            return redirect(reverse('app-linkup:login'))
        task_guardar_categorias()
        return render(request, 'encuesta.html', self.get_contexto())


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('app-linkup:login'))
