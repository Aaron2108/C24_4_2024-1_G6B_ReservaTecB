from django.contrib import admin
from .models import Usuario, Carrera, Rol, Estado, Campo, Reserva, Alerta, Horario

admin.site.register(Usuario)
admin.site.register(Carrera)
admin.site.register(Rol)
admin.site.register(Estado)
admin.site.register(Campo)
admin.site.register(Reserva)
admin.site.register(Alerta)
admin.site.register(Horario)
