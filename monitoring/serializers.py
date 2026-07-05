from rest_framework import serializers
from .models import Device, EventLog
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

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

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Credenciais inválidas.")
        else:
            raise serializers.ValidationError("É necessário fornecer um nome de usuário e senha.")

        data['user'] = user
        return data
