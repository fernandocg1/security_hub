import requests

url = 'http://127.0.0.1:8000/api/events/'

# Aqui é onde o ESP32 apresenta o crachá VIP!
headers = {
    'Authorization': 'Token 6513c2044c6d16cd5a459dda6c4dd3bd3b4f9388' 
}

# Dados falsos simulando a câmera YOLO detectando uma pessoa
dados = {
    "device": 1, # O ID da sua Câmera 
    "event_type": "Pessoa Detectada no Quintal",
    "is_emergency": True
}

# Fazendo o disparo
resposta = requests.post(url, headers=headers, json=dados)

print("Status Code:", resposta.status_code)
print("Resposta do Servidor:", resposta.json())