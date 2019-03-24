from rest_framework import routers

from app_linkup.api.views import EncuestaViewSet, EncuestaDetalleView

router = routers.DefaultRouter()
router.register(r'encuesta', EncuestaViewSet, base_name='encuesta')
router.register(r'categoria-resultado', EncuestaDetalleView, base_name='ctegoria-resultado')
urlpatterns = router.urls
