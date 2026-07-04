from rest_framework import serializers
from .models import Device, EventLog

# 1. SERIALIZERS PARA O MODELO Device
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'device_type', 'is_active']

# 2. SERIALIZERS PARA O MODELO EventLog
class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'device', 'event_type', 'details', 'is_emergency', 'timestamp']