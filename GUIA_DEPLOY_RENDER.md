# 🚀 GUIA COMPLETO - HOSPEDAR DJANGO NO RENDER.COM

## 📋 Índice
1. Preparação do Projeto
2. Configuração de Banco de Dados
3. Criação do Serviço no Render
4. Variáveis de Ambiente
5. Deploy Inicial
6. Troubleshooting
7. Manutenção

---

## 1️⃣ PREPARAÇÃO DO PROJETO

### Passo 1: Criar arquivo `requirements.txt`
```bash
pip freeze > requirements.txt
```

**Seu arquivo deve conter:**
```
Django==5.2
Pillow==12.0.0
gunicorn==22.0.0
whitenoise==6.6.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
```

**Se não tiver esses pacotes, instale:**
```bash
pip install gunicorn whitenoise python-dotenv psycopg2-binary
pip freeze > requirements.txt
```

### Passo 2: Criar arquivo `runtime.txt`
Cria um arquivo com este conteúdo:

```
python-3.12.0
```

**Por quê?** Render precisa saber qual versão do Python usar.

### Passo 3: Criar arquivo `build.sh`
Cria um arquivo na raiz do projeto:

```bash
#!/usr/bin/env bash
# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Aplicar migrações
python manage.py migrate
```

**Permissão no bash:**
```bash
chmod +x build.sh
```

### Passo 4: Atualizar `settings.py`
```python
# No topo do arquivo
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# ... resto do código ...

# SECURITY SETTINGS PARA PRODUÇÃO
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'seu-app.onrender.com',  # ← Substitua com seu URL do Render
    os.getenv('RENDER_EXTERNAL_HOSTNAME', ''),
]

# Remover hosts vazios
ALLOWED_HOSTS = [h for h in ALLOWED_HOSTS if h]

# DATABASE - Usar variável de ambiente
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

# STATIC FILES
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Middleware de whitenoise (comprime e cacheia estáticos)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Adicionar aqui
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... resto do middleware ...
]

# Compressão de estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SECURITY
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG

# CORS
CORS_ALLOWED_ORIGINS = [
    'https://seu-app.onrender.com',
    'http://localhost:8000',
]

# Logs (importante para debug)
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
}
```

### Passo 5: Criar arquivo `.gitignore` (se não tiver)
```
*.pyc
__pycache__/
*.egg-info/
dist/
build/
.env
.venv
venv/
staticfiles/
media/
db.sqlite3
.DS_Store
*.log
```

### Passo 6: Fazer commit dos arquivos
```bash
git add requirements.txt runtime.txt build.sh settings.py
git commit -m "Configurar para deploy no Render"
git push origin develop
```

---

## 2️⃣ CONFIGURAÇÃO DE BANCO DE DADOS

### Opção A: PostgreSQL (Recomendado)

#### No Render:
1. Login em https://render.com
2. Dashboard → New → PostgreSQL
3. Preencher:
   - **Name:** `ecaa09-db`
   - **Database:** `ecaa09`
   - **User:** `postgres`
   - **Region:** São Paulo (sa-south-1)
   - **Plan:** Free (até 7GB)
4. Copiar a **Internal Database URL**

#### Exemplo de URL:
```
postgresql://postgres:SENHA@dpg-xxx.render.internal:5432/ecaa09
```

### Opção B: SQLite (Mais Simples, não recomendado para produção)
- Usar banco local
- Dados salvos no servidor
- Limite de conexões

**Para esta sessão, use PostgreSQL**

---

## 3️⃣ CRIAÇÃO DO SERVIÇO NO RENDER

### Passo 1: Conectar GitHub
1. Ir para https://render.com
2. Sign up / Login
3. Conectar GitHub

### Passo 2: Criar novo Web Service
1. Dashboard → **New** → **Web Service**
2. Selecionar repository: `ECAA09_Parte2-main`
3. Configurar:

| Campo | Valor |
|-------|-------|
| **Name** | `ecaa09-app` |
| **Environment** | `Python 3` |
| **Region** | `São Paulo (sa-south-1)` |
| **Branch** | `develop` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn oficina_prj.wsgi:application --bind 0.0.0.0:$PORT` |
| **Plan** | `Free` |

### Passo 3: Adicionar Variáveis de Ambiente
Na página de criação, rolar para **Environment** e adicionar:

```
DEBUG=False
SECRET_KEY=seu-secret-key-super-seguro-aqui
DATABASE_URL=postgresql://postgres:SENHA@dpg-xxx.render.internal:5432/ecaa09
ALLOWED_HOSTS=seu-app.onrender.com,localhost
```

**Gerar SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Passo 4: Criar Serviço
Clicar em **Create Web Service**

---

## 4️⃣ VARIÁVEIS DE AMBIENTE

### Arquivo `.env.example` (para referência)
Cria na raiz do projeto:

```
# Django
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=seu-app.onrender.com,localhost

# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu@email.com
EMAIL_HOST_PASSWORD=sua-senha-app

# Static Files
STATIC_ROOT=staticfiles
```

### Valores Importantes

| Variável | Valor | Onde Pegar |
|----------|-------|-----------|
| `DEBUG` | `False` | Segurança - sempre False em produção |
| `SECRET_KEY` | Aleatório | Gerado localmente |
| `DATABASE_URL` | Postgres URL | Dashboard Render |
| `ALLOWED_HOSTS` | Seu domínio | dashboard.onrender.com |

---

## 5️⃣ DEPLOY INICIAL

### Etapa 1: Verificar Build
1. Ir para Dashboard do Render
2. Clicar no seu serviço `ecaa09-app`
3. Ir para aba **Logs**
4. Esperar build completo

### Etapa 2: Verificar Erros
Se houver erros, ver em **Logs**:

**Erro comum: Static Files**
```
ModuleNotFoundError: No module named 'whitenoise'
```
Solução: Adicionar `whitenoise` ao `requirements.txt`

**Erro comum: Database**
```
psycopg2.OperationalError: could not connect to server
```
Solução: Verificar `DATABASE_URL` correto

### Etapa 3: Primeira Execução
1. Render executa `build.sh` automaticamente
2. Coleta static files
3. Aplica migrations
4. Inicia servidor

### Etapa 4: Acessar Aplicação
- **URL:** `https://seu-app.onrender.com`
- Esperar ~30 segundos na primeira carga

---

## 6️⃣ TROUBLESHOOTING

### 🔴 Erro: 500 Internal Server Error

**Solução 1: Ver logs**
```
Render Dashboard → Logs → Procurar erro
```

**Solução 2: DEBUG=True temporariamente** (apenas para debug)
```
Environment → DEBUG=True → Save
```

**Solução 3: Verificar migrations**
```
# Local
python manage.py migrate

# Commit e push
git add .
git commit -m "Apply migrations"
git push origin develop
```

### 🔴 Erro: Database Connection Failed

**Verificar DATABASE_URL:**
```bash
# Local, testar conexão
python
>>> import dj_database_url
>>> url = "postgresql://user:pass@host:5432/db"
>>> dj_database_url.config(default=url)
```

### 🔴 Erro: Static Files Not Found

**Solução:**
```bash
# Local
python manage.py collectstatic --noinput
git add staticfiles/
git commit -m "Add static files"
git push
```

### 🔴 Erro: Module Not Found

**Solução:**
```bash
# Local
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

### 🔴 Imagens Não Aparecem

**Problema:** Upload de imagem (media files) não persiste

**Solução:** Usar S3 ou similar
```python
# settings.py
import os
from storages.backends.s3boto3 import S3Boto3Storage

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = 'seu-bucket'
    AWS_S3_REGION_NAME = 'sa-east-1'
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'
```

---

## 7️⃣ MANUTENÇÃO

### Deploy Automático
Render faz deploy automático quando há push para `develop`:
1. Push código
2. Render detecta mudança
3. Build automático
4. Deploy automático

### Redeployar Manualmente
```
Dashboard → Seu serviço → Manual Deploy → Deploy latest commit
```

### Monitorar Aplicação
1. Ir para **Metrics** no dashboard
2. Ver: CPU, Memória, Requisições
3. Ver **Logs** para erros

### Backup do Banco de Dados
1. Dashboard PostgreSQL
2. Backups → Download
3. Guardar em local seguro

### Atualizar Dependências
```bash
# Local
pip install --upgrade Django Pillow gunicorn
pip freeze > requirements.txt

# Commit e push
git add requirements.txt
git commit -m "Update dependencies"
git push origin develop
```

---

## 📊 Checklist de Deploy

- [ ] `requirements.txt` criado e atualizado
- [ ] `runtime.txt` com Python 3.12
- [ ] `build.sh` criado com permissão
- [ ] `settings.py` configurado para produção
- [ ] `.gitignore` criado
- [ ] PostgreSQL criado no Render
- [ ] Web Service criado no Render
- [ ] Variáveis de ambiente definidas
- [ ] Build completado sem erros
- [ ] Aplicação carrega em produção
- [ ] Testes: login, cadastro, upload funcionam
- [ ] Domínio customizado configurado (opcional)

---

## 🔗 Links Úteis

- [Render Documentation](https://render.com/docs)
- [Django Deployment](https://docs.djangoproject.com/en/5.2/howto/deployment/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)
- [PostgreSQL Render](https://render.com/docs/databases)

---

## 💡 Dicas Importantes

### 1. Backup de Dados
```bash
# Fazer backup local antes de qualquer mudança
python manage.py dumpdata > backup.json
```

### 2. Testar Localmente Antes
```bash
# Simular produção localmente
DEBUG=False python manage.py runserver
```

### 3. Logs são seus Amigos
```
Sempre verificar Render Logs para erros
Render → Seu App → Logs
```

### 4. Domínio Customizado
```
Render Dashboard → Settings → Custom Domain
Adicionar: minhaapp.com.br
```

### 5. SSL/HTTPS
```
Automático no Render
Todas URLs são HTTPS
```

---

## ⚡ Quick Deploy (5 passos)

1. **Preparar projeto:**
   ```bash
   pip freeze > requirements.txt
   echo "python-3.12.0" > runtime.txt
   ```

2. **Criar build.sh e settings.py** (como acima)

3. **Commit e push:**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin develop
   ```

4. **No Render:**
   - New Web Service
   - Conectar GitHub
   - Configurar build/start commands
   - Adicionar variáveis de ambiente

5. **Deploy automático:**
   - Render faz tudo sozinho
   - Esperar ~5 minutos
   - Acessar seu-app.onrender.com

---

**Versão:** 1.0  
**Data:** 2024  
**Status:** ✅ Pronto para usar

🚀 **Seu Django no ar em menos de 1 hora!**
