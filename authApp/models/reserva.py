from django.db      import models
from .user          import User
from .habitacion    import Habitacion

class Reserva(models.Model):
    id                  = models.AutoField(primary_key=True)
    reserva_usuario     = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    reserva_habitacion  = models.ForeignKey(Habitacion, related_name='habitacion_reservada', on_delete=models.CASCADE)
    fecha_ingreso       = models.DateField()
    fecha_salida        = models.DateField()