# ⚡ QUICK START - PRÓXIMOS 5 MINUTOS

## 🎯 O Que Você Precisa Fazer AGORA

```
TEMPO TOTAL: 5 minutos
```

---

## 📋 PASSO 1: Copiar a SECRET_KEY

```
SECRET_KEY gerada:
67yufc+ty96$#k#c753_%@np$&l+31afvt@t**sv60%gm+r2)2

👉 COPIE AGORA E GUARDE TEMPORARIAMENTE
```

---

## 📋 PASSO 2: Abrir Render Dashboard

👉 **Clique aqui:** https://dashboard.render.com

**Você verá:**
```
Dashboard
├─ pedrocosta-django (seu Web Service)
├─ ecaa09-db (seu PostgreSQL)
```

---

## 📋 PASSO 3: Abrir o Web Service

Clique em: **pedrocosta-django**

---

## 📋 PASSO 4: Ir para Environment

Procure pela aba: **Environment** (próximo a Settings)

---

## 📋 PASSO 5: Atualizar Variáveis

### Variable 1: DEBUG
```
Key: DEBUG
Value: False
```

### Variable 2: SECRET_KEY
```
Key: SECRET_KEY
Value: 67yufc+ty96$#k#c753_%@np$&l+31afvt@t**sv60%gm+r2)2
```

### Variable 3: DATABASE_URL
```
Key: DATABASE_URL
Value: postgresql://user:pass@host/db
```
(Já deve estar lá, não precisa mudar)

### Variable 4: ALLOWED_HOSTS
```
Key: ALLOWED_HOSTS
Value: pedrocosta-django.onrender.com
```

---

## 📋 PASSO 6: Salvar (se necessário)

Se houver botão **[Save]**, clique.

---

## 📋 PASSO 7: Manual Deploy

Procure pelo botão: **Manual Deploy** (topo da página)

Clique e depois clique: **Deploy latest commit**

---

## 📋 PASSO 8: Aguardar (5-10 minutos)

```
Status passará por:
🟡 Building...
🟡 Deploying...
🟢 Live ✅
```

Enquanto aguarda, procure nos logs por:
```
✓ Collecting static files
✓ Running migrations
✓ Starting Gunicorn
```

---

## 📋 PASSO 9: Testar URL

Quando status ficar **🟢 Live**, acesse:

👉 **https://pedrocosta-django.onrender.com**

**Você deve ver a homepage funcionando!**

---

## ✅ Testes Rápidos

Depois de abrir, teste rapidamente:

```
□ Homepage carrega?
□ Consegue clicar em Login?
□ Consegue fazer login?
□ Dashboard aparece?
```

---

## 🎉 Se Tudo Funcionar

Parabéns! Sua aplicação está LIVE! 🚀

---

## ❌ Se Algo Falhar

### Erro comum: DisallowedHost
```
Solução: ALLOWED_HOSTS está diferente
Vai para: Environment
Verifica se é: pedrocosta-django.onrender.com
```

### Erro comum: Database error
```
Solução: DATABASE_URL está incorreto
Vai para: Seu PostgreSQL
Copia Internal Database URL novamente
```

### Erro comum: Build failed
```
Solução: Ver logs completos
Dashboard → Logs → Procura "Error" ou "Traceback"
Se não conseguir resolver, ver DIAGNOSTICO_DEPLOY_RENDER.md
```

---

## 📞 Dúvidas?

Leia: **GUIA_VISUAL_RENDER.md** (mais detalhado com screenshots)

---

## ⏱️ Timeline

```
Agora:           Você inicia
        ↓
5 min:  Dashboard configurado
        ↓
10 min: Deploy iniciado (Render buildando)
        ↓
15 min: Status Live
        ↓
20 min: Testado e funcionando
        ↓
SUCESSO! 🎊
```

---

**Próximo:** https://dashboard.render.com

**Boa sorte!** 🚀
