from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from app_linkup.views import LoginView, EncuestaViewSet

urlpatterns = [
    url(r'^api/', include(('app_linkup.api.urls', 'api'), namespace='api')),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^encuesta/', EncuestaViewSet.as_view(), name='encuesta'),
    url(r'^logout/', LogoutView.as_view(), name='salida'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
