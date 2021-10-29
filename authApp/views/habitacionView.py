from django.conf                                import settings
from rest_framework                             import status, generics
from rest_framework.response                    import Response
from rest_framework.permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend
from authApp.models.habitacion                  import Habitacion
from authApp.models.user import User
from authApp.serializers.habitacionSerializer   import HabitacionSerializer

class HabitacionesView(generics.ListAPIView):
    #ListAPIView, para traer mas de un elemento
    serializer_class  = HabitacionSerializer
    def get_queryset(self):
        queryset = Habitacion.objects.all()
        return queryset

class  HabitacionDetailView(generics.RetrieveAPIView):
    #RetrieveAPIView para ver el detalle de solo una
    serializer_class    = HabitacionSerializer
    queryset            =  Habitacion.objects.all()
    
    def get(self, request, *args, **kwargs):
        #print('Request: ', request)
        #print('Args: ', args)
        #print('KWArgs: ', kwargs)
        return super().get(request, *args, **kwargs)

class HabitacionCreateView(generics.CreateAPIView):
    serializer_class    = HabitacionSerializer
    permissions_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        print('Request: ', request)
        print('Args: ', args)
        print('KWArgs: ', kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(id=request.data['user_id'])
        if user.is_superuser:
            serializer = HabitacionSerializer(data=request.data['habitacion_data'])
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("Creacion de Habitacion Exitosa", status=status.HTTP_201_CREATED)
        else:
            return Response("Permisos de administrador, requerido", status=status.HTTP_401_UNAUTHORIZED)
        #serializer = HabitacionSerializer(data=request.data['habitacion_data'])
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response("Creacion de Habitacion Exitosa", status=status.HTTP_201_CREATED)

class HabitacionUpdateView(generics.UpdateAPIView):
    serializer_class    = HabitacionSerializer
    permissions_classes = (IsAuthenticated,)
    queryset            = Habitacion.objects.all()
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
        user = User.objects.get(id=kwargs['user'])
        if user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        else:
            return Response("Permisos de administrador, requerido", status=status.HTTP_401_UNAUTHORIZED)
    """def post(self, request, *args, **kwargs):
        print('Request: ', request)
        print('Args: ', args)
        print('KWArgs: ', kwargs)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail' : 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        try:
            super().partial_update(request, *args, **kwargs)
        except NameError:
            return Response(NameError, status=status.HTTP_304_NOT_MODIFIED)
        return Response("Actualizacion Exitosa", status=status.HTTP_200_OK)
    """

class HabitacionDelateView(generics.DestroyAPIView):
    serializer_class    = HabitacionSerializer
    permissions_classes = (IsAuthenticated,)
    queryset            = Habitacion.objects.all()
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
        user = User.objects.get(id=kwargs['user'])
        if user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response("Permisos de administrador, requerido", status=status.HTTP_401_UNAUTHORIZED)
    

