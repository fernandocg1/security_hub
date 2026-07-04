from rest_framework import viewsets 
from .models import Device, EventLog
from .serializers import DeviceSerializer, EventLogSerializer

#1. VIEW PARA LISTAR E CRIAR DISPOSITIVOS
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

#2. VIEW PARA LISTAR E CRIAR EVENTOS
class EventLogViewSet(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer