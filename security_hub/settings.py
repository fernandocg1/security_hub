import os
from pathlib import Path

# 1. DIRETÓRIO RAIZ DO PROJETO
# Isso ajuda o Django a descobrir em qual pasta do seu computador o projeto está rodando.
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. CHAVE DE SEGURANÇA 
SECRET_KEY = 'Chave de segurança teste para desenvolvimento.'

# 3. MODO DE DEBUG (Desenvolvimento)
# Deixamos como True para que o Django nos mostre erros detalhados no terminal se algo der errado.
DEBUG = True

# Quem pode acessar esse servidor. '*' significa que qualquer dispositivo na rede local pode se conectar.
ALLOWED_HOSTS = ['*']

# 4. A LISTA DE APLICATIVOS (Onde registramos o nosso app e o REST Framework)
INSTALLED_APPS = [
    'django.contrib.admin',          # Painel administrativo visual
    'django.contrib.auth',           # Sistema de usuários e senhas
    'django.contrib.contenttypes',   # Permite ao Django entender as relações entre tabelas
    'django.contrib.sessions',       # Guarda o login do usuário no navegador
    'django.contrib.messages',       # Sistema de alertas/notificações internas
    'django.contrib.staticfiles',     # Gerencia arquivos como CSS e imagens do painel
    
    # Nossas ferramentas do projeto:
    'rest_framework',                # Ferramenta para criar as APIs para o celular e ESP32
    'monitoring',                    # O nosso aplicativo de sensores
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'security_hub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'security_hub.wsgi.application'

# 5. GERENCIADOR DE BANCO DE DADOS
# Estamos configurando o SQLite, que é um banco de dados leve que salva tudo em um arquivo local (.sqlite3).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. CONFIGURAÇÕES DE IDIOMA E HORA
# Configurado para o padrão do Brasil para os logs de segurança ficarem com o horário correto.
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# 7. ARQUIVOS ESTÁTICOS E CHAVE PRIMÁRIA
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'