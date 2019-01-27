
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.cadastros.api.viewsets import OnibusViewSet


router = routers.DefaultRouter()
router.register(r'onibus', OnibusViewSet)



urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
