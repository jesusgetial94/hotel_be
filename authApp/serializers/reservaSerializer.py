from authApp.models.reserva         import Reserva
from authApp.models.user            import User
from authApp.models.habitacion      import Habitacion
from rest_framework                 import serializers

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Reserva
        fields  = ['id', 'reserva_usuario', 'reserva_habitacion', 'fecha_ingreso', 'fecha_salida']
    def to_representation(self, obj):
        reserva_usuario     = User.objects.get(id = obj.reserva_usuario_id)
        reserva_habitacion  = Habitacion.objects.get(id = obj.reserva_habitacion_id)
        reserva          = Reserva.objects.get(id=obj.id)
        return {
            'id'                    : reserva.id,
            'fecha_ingreso'         : reserva.fecha_ingreso,
            'fecha_salida'          : reserva.fecha_salida,
            'reserva_usuario': {
                'name'              : reserva_usuario.name,
                'phone'             : reserva_usuario.phone,
                'email'             : reserva_usuario.email,
            },
            'reserva_habitacion': {
                'descripcion'       : reserva_habitacion.descripcion,
                'disponibilidad'    : reserva_habitacion.disponibilidad,
                'precio'            : reserva_habitacion.precio
            },
        }

class ReservaSerializerHidden(serializers.ModelSerializer):
    class Meta:
        model   = Reserva
        fields  = ['reserva_usuario', 'reserva_habitacion', 'fecha_ingreso', 'fecha_salida']
    def to_representation(self, obj):
        #reserva_usuario     = User.objects.get(id = obj.reserva_usuario)
        #reserva_habitacion  = Habitacion.objects.get(id = obj.reserva_habitacion)
        #reserva          = Reserva.objects.get(id=obj.id)
        return {
            """'id'                    : reserva.id,
            'fecha_ingreso'         : reserva.fecha_ingreso,
            'fecha_salida'          : reserva.fecha_salida,
            'reserva_habitacion': {
                'id'                : reserva_habitacion.id,
                'descripcion'       : reserva_habitacion.descripcion,
                'disponibilidad'    : reserva_habitacion.disponibilidad,
                'precio'            : reserva_habitacion.precio
            },"""
        }
