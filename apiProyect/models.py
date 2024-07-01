from django.db import models

class Estado(models.Model):
    pk_id_estado = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'


class Carrera(models.Model):
    pk_id_carrera = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'carrera'


class Rol(models.Model):
    pk_id_rol = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    pk_id_estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, db_column='pk_id_estado')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'rol'


class Usuario(models.Model):
    pk_id_usuario = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    nombres = models.CharField(max_length=255)
    codigo_tecsup = models.CharField(max_length=255)
    fk_id_carrera = models.ForeignKey(Carrera, on_delete=models.DO_NOTHING, db_column='fk_id_carrera', blank=True, null=True)
    fk_id_rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING, db_column='fk_id_rol')
    fk_id_estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, db_column='fk_id_estado')

    def __str__(self):
        return self.nombres

    class Meta:
        db_table = 'usuario'


class Campo(models.Model):
    pk_id_campo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    aforo = models.IntegerField()
    fk_id_estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, db_column='fk_id_estado')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'campo'


class Horario(models.Model):
    pk_id_horario = models.BigAutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin}"

    class Meta:
        db_table = 'horario'


class Reserva(models.Model):
    pk_id_reserva = models.BigAutoField(primary_key=True)
    fk_id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_campo = models.ForeignKey(Campo, on_delete=models.DO_NOTHING, db_column='fk_id_campo')
    fecha = models.DateField()
    fk_id_horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, db_column='fk_id_horario')
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fk_id_estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, db_column='fk_id_estado')

    def __str__(self):
        return f"Reserva de {self.fk_id_usuario} en {self.fk_id_campo} el {self.fecha}"

    class Meta:
        db_table = 'reserva'


class Alerta(models.Model):
    pk_id_alerta = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Alerta: {self.descripcion} ({self.fecha})"

    class Meta:
        db_table = 'alerta'
