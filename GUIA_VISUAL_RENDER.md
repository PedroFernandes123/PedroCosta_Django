# 🌐 GUIA VISUAL - PRÓXIMOS PASSOS NO RENDER

## 📍 Você está aqui:

```
✅ Django configurado localmente
✅ Código no GitHub
✅ Documentação pronta
         ↓
⏳ PRÓXIMO: Configurar no Render.com
         ↓
🎯 RESULTADO: URL em produção funcionando
```

---

## 🎬 PASSO 1: Abra o Render Dashboard

**URL:** https://dashboard.render.com

**Você verá:**
```
┌─────────────────────────────────────────────┐
│  Render Dashboard                           │
│                                             │
│  Services                                   │
│  ├─ pedrocosta-django    [Web Service]     │
│  ├─ ecaa09-db            [PostgreSQL]      │
│                                             │
│  [New] [Manual Deploy] [Settings]          │
└─────────────────────────────────────────────┘
```

---

## 🎬 PASSO 2: Clique em seu Web Service

**Clique em:** `pedrocosta-django`

**Você verá:**
```
┌──────────────────────────────────────┐
│  pedrocosta-django                   │
│                                      │
│  Status: Building / Live             │
│  Deployed: Dec 3, 2025               │
│                                      │
│  [Logs] [Settings] [Environment]     │
│  [Metrics] [Plans] [Advanced]        │
│                                      │
│  Manual Deploy ▼                     │
└──────────────────────────────────────┘
```

---

## 🎬 PASSO 3: Clique em "Environment"

**Clique em:** `Environment` (aba)

**Você verá:**
```
┌───────────────────────────────────────────┐
│  Environment Variables                    │
│                                           │
│  [+ Add Environment Variable]             │
│                                           │
│  DEBUG                      False    [X]  │
│  SECRET_KEY                 ****    [X]  │
│  DATABASE_URL              ****    [X]  │
│  ALLOWED_HOSTS             ****    [X]  │
│                                           │
│  [Save]                                   │
└───────────────────────────────────────────┘
```

---

## 🎬 PASSO 4: ATUALIZAR DEBUG

1. **Clique no valor** de `DEBUG` (se tiver)
2. **Mude para:** `False`
3. **Clique fora** para confirmar

**Ficará assim:**
```
DEBUG = False  ✓
```

---

## 🎬 PASSO 5: ATUALIZAR ou ADICIONAR SECRET_KEY

### Se já existe:
1. Clique no ícone [X] para deletar
2. Clique [+ Add Environment Variable]

### Se não existe:
1. Clique [+ Add Environment Variable]

### Na nova linha:
```
Key:   SECRET_KEY
Value: 67yufc+ty96$#k#c753_%@np$&l+31afvt@t**sv60%gm+r2)2
```

**Ficará assim:**
```
SECRET_KEY = 67yufc+ty96$#k#c753_%@np$&l+31afvt@t**sv60%gm+r2)2  ✓
```

---

## 🎬 PASSO 6: VERIFICAR DATABASE_URL

**Deve estar assim:**
```
DATABASE_URL = postgresql://user:pass@host:5432/dbname  ✓
```

⚠️ Se não estiver:
1. Vá para seu PostgreSQL no Render
2. Clique em "Connections"
3. Copie "Internal Database URL"
4. Cole aqui em DATABASE_URL

---

## 🎬 PASSO 7: VERIFICAR ou ADICIONAR ALLOWED_HOSTS

### Se não existe:
1. Clique [+ Add Environment Variable]

### Na nova linha:
```
Key:   ALLOWED_HOSTS
Value: pedrocosta-django.onrender.com
```

**Ficará assim:**
```
ALLOWED_HOSTS = pedrocosta-django.onrender.com  ✓
```

---

## 🎬 PASSO 8: SALVAR (se necessário)

Se houver botão **[Save]**, clique nele!

```
✓ Variáveis atualizadas com sucesso
```

---

## 🎬 PASSO 9: MANUAL DEPLOY

1. **Volte** para a página principal do serviço
2. **Clique em** `Manual Deploy` (botão topo direito)
3. **Clique em** `Deploy latest commit`

**Você verá:**
```
┌─────────────────────────────────────┐
│  Building...                        │
│  (aguarde 5-10 minutos)            │
│                                    │
│  Logs:                             │
│  > Building Docker image...        │
│  > Running build script...         │
│  > Collecting dependencies...      │
│  > Applying migrations...          │
│  > Collecting static files...      │
│  > Starting service...             │
│  ✓ Live                            │
└─────────────────────────────────────┘
```

---

## 🎬 PASSO 10: AGUARDE O BUILD

### Tempo estimado: **5-10 minutos**

Enquanto aguarda, **procure no log por:**

```
✓ "Collecting static files"
✓ "Running migrations"
✓ "Listening on 0.0.0.0"
✓ "Service live"
```

Se ver **ERROR** ou **Traceback**, anote o erro e verifique DIAGNOSTICO_DEPLOY_RENDER.md

---

## 🎬 PASSO 11: TESTAR A URL

Quando o status mudar para **Live** (verde):

1. **Copie sua URL**: `https://pedrocosta-django.onrender.com`
2. **Abra em novo navegador**
3. **Aguarde 30 segundos** para carregar (primeira vez é lenta)

**Você verá:**
```
┌──────────────────────────────────────┐
│  Oficina App                         │
│                                      │
│  [Home] [Login] [Cadastrar]         │
│                                      │
│  Bem-vindo!                          │
│  Selecione uma opção acima...       │
└──────────────────────────────────────┘
```

---

## 🎯 TESTES A FAZER

Depois de abrir, teste:

```
□ 1. Homepage carrega normalmente
□ 2. Consegue clicar em [Login]
□ 3. Consegue clicar em [Cadastrar]
□ 4. Consegue fazer login com conta existente
□ 5. Dashboard de oficina carrega
□ 6. Consegue cadastrar novo problema
□ 7. Consegue fazer upload de imagem
□ 8. Imagem aparece no detalhe
□ 9. Consegue marcar interesse
□ 10. Dados persistem (recarregar página)
```

---

## ✅ SE TUDO PASSOU:

### 🎉 PARABÉNS! SUA APP ESTÁ NO AR!

```
┌─────────────────────────────────────┐
│  ✓ Django app live em produção     │
│  ✓ Banco de dados PostgreSQL OK     │
│  ✓ Arquivos estáticos funcionando   │
│  ✓ Uploads funcionando              │
│  ✓ Autenticação OK                  │
│                                     │
│  URL: pedrocosta-django.onrender.com
│                                     │
│  Status: PRONTO PARA USAR!          │
└─────────────────────────────────────┘
```

---

## ❌ SE ALGO DEU ERRADO:

### 1. Ver Logs:
```
Dashboard → pedrocosta-django → Logs → Ver erro completo
```

### 2. Erros comuns:

**Erro:** `DisallowedHost`
```
Solução: Verificar ALLOWED_HOSTS está igual ao seu domínio
```

**Erro:** `ProgrammingError`
```
Solução: Banco não sincronizou, fazer Manual Deploy novamente
```

**Erro:** `ModuleNotFoundError`
```
Solução: requirements.txt incompleto, verificar em GitHub
```

**Erro:** `404 em static files`
```
Solução: collectstatic não rodou, ver build log
```

### 3. Passos de debug:

1. Copiar erro do log
2. Verificar DIAGNOSTICO_DEPLOY_RENDER.md
3. Fazer Manual Deploy novamente
4. Se persistir: resetar ou recriar serviço

---

## 📞 CHECKLIST FINAL

```
□ SECRET_KEY copiada
□ Render Dashboard aberto
□ Web Service selecionado
□ Environment atualizadas:
  □ DEBUG = False
  □ SECRET_KEY = 67yufc+ty96...
  □ DATABASE_URL = postgresql://...
  □ ALLOWED_HOSTS = pedrocosta-django.onrender.com
□ Manual Deploy acionado
□ Build completou com sucesso
□ Status: Live (verde)
□ URL testada e funcionando
□ Todos os testes passaram
```

---

## 🚀 PRÓXIMOS PASSOS OPCIONAIS

Depois que tudo estiver funcionando:

1. **Domínio customizado** → Render DNS settings
2. **Email** → Configurar SMTP em settings.py
3. **S3 para uploads** → Para garantir persistência de imagens
4. **Backups** → Programar backups do PostgreSQL
5. **Monitoring** → Ver Metrics no dashboard

---

**Data:** 2025-12-03  
**Status:** PRONTO PARA DEPLOY  
**Tempo estimado:** 15 minutos até estar no ar  

🎯 **Agora é com você! Boa sorte!** 🚀
