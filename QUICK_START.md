# ⚡ Quick Start - Tela de Cadastro

## 🚀 Começar em 5 Minutos

### 1. Verificar Especialidades (2 min)
```bash
python manage.py shell
```

```python
from core.models import Especialidade

# Verificar se existem especialidades
Especialidade.objects.all()

# Se estiver vazio, criar algumas
Especialidade.objects.create(nome="Mecânica Geral")
Especialidade.objects.create(nome="Eletrônica Automotiva")
Especialidade.objects.create(nome="Funilaria e Pintura")
Especialidade.objects.create(nome="Alinhamento e Balanceado")
Especialidade.objects.create(nome="Sistema de Freios")
Especialidade.objects.create(nome="Suspensão")

exit()
```

### 2. Rodar Migrações (1 min)
```bash
python manage.py migrate
```

### 3. Iniciar Servidor (0.5 min)
```bash
python manage.py runserver
```

### 4. Testar (1.5 min)
Abrir navegador em `http://localhost:8000/`

- Clique em **"Cadastro"**
- Escolha **"Cliente"** ou **"Oficina"**
- Preencha o formulário
- Clique em **"Confirmar Cadastro"**

✅ **Pronto!** Seu novo usuário foi criado!

---

## 📋 Estrutura de Arquivos

```
proyecto/
├── core/
│   ├── forms.py           ← Formulários (Cliente + Oficina)
│   ├── views.py           ← Views (3 novas rotas)
│   ├── models.py          ← Modelos (sem mudanças)
│   └── ...
├── oficina_prj/
│   ├── urls.py            ← URLs atualizadas
│   ├── settings.py        ← Sem mudanças
│   └── ...
├── templates/
│   ├── base.html          ← Navbar atualizado
│   ├── core/
│   │   └── home.html      ← Home melhorada
│   └── registration/
│       ├── signup.html                ← Signup melhorado
│       └── signup_choice.html         ← ✨ NOVO
├── DOCUMENTACAO_CADASTRO.md           ← ✨ NOVO
├── FLUXO_VISUAL_CADASTRO.md           ← ✨ NOVO
├── GUIA_TESTES.md                     ← ✨ NOVO
├── GUIA_PERSONALIZACAO.md             ← ✨ NOVO
├── CHECKLIST_DEPLOYMENT.md            ← ✨ NOVO
├── RESUMO_IMPLEMENTACAO.md            ← ✨ NOVO
└── manage.py
```

---

## 🎯 Rotas Disponíveis

| URL | Descrição |
|-----|-----------|
| `/` | Home |
| `/cadastro/` | 👈 **Escolha entre Cliente ou Oficina** |
| `/cadastro/cliente/` | Formulário para Cliente |
| `/cadastro/oficina/` | Formulário para Oficina |
| `/login/` | Login |
| `/logout/` | Logout |
| `/painel/cliente/` | Dashboard do Cliente |
| `/painel/oficina/` | Dashboard da Oficina |
| `/admin/` | Admin Django |

---

## 📋 O que foi Mudado

### ✏️ Modificados:
1. **core/forms.py** - Novos formulários
2. **core/views.py** - Novas views (signup, signup_cliente, signup_oficina)
3. **oficina_prj/urls.py** - Novas rotas
4. **templates/base.html** - Navbar + Font Awesome
5. **templates/registration/signup.html** - Campos dinâmicos
6. **templates/core/home.html** - Links + Ícones

### ✨ Criados:
1. **templates/registration/signup_choice.html** - Tela de escolha

---

## 🔑 Recursos Principais

✅ **Dois tipos de cadastro** - Cliente e Oficina
✅ **Formulários específicos** - Cada tipo tem seus campos
✅ **Criação automática de perfil** - Para oficinas
✅ **Design responsivo** - Funciona em mobile/tablet/desktop
✅ **Segurança CSRF** - Proteção contra ataques
✅ **Validação de formulários** - Feedback de erro
✅ **Ícones Font Awesome** - Visual profissional
✅ **Bootstrap 5** - Layout moderno

---

## 🧪 Teste Rápido

### Teste 1: Cliente
```
1. Ir para /cadastro/
2. Clicar "Cadastrar como Cliente"
3. Preencher:
   - Username: cliente1
   - Email: cliente@teste.com
   - Senha: senha123!
4. Enviar
5. Verificar redirecionamento para /painel/cliente/
```

### Teste 2: Oficina
```
1. Ir para /cadastro/
2. Clicar "Cadastrar como Oficina"
3. Preencher:
   - Username: oficina1
   - Email: oficina@teste.com
   - Nome da Oficina: Minha Oficina
   - Endereço: Rua A, 123
   - Especialidades: selecionar 2+
4. Enviar
5. Verificar redirecionamento para /painel/oficina/
```

---

## 🐛 Solução de Problemas

### Erro: "Especialidades vazias"
```bash
# Solução: Criar especialidades
python manage.py shell
>>> from core.models import Especialidade
>>> Especialidade.objects.create(nome="Mecânica Geral")
>>> exit()
```

### Erro: "Campo X não existe"
```bash
# Solução: Fazer migrações
python manage.py makemigrations
python manage.py migrate
```

### CSS não aparece
```bash
# Solução: Coletar static files
python manage.py collectstatic --no-input
```

### Usuário não vê o botão de cadastro
```bash
# Verificar se está no base.html
# grep -r "signup" templates/
```

---

## 📊 Dados de Exemplo

**Cliente Teste:**
- Username: `cliente_teste`
- Email: `cliente@teste.com`
- Senha: `SenhaSegura123!`

**Oficina Teste:**
- Username: `oficina_teste`
- Email: `oficina@teste.com`
- Nome: `AutoFix Mecânica`
- Endereço: `Rua das Flores, 123`

---

## 🎨 Personalização Rápida

### Mudar cor do header
Arquivo: `templates/registration/signup.html`
```html
<div class="card-header bg-secondary text-white">
                          ↓ mudar aqui
                    bg-primary (azul)
                    bg-success (verde)
                    bg-danger (vermelho)
```

### Mudar ícone do card
Arquivo: `templates/registration/signup_choice.html`
```html
<div style="font-size: 3rem;">👤</div>
             ↓ mudar aqui
        Qualquer emoji
```

### Mudar texto
Arquivo: `templates/registration/signup_choice.html`
```html
"Tenho problemas com meu veículo e preciso de uma oficina"
↓ mudar para qualquer texto
```

---

## 📚 Documentação Completa

Para documentação detalhada, veja:
- 📖 `DOCUMENTACAO_CADASTRO.md` - Documentação técnica completa
- 🎨 `FLUXO_VISUAL_CADASTRO.md` - Mockups do fluxo
- 🧪 `GUIA_TESTES.md` - Como testar
- 🎯 `GUIA_PERSONALIZACAO.md` - Como personalizar
- 🚀 `CHECKLIST_DEPLOYMENT.md` - Deploy seguro
- 📋 `RESUMO_IMPLEMENTACAO.md` - Resumo das mudanças

---

## 🆘 Precisa de Ajuda?

1. **Verificar documentação** - Consulte os arquivos .md
2. **Rodar testes** - `python manage.py test`
3. **Check admin** - `http://localhost:8000/admin/`
4. **Ver logs** - `python manage.py runserver` mostra erros
5. **Django shell** - `python manage.py shell` para debug

---

## ✅ Checklist Inicial

- [ ] Especialidades criadas
- [ ] Migrações executadas
- [ ] Servidor rodando
- [ ] Página `/cadastro/` funcionando
- [ ] Cadastro de Cliente funcionando
- [ ] Cadastro de Oficina funcionando
- [ ] Usuários aparecendo no admin
- [ ] Dashboards acessíveis

---

**Tudo funcionando?** 🎉

Próximos passos:
1. Testar todos os fluxos
2. Personalizar conforme necessário
3. Fazer testes de segurança
4. Fazer deploy em produção
5. Monitorar uso

---

**Versão**: 1.0
**Última atualização**: 2 de Dezembro de 2024
