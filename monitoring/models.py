from django.db import models

class Device(models.Model):
    DEVICE_TYPES = (
        ('DOOR', 'Sensor de Porta/Janela'),
        ('CAM', 'Câmera com IA (YOLO)'),
    )
    
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=4, choices=DEVICE_TYPES)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class EventLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True, help_text="Detalhes adicionais da IA")
    is_emergency = models.BooleanField(default=False)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        emergencia_str = " [EMERGÊNCIA]" if self.is_emergency else ""
        return f"{self.device.name} - {self.event_type}{emergencia_str} at {self.timestamp.strftime('%d/%m/%Y %H:%M')}"