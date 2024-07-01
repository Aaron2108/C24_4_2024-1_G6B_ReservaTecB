from rest_framework import serializers
from .models import Estado, Carrera, Rol, Usuario, Campo, Horario, Reserva, Alerta

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
