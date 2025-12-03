# 🎯 DEPLOY NO RENDER - GUIA PASSO A PASSO

## ⏱️ Tempo Estimado: 30 minutos

---

## 🔴 PASSO 1: Preparação Local (5 minutos)

### 1.1 Gerar `requirements.txt`
```bash
pip freeze > requirements.txt
```

**Verificar que contém:**
```
Django==5.2.0
Pillow==12.0.0
gunicorn>=22.0.0
whitenoise>=6.6.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
dj-database-url>=2.1.0
```

Se faltar algum, instale:
```bash
pip install gunicorn whitenoise psycopg2-binary python-dotenv dj-database-url
pip freeze > requirements.txt
```

### 1.2 Verificar arquivos criados
```bash
ls -la runtime.txt build.sh .env.example
```

Deve ter:
- ✅ `runtime.txt` (com python-3.12.0)
- ✅ `build.sh` (com permissão de execução)
- ✅ `.env.example` (exemplo de variáveis)

### 1.3 Testar Django em "produção"
```bash
DEBUG=False python manage.py collectstatic --noinput
DEBUG=False python manage.py check
```

Resultado esperado:
```
System check identified no issues (0 silenced).
✅ OK
```

---

## 🟢 PASSO 2: GitHub (3 minutos)

### 2.1 Commit das mudanças
```bash
git add requirements.txt runtime.txt build.sh .env.example
git commit -m "Preparar para deploy no Render.com"
git push origin develop
```

### 2.2 Verificar push
```bash
# Ir para GitHub
https://github.com/seu-usuario/ECAA09_Parte2-main
# Verificar se os arquivos estão lá
```

---

## 🟡 PASSO 3: Criar Banco de Dados PostgreSQL (5 minutos)

### 3.1 Ir para Render
- Abrir: https://render.com
- Login com GitHub (recomendado)

### 3.2 Criar PostgreSQL
```
Dashboard → New → PostgreSQL
```

### 3.3 Preencher Informações
```
Name: ecaa09-db
Database: ecaa09
User: postgres
Region: São Paulo (sa-south-1)
Plan: Free
```

### 3.4 Copiar Database URL
Depois de criado:
```
1. Clicar em "Connections"
2. Copiar "Internal Database URL"
3. Exemplo: postgresql://postgres:xyz@dpg-abc.render.internal:5432/ecaa09
```

**⚠️ Guardar esta URL - será usada no passo 5**

---

## 🔵 PASSO 4: Criar Web Service (3 minutos)

### 4.1 Ir para Dashboard Render
```
https://render.com/dashboard
```

### 4.2 Criar novo serviço
```
New → Web Service
```

### 4.3 Conectar GitHub (primeira vez)
```
1. "Connect Account"
2. Autorizar Render
3. Selecionar repository: ECAA09_Parte2-main
4. Clicar "Connect"
```

### 4.4 Preencher Informações
```
Name: ecaa09-app
Region: São Paulo (sa-south-1)
Branch: develop
Runtime: Python 3
Build Command: ./build.sh
Start Command: gunicorn oficina_prj.wsgi:application --bind 0.0.0.0:$PORT
```

**⚠️ Não clicar em "Create Service" ainda!**

---

## 🟣 PASSO 5: Configurar Variáveis de Ambiente (5 minutos)

### 5.1 Na mesma página do Render, rolar até "Environment"

### 5.2 Gerar SECRET_KEY
```bash
# Local, no terminal
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Copiar o output
# Exemplo: django-insecure-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### 5.3 Adicionar Variáveis
Na página do Render, em "Environment", adicionar cada uma (clique em "Add Environment Variable"):

| Key | Value |
|-----|-------|
| `DEBUG` | `False` |
| `SECRET_KEY` | (copiar do comando acima) |
| `DATABASE_URL` | (do passo 3.4) |
| `ALLOWED_HOSTS` | `ecaa09-app.onrender.com,localhost` |
| `RENDER_EXTERNAL_HOSTNAME` | `ecaa09-app.onrender.com` |

**⚠️ Substituir `ecaa09-app` pelo nome que você escolheu**

### 5.4 Verificar Variáveis
Deve aparecer assim:
```
✅ DEBUG: False
✅ SECRET_KEY: django-insecure-...
✅ DATABASE_URL: postgresql://...
✅ ALLOWED_HOSTS: ecaa09-app.onrender.com,localhost
✅ RENDER_EXTERNAL_HOSTNAME: ecaa09-app.onrender.com
```

---

## 🟠 PASSO 6: Deploy Inicial (5 minutos)

### 6.1 Clicar em "Create Web Service"
```
(último passo!)
```

### 6.2 Aguardar Build
```
Render faz:
1. Clone do repositório
2. Instalar dependências
3. Executar build.sh
4. Iniciar aplicação
```

Tempo: ~3-5 minutos

### 6.3 Ver Logs
```
1. Ir para: Seu serviço → Logs
2. Procurar por:
   - "Building Docker image"
   - "Running build script"
   - "Starting service"
   - "Listening on..."
```

### 6.4 Verificar se Sucesso
Log final esperado:
```
[SUCESSO] Starting gunicorn
Listening on 0.0.0.0:10000
✅ Application started successfully
```

Se houver erro, voltar ao [Troubleshooting](#troubleshooting)

---

## ✅ PASSO 7: Testar Aplicação (3 minutos)

### 7.1 Acessar URL
```
https://ecaa09-app.onrender.com
```

### 7.2 Primeira Carga
- Pode levar ~30 segundos
- Se vir "Application loading...", aguardar

### 7.3 Testes Básicos
- [ ] Homepage carrega
- [ ] Consegue fazer login
- [ ] Consegue cadastrar problema
- [ ] Consegue fazer upload de imagem
- [ ] Banco de dados funciona

### 7.4 Se Funcionar
```
🎉 PARABÉNS! Deploy bem-sucedido!
```

---

## 🆘 TROUBLESHOOTING

### ❌ Erro: Build Falhou

**Ver Logs:**
```
Dashboard → Seu Serviço → Logs
```

**Erro Comum 1: Static Files**
```
ModuleNotFoundError: No module named 'whitenoise'
```
Solução:
```bash
# Local
pip install whitenoise
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add whitenoise"
git push origin develop
```

**Erro Comum 2: Database**
```
psycopg2.OperationalError: could not connect to server
```
Solução:
- Verificar DATABASE_URL está correto
- Verificar PostgreSQL foi criado
- Tentar novamente

**Erro Comum 3: SECRET_KEY**
```
Configuration Error: SECRET_KEY not found
```
Solução:
- Ir para Environment
- Adicionar SECRET_KEY novamente
- Manual Deploy

### ❌ Erro: 500 Internal Server Error

**Debug:**
```
1. Ir para Logs
2. Procurar por erro específico
3. Se tiver "DEBUG=True", ativa modo debug:
   - Environment → DEBUG=True
   - Manual Deploy
   - Recarregar página
   - Ver erro detalhado
   - Voltar DEBUG=False
```

### ❌ Erro: Database Connection

**Verificar:**
```
1. PostgreSQL está rodando?
   - Render Dashboard → Seu DB → aba "Overview"
   
2. DATABASE_URL está correto?
   - Copiar novamente de: Database → Connections → Internal Database URL
```

### ❌ Erro: Page Not Found / 404

**Solução:**
```bash
# Local
python manage.py collectstatic --noinput
git add staticfiles/
git commit -m "Add static files"
git push origin develop
```

---

## 🔄 DEPOIS DO DEPLOY (Manutenção)

### Atualizar Código
```bash
# Local
# Fazer mudanças
git add .
git commit -m "Descrição das mudanças"
git push origin develop

# No Render
# Deploy automático em ~1 minuto
# Ver em: Dashboard → Seu Serviço → Deploy log
```

### Redeployar Manualmente
```
Se precisar forçar redeploy:
Dashboard → Seu Serviço → Manual Deploy → Deploy Latest Commit
```

### Ver Logs em Tempo Real
```
Dashboard → Seu Serviço → Logs → Live
```

### Monitorar Performance
```
Dashboard → Seu Serviço → Metrics
Ver: CPU, Memória, Requisições, Tempo de resposta
```

---

## 💾 BACKUP DO BANCO

### Fazer Backup
```
Dashboard → Seu PostgreSQL → Backups → Download Latest Backup
```

### Restaurar (em caso de problema)
```
Entre em contato com Render ou:
Dashboard → PostgreSQL → Backups → Restore from backup
```

---

## 📋 Checklist Final

- [ ] `requirements.txt` atualizado
- [ ] `runtime.txt` criado (python-3.12.0)
- [ ] `build.sh` criado
- [ ] `.env.example` criado
- [ ] Código com commit no GitHub
- [ ] PostgreSQL criado no Render
- [ ] Web Service criado no Render
- [ ] Variáveis de ambiente definidas
- [ ] Build completado com sucesso
- [ ] Aplicação acessível
- [ ] Testes básicos passam
- [ ] Logs sem erros
- [ ] Database funcionando
- [ ] Upload de imagens funciona
- [ ] Login/Cadastro funciona

---

## 🎉 Pronto!

Sua aplicação Django está no ar! 🚀

**URL:** `https://ecaa09-app.onrender.com`

---

## 📞 Dúvidas?

| Problema | Solução |
|----------|---------|
| Não consegue fazer login | Verificar DATABASE_URL |
| Imagens não aparecem | Upload funciona? |
| Build falha | Ver Logs → procurar erro |
| Página branca | DEBUG=True e ver erro |

---

**Versão:** 1.0  
**Data:** 2024  
**Status:** ✅ Pronto!
