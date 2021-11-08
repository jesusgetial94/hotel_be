from django.conf                                import settings
from django.db.models.query import QuerySet
from rest_framework                             import status, generics
from rest_framework.response                    import Response
from rest_framework.permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend
from authApp.models.reserva                     import Reserva
from authApp.serializers.reservaSerializer      import ReservaSerializer
from authApp.models.user                        import User
from authApp.models.habitacion                  import Habitacion
from rest_framework.exceptions                  import NotAuthenticated
class ReservasView(generics.ListAPIView):
    serializer_class  = ReservaSerializer
    def get_queryset(self):
        try:
            token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data   = tokenBackend.decode(token,verify=False)
            print("id de usuario: ", valid_data['user_id'])
        except:
            raise NotAuthenticated("Se requiere autentificacion")
        user = User.objects.get(id=valid_data['user_id'])
        if user.is_superuser:
            queryset = Reserva.objects.all()
            return queryset
        else:
            queryset = Reserva.objects.filter(reserva_usuario_id = valid_data['user_id'])
            return queryset
class  ReservaDetailView(generics.RetrieveAPIView):
    #RetrieveAPIView para ver el detalle de solo una
    serializer_class    = ReservaSerializer
    permissions_classes = (IsAuthenticated,)
    queryset            =  Reserva.objects.all()
    
    def get(self, request, *args, **kwargs):
        print('Request: ', request)
        print('Args: ', args)
        print('KWArgs: ', kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class ReservaCreateView(generics.CreateAPIView):
    serializer_class    = ReservaSerializer
    permissions_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        print('Request: ', request)
        print('Args: ', args)
        print('KWArgs: ', kwargs)
        try:
            token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        except:
            return Response("Token requerido", status=status.HTTP_401_UNAUTHORIZED)
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != request.data['reserva_usuario']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        print(request.data)
        serializer = ReservaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Reservación Exitosa", status=status.HTTP_201_CREATED)

class ReservaUpdateView(generics.UpdateAPIView):
    serializer_class    = ReservaSerializer
    permissions_classes = (IsAuthenticated,)
    queryset            = Reserva.objects.all()
    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().partial_update(request, *args, **kwargs)

class ReservaDelateView(generics.DestroyAPIView):
    serializer_class    = ReservaSerializer
    permissions_classes = (IsAuthenticated,)
    queryset            = Reserva.objects.all()
    def get(self, request, *args, **kwargs):
        print('Request: ', request)
        print('Args: ', args)
        print('KWArgs: ', kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if not (User.objects.get(id=valid_data['user_id']).is_superuser) and valid_data['user_id'] != kwargs['user'] :
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)

