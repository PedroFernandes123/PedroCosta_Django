# 🔧 MUDANÇAS NECESSÁRIAS NO settings.py

## INSTRUÇÕES
Abra o arquivo `oficina_prj/settings.py` e faça as seguintes mudanças:

---

## PASSO 1: Adicionar Imports no Topo

**ENCONTRAR:**
```python
from pathlib import Path
```

**SUBSTITUIR POR:**
```python
from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
```

---

## PASSO 2: Configurar DEBUG e SECRET_KEY

**ENCONTRAR:**
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!chg5(xco6zd4kgtis8u2)&9mrt0+^vro4w2^=)q*p@cgt24i0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```

**SUBSTITUIR POR:**
```python
# Carregando variáveis de ambiente
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-unsafe-key-for-dev-only')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
```

---

## PASSO 3: Configurar ALLOWED_HOSTS

**ENCONTRAR:**
```python
ALLOWED_HOSTS = ['127.0.0.1','ecaa09-parte2-7uix.onrender.com']
```

**SUBSTITUIR POR:**
```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'ecaa09-app.onrender.com',  # ← Substituir com seu URL do Render
    os.getenv('RENDER_EXTERNAL_HOSTNAME', ''),
]

# Remover hosts vazios
ALLOWED_HOSTS = [h for h in ALLOWED_HOSTS if h]
```

---

## PASSO 4: Adicionar WhiteNoise Middleware

**ENCONTRAR:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
```

**SUBSTITUIR POR:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← ADICIONAR
    'django.contrib.sessions.middleware.SessionMiddleware',
```

---

## PASSO 5: Configurar Banco de Dados

**ENCONTRAR:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**SUBSTITUIR POR:**
```python
# Usar PostgreSQL em produção, SQLite em desenvolvimento
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

---

## PASSO 6: Configurar Static Files

**ENCONTRAR:**
```python
STATIC_URL = '/static/'
```

**SUBSTITUIR POR:**
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise storage para cache e compressão
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## PASSO 7: Configurar Media Files

**ENCONTRAR:**
```python
# Se não tiver esta configuração, adicione após STATIC_ROOT
```

**ADICIONAR:**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## PASSO 8: Configurar Segurança para Produção

**ENCONTRAR:**
```python
# Adicionar no final do arquivo, antes do último # ou no final
```

**ADICIONAR:**
```python
# ==================== SEGURANÇA ====================
# Ativado apenas em produção (DEBUG=False)

SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG

# ==================== CORS ====================
CORS_ALLOWED_ORIGINS = [
    'https://ecaa09-app.onrender.com',
    'http://localhost:8000',
    'http://localhost:3000',
]

# ==================== LOGGING ====================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
```

---

## PASSO 9: Verificar Arquivo Completo

Seu arquivo `settings.py` deve ter:

✅ Imports com `os`, `dj_database_url`, `load_dotenv`  
✅ `SECRET_KEY` carregando de variável de ambiente  
✅ `DEBUG` carregando de variável de ambiente  
✅ `ALLOWED_HOSTS` com Render URL  
✅ `WhiteNoiseMiddleware` no MIDDLEWARE  
✅ `DATABASES` com suporte a PostgreSQL  
✅ `STATIC_ROOT` configurado  
✅ `STATICFILES_STORAGE` com WhiteNoise  
✅ `MEDIA_URL` e `MEDIA_ROOT` configurados  
✅ Configurações de segurança adicionadas  
✅ Logging configurado  

---

## PASSO 10: Testar Localmente

```bash
# Verificar se não tem erros
python manage.py check

# Resultado esperado:
# System check identified no issues (0 silenced).
```

---

## 🎯 Arquivo settings.py Completo (Exemplo)

Veja o arquivo `settings.py.example` neste repositório para um exemplo completo pronto para usar.

---

## ⚠️ Importante

- **Nunca faça commit da variável `SECRET_KEY` real**
- Use `.env` local (não versionado)
- Gere uma nova `SECRET_KEY` para produção
- Use comando: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

---

**Status:** ✅ Pronto para aplicar

🚀 Depois disso, commit e push para o Render fazer o deploy automático!
