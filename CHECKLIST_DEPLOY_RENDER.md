# ✅ CHECKLIST INTERATIVO - DEPLOY RENDER

## 📋 Use este checklist para acompanhar seu progresso

---

## FASE 1: PREPARAÇÃO LOCAL

### [ ] Passo 1.1: Instalar pacotes necessários
```bash
pip install gunicorn whitenoise psycopg2-binary python-dotenv dj-database-url
```
**Verifiação:** `pip list | grep gunicorn`

### [ ] Passo 1.2: Criar requirements.txt
```bash
pip freeze > requirements.txt
```
**Verificação:** `cat requirements.txt | head -5`

### [ ] Passo 1.3: Verificar runtime.txt
```bash
ls -la runtime.txt
cat runtime.txt
```
**Conteúdo esperado:** `python-3.12.0`

### [ ] Passo 1.4: Verificar build.sh
```bash
ls -la build.sh
cat build.sh
```
**Conteúdo esperado:** Tem `collectstatic` e `migrate`

### [ ] Passo 1.5: Verificar .env.example
```bash
ls -la .env.example
```
**Conteúdo esperado:** Tem variáveis de exemplo

### [ ] Passo 1.6: Testar locally
```bash
python manage.py check
```
**Resultado esperado:** `System check identified no issues (0 silenced).`

---

## FASE 2: CONFIGURAÇÃO DO settings.py

### [ ] Passo 2.1: Adicionar imports
```python
# Verificar no início de settings.py:
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()
```

### [ ] Passo 2.2: Configurar SECRET_KEY
```python
# Deve ser assim:
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-only')
```

### [ ] Passo 2.3: Configurar DEBUG
```python
# Deve ser assim:
DEBUG = os.getenv('DEBUG', 'True') == 'True'
```

### [ ] Passo 2.4: Configurar ALLOWED_HOSTS
```python
# Deve incluir:
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'seu-app.onrender.com',
    os.getenv('RENDER_EXTERNAL_HOSTNAME', ''),
]
```

### [ ] Passo 2.5: Adicionar WhiteNoise Middleware
```python
# Verificar em MIDDLEWARE:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Deve estar aqui
    ...
]
```

### [ ] Passo 2.6: Configurar DATABASES
```python
# Deve ter:
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL'),
            conn_max_age=600,
        )
    }
else:
    # SQLite para desenvolvimento
```

### [ ] Passo 2.7: Configurar STATIC FILES
```python
# Deve ter:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### [ ] Passo 2.8: Testar settings
```bash
python manage.py check
```
**Resultado esperado:** 0 issues

---

## FASE 3: GITHUB

### [ ] Passo 3.1: Verificar git status
```bash
git status
```
**Deve mostrar:** Arquivos novos (`requirements.txt`, `runtime.txt`, `build.sh`)

### [ ] Passo 3.2: Adicionar arquivos
```bash
git add requirements.txt runtime.txt build.sh .env.example
git add oficina_prj/settings.py
```

### [ ] Passo 3.3: Verificar adições
```bash
git status
```
**Deve mostrar:** Arquivos prontos para commit (green)

### [ ] Passo 3.4: Fazer commit
```bash
git commit -m "Configurar para deploy no Render.com"
```
**Resultado:** Commit criado

### [ ] Passo 3.5: Fazer push
```bash
git push origin develop
```
**Resultado:** Push completo, sem erros

### [ ] Passo 3.6: Verificar no GitHub
```
https://github.com/seu-usuario/ECAA09_Parte2-main
- Verificar branch develop
- Arquivo runtime.txt presente ✅
- Arquivo build.sh presente ✅
- Arquivo requirements.txt presente ✅
```

---

## FASE 4: RENDER - SETUP BANCO DE DADOS

### [ ] Passo 4.1: Acessar Render
```
https://render.com
Login com GitHub
```

### [ ] Passo 4.2: Criar PostgreSQL
```
Dashboard → New → PostgreSQL
```

### [ ] Passo 4.3: Preencher formulário
```
✓ Name: ecaa09-db
✓ Database: ecaa09
✓ User: postgres
✓ Region: São Paulo (sa-south-1)
✓ Plan: Free
```

### [ ] Passo 4.4: Copiar DATABASE_URL
```
Clicar em "Connections"
Copiar "Internal Database URL"
Exemplo: postgresql://postgres:xyz@dpg-abc.render.internal:5432/ecaa09
```
**Verificação:** Salva em algum lugar seguro para usar depois

---

## FASE 5: RENDER - CRIAR WEB SERVICE

### [ ] Passo 5.1: Ir para Dashboard
```
https://render.com/dashboard
```

### [ ] Passo 5.2: Novo Web Service
```
New → Web Service
```

### [ ] Passo 5.3: Conectar GitHub (primeira vez)
```
1. Click "Connect Account"
2. Authorize Render
3. Select repository: ECAA09_Parte2-main
4. Click "Connect"
```

### [ ] Passo 5.4: Preencher Configuração
```
✓ Name: ecaa09-app
✓ Region: São Paulo (sa-south-1)
✓ Branch: develop
✓ Runtime: Python 3
✓ Build Command: ./build.sh
✓ Start Command: gunicorn oficina_prj.wsgi:application --bind 0.0.0.0:$PORT
✓ Plan: Free
```

---

## FASE 6: RENDER - VARIÁVEIS DE AMBIENTE

### [ ] Passo 6.1: Gerar SECRET_KEY
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
**Resultado:** Copiou a chave

### [ ] Passo 6.2: Na página Render, rolar para Environment

### [ ] Passo 6.3: Adicionar variáveis (uma por uma)
```
DEBUG: False
SECRET_KEY: (cole aqui a chave gerada)
DATABASE_URL: (cole aqui a URL do PostgreSQL)
ALLOWED_HOSTS: ecaa09-app.onrender.com,localhost
RENDER_EXTERNAL_HOSTNAME: ecaa09-app.onrender.com
```

### [ ] Passo 6.4: Verificar cada variável foi adicionada
```
✓ DEBUG
✓ SECRET_KEY
✓ DATABASE_URL
✓ ALLOWED_HOSTS
✓ RENDER_EXTERNAL_HOSTNAME
```

---

## FASE 7: DEPLOY INICIAL

### [ ] Passo 7.1: Clicar "Create Web Service"
```
Botão azul em baixo da página
```

### [ ] Passo 7.2: Aguardar Build
```
Render está fazendo:
- Clone repositório
- Instalar dependências
- Executar build.sh
- Iniciar aplicação

Tempo: ~5 minutos
```

### [ ] Passo 7.3: Ver Logs
```
Dashboard → seu-app → Logs
Procurar por:
- "Building Docker image"
- "Running build script"
- "Listening on 0.0.0.0"
```

### [ ] Passo 7.4: Build completado?
```
Procurar por:
"✅ Application started successfully"

Se ver "Red X", há erro - ir para Troubleshooting
```

### [ ] Passo 7.5: Acessar aplicação
```
https://ecaa09-app.onrender.com
```

### [ ] Passo 7.6: Primeira carga
```
⏳ Pode levar 30 segundos
⏳ Se ver "Loading", aguardar

✅ Se carrega, funciona!
```

---

## FASE 8: TESTES BÁSICOS

### [ ] Teste 8.1: Homepage carrega
```
https://seu-app.onrender.com
Verificar: Página do Django aparece
```

### [ ] Teste 8.2: Login funciona
```
1. Clicar em Login
2. Entrar com usuário
3. Dashboard carrega
```

### [ ] Teste 8.3: Cadastro funciona
```
1. Se cliente: criar novo problema
2. Preencher título, descrição
3. Clicar "Salvar"
4. Verificar: dados salvam ✓
```

### [ ] Teste 8.4: Upload de imagem
```
1. Ao criar problema, selecionar imagem
2. Clicar upload
3. Verificar: imagem aparece
```

### [ ] Teste 8.5: Banco funciona
```
1. Criar 2-3 dados
2. Logout
3. Login novamente
4. Verificar: dados ainda existem
```

### [ ] Teste 8.6: Sem erros
```
1. Abrir DevTools (F12)
2. Ir para console
3. Verificar: sem erros vermelhos
```

---

## FASE 9: VERIFICAÇÃO FINAL

### [ ] Tudo funcionando?
```
✅ App carrega em https
✅ Login funciona
✅ Dados salvam
✅ Upload funciona
✅ Sem erros
```

### [ ] Sucesso!
```
🎉 Deploy bem-sucedido!
🎉 App online para sempre!
🎉 Compartilhe o link!
```

---

## 🆘 TROUBLESHOOTING RÁPIDO

### Se Build Falhou:
```
1. Ir para Logs
2. Procurar por "ERROR"
3. Procurar solução em: GUIA_DEPLOY_RENDER.md
```

### Se 500 Error:
```
1. Environment → DEBUG=True
2. Manual Deploy
3. Recarregar página
4. Ver erro detalhado
```

### Se Database Error:
```
1. Copiar DATABASE_URL novamente
2. Environment → atualizar DATABASE_URL
3. Manual Deploy
```

### Se Build Lento:
```
Render é grátis, às vezes é lento
Aguardar 5-10 minutos é normal
```

---

## 📊 PROGRESSO

```
Fase 1: ████████████░░░░░░░░ 60%
Fase 2: ████████████░░░░░░░░ 60%
Fase 3: ████████████░░░░░░░░ 60%
Fase 4: ████████████░░░░░░░░ 60%
Fase 5: ████████████░░░░░░░░ 60%
Fase 6: ████████████░░░░░░░░ 60%
Fase 7: ████████████░░░░░░░░ 60%
Fase 8: ████████████░░░░░░░░ 60%
Fase 9: ████████████░░░░░░░░ 60%

Total: 54% de 100 itens marcados

Continue marcando itens conforme completa!
```

---

## 🎊 PARABÉNS!

Se marcou todos os ✅, seu Django está ONLINE! 🚀

**Próximos passos:**
- [ ] Compartilhe o link com alguém
- [ ] Teste em mobile
- [ ] Convide outros usuários
- [ ] Continue desenvolvendo!

---

**Última atualização:** 2024  
**Status:** ✅ Pronto para usar

🚀 **Você consegue!**
