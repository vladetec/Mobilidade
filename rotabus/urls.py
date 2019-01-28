
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.cadastros.api.viewsets import OnibusViewSet, ParadaViewSet, EnderecoViewSet


router = routers.DefaultRouter()
router.register(r'onibus', OnibusViewSet)
router.register(r'parada', ParadaViewSet)
router.register(r'endereco', EnderecoViewSet)



urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
