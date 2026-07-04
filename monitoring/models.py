from django.db import models

# 1. A TABELA DE DISPOSITIVOS
class Device(models.Model):
    # Uma lista de opções fixas para o tipo de dispositivo
    DEVICE_TYPES = (
        ('DOOR', 'Sensor de Porta/Janela'),
        ('CAM', 'Câmera com IA (YOLO)'),
    )
    
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=4, choices=DEVICE_TYPES)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
# 2. Eventlog (Registro de eventos consolidados)
class EventLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    
    # Novos campos unificados na mesma tabela
    details = models.TextField(blank=True, null=True, help_text="Detalhes adicionais da IA")
    is_emergency = models.BooleanField(default=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        emergencia_str = " [EMERGÊNCIA]" if self.is_emergency else ""
        return f"{self.device.name} - {self.event_type}{emergencia_str} at {self.timestamp.strftime('%d/%m/%Y %H:%M')}"