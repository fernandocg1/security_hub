from rest_framework import viewsets 
from .models import Device, EventLog
from .serializers import DeviceSerializer, EventLogSerializer, loginSerializer, UserSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#1. VIEW PARA LISTAR E CRIAR DISPOSITIVOS
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

#2. VIEW PARA LISTAR E CRIAR EVENTOS
class EventLogViewSet(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer

@api_view(['GET'])
def index(request):
    return Response({"message": "Bem-vindo ao Security Hub!"})

@api_view (['POST'])
def login_user(request):
    serializer = loginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        # Aqui você pode gerar um token ou realizar outras ações de login
        return Response({'token': token.key, 'user': user_data}
                        ,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           