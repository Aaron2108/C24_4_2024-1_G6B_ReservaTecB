from django.db import models


class Alerta(models.Model):
    pk_id_alerta = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'alerta'


class Campo(models.Model):
    pk_id_campo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    aforo = models.IntegerField()
    fk_id_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='fk_id_estado', default=1)

    class Meta:
        managed = False
        db_table = 'campo'


class Carrera(models.Model):
    pk_id_carrera = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'carrera'


class Estado(models.Model):
    pk_id_estado = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Horario(models.Model):
    pk_id_horario = models.BigAutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'horario'


class Reserva(models.Model):
    pk_id_reserva = models.BigAutoField(primary_key=True)
    fk_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usuario')
    fk_id_campo = models.ForeignKey(Campo, models.DO_NOTHING, db_column='fk_id_campo')
    fecha = models.DateField()
    fk_id_horario = models.ForeignKey(Horario, models.DO_NOTHING, db_column='fk_id_horario')
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fk_id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='fk_id_estado')

    class Meta:
        managed = False
        db_table = 'reserva'
        unique_together = (('fk_id_usuario', 'fecha'), ('fk_id_campo', 'fk_id_horario', 'fecha'),)


class Rol(models.Model):
    pk_id_rol = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    pk_id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='pk_id_estado')

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    pk_id_usuario = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    nombres = models.CharField(max_length=255)
    codigo_tecsup = models.CharField(max_length=255)
    fk_id_carrera = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='fk_id_carrera', blank=True, null=True)
    fk_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_id_rol')
    fk_id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='fk_id_estado')

    class Meta:
        managed = False
        db_table = 'usuario'
