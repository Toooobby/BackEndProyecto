from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TipoComidaViewSet, ComidaViewSet

router = DefaultRouter()
router.register(r'TipoComidas', TipoComidaViewSet)
router.register(r'Comidas', ComidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
