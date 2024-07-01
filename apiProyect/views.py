from rest_framework import viewsets
from .models import Estado, Carrera, Rol, Usuario, Campo, Horario, Reserva, Alerta
from .serializer import (
    EstadoSerializer, CarreraSerializer, RolSerializer, UsuarioSerializer,
    CampoSerializer, HorarioSerializer, ReservaSerializer, AlertaSerializer
)

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CampoViewSet(viewsets.ModelViewSet):
    queryset = Campo.objects.all()
    serializer_class = CampoSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
