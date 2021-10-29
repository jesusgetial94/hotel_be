from authApp.models.reserva         import Reserva
from authApp.models.user            import User
from authApp.models.habitacion      import Habitacion
from rest_framework                 import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Reserva
        fields  = ['id', 'reserva_usuario', 'reserva_habitacion', 'fecha_ingreso', 'fecha_salida']
    def to_representation(self, obj):
        reserva_usuario     = User.objects.get(id = obj.reserva_usuario)
        reserva_habitacion  = Habitacion.objects.get(id = obj.reserva_habitacion)
        habitacion          = Habitacion.objects.get(id=obj.id)
        return {
            'id'                    : habitacion.id,
            'fecha_ingreso'         : habitacion.fecha_ingreso,
            'fecha_salida'          : habitacion.fecha_salida,
            'reserva_usuario': {
                'id'                : reserva_usuario.id,
                'name'              : reserva_usuario.name,
                'phone'             : reserva_usuario.phone,
                'email'             : reserva_usuario.email,
            },
            'reserva_habitacion': {
                'id'                : reserva_habitacion.id,
                'descripcion'       : reserva_habitacion.descripcion,
                'disponibilidad'    : reserva_habitacion.disponibilidad,
                'precio'            : reserva_habitacion.precio
            },
        }
