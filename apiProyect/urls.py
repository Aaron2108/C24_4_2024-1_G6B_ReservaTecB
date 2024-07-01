from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    EstadoViewSet, CarreraViewSet, RolViewSet, UsuarioViewSet,
    CampoViewSet, HorarioViewSet, ReservaViewSet, AlertaViewSet
)

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'carreras', CarreraViewSet)
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'campos', CampoViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'alertas', AlertaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
