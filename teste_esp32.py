import requests

url = 'http://127.0.0.1:8000/api/events/'
]

headers = {
    'Authorization': 'Token 6513c2044c6d16cd5a459dda6c4dd3bd3b4f9388' 
}

dados = {
    "device": 1,
    "event_type": "Pessoa Detectada no Quintal",
    "is_emergency": True
}

resposta = requests.post(url, headers=headers, json=dados)

print("Status Code:", resposta.status_code)
print("Resposta do Servidor:", resposta.json())
