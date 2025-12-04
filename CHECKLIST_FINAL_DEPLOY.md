# 📋 CHECKLIST FINAL - DEPLOY RENDER

## LOCAL (Sua Máquina)

### Python & Django
- [x] Python 3.12 instalado
- [x] Virtual environment ativo
- [x] Django 5.2.9 instalado
- [x] Todos os pacotes do requirements.txt instalados

### Configuração
- [x] settings.py corrigido para produção
- [x] requirements.txt atualizado
- [x] runtime.txt criado
- [x] build.sh criado
- [x] .env local criado (para testes)

### Testes Locais
- [x] `python manage.py check` - PASSOU
- [x] `python manage.py migrate` - PASSOU
- [x] `python manage.py collectstatic` - PASSOU
- [x] Modelos carregam corretamente
- [x] Banco de dados conecta

### Git/GitHub
- [x] Código commitado
- [x] Código enviado para GitHub (branch: main)

---

## RENDER.COM (Próximo passo)

### Account & Setup
- [ ] 1. Criar conta em https://render.com
- [ ] 2. Conectar GitHub account
- [ ] 3. Autorizar acesso ao repositório

### Banco de Dados PostgreSQL
- [ ] 1. Ir para Dashboard → New → PostgreSQL
- [ ] 2. Nome: ecaa09-db (ou similar)
- [ ] 3. Copiar DATABASE_URL após criação
- [ ] 4. Guardar URL em lugar seguro

### Web Service
- [ ] 1. Dashboard → New → Web Service
- [ ] 2. Conectar repositório: receitas-trabalho
- [ ] 3. Branch: main
- [ ] 4. Nome do serviço: pedrocosta-django
- [ ] 5. Runtime: Python 3
- [ ] 6. Build Command: `./build.sh`
- [ ] 7. Start Command: `gunicorn oficina_prj.wsgi:application --bind 0.0.0.0:$PORT`

### Environment Variables
- [ ] 1. Na aba Environment do Web Service:
  - [ ] DEBUG: `False`
  - [ ] SECRET_KEY: `67yufc+ty96$#k#c753_%@np$&l+31afvt@t**sv60%gm+r2)2`
  - [ ] DATABASE_URL: (sua PostgreSQL URL)
  - [ ] ALLOWED_HOSTS: `pedrocosta-django.onrender.com`

### Deploy
- [ ] 1. Clicar "Create Web Service"
- [ ] 2. Aguardar build (3-5 minutos)
- [ ] 3. Ver logs para verificar:
  - [ ] Build iniciou
  - [ ] Dependências instaladas
  - [ ] build.sh executou
  - [ ] Migrations aplicadas
  - [ ] Static files coletados
  - [ ] Servidor iniciou

### Testes em Produção
- [ ] 1. Acessar https://pedrocosta-django.onrender.com
- [ ] 2. Homepage carrega
- [ ] 3. Conseguir fazer login
- [ ] 4. Conseguir cadastrar problema
- [ ] 5. Conseguir fazer upload de imagem
- [ ] 6. Banco de dados persiste dados

### Performance
- [ ] 1. Ver em Dashboard → Metrics
- [ ] 2. CPU, Memória e requisições parecem OK
- [ ] 3. Tempo de resposta < 1s

---

## ⚠️ Possíveis Problemas & Soluções

### Se não conseguir carregar página:
```
1. Ver Logs no Render
2. Procurar por error/ERROR/Traceback
3. Verificar ALLOWED_HOSTS
4. Verificar DATABASE_URL está correto
5. Fazer Manual Deploy novamente
```

### Se banco de dados não conectar:
```
1. Verificar PostgreSQL está rodando no Render
2. Verificar DATABASE_URL foi copiada corretamente
3. Tentar recriar PostgreSQL
4. Verificar credenciais
```

### Se imagens não aparecem:
```
1. Verificar MEDIA_URL e MEDIA_ROOT em settings.py
2. Upload funciona localmente?
3. Em produção: considerar usar S3
```

### Se static files aparecem quebrados:
```
1. Verificar se collectstatic rodou
2. Ver build.sh foi executado
3. Verificar STATIC_ROOT e STATICFILES_STORAGE
4. Manual Deploy novamente
```

---

## 🎯 Resumo Rápido do Fluxo

```
1. Você aqui! ✓
         ↓
2. Ir para Render Dashboard
         ↓
3. Criar PostgreSQL
         ↓
4. Criar Web Service
         ↓
5. Adicionar Environment Variables
         ↓
6. Deploy
         ↓
7. Aguardar 5 minutos
         ↓
8. Acessar https://pedrocosta-django.onrender.com
         ↓
9. SUCESSO! 🎉
```

---

## 📞 Dúvidas?

Verifique o arquivo: `DIAGNOSTICO_DEPLOY_RENDER.md` para mais detalhes!

---

**Status:** PRONTO PARA IR PARA RENDER.COM  
**Próximo Passo:** https://dashboard.render.com  
**Tempo Estimado:** ~15 minutos  
**Data:** 2025-12-03
