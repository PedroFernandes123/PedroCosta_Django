# 🎯 GETTING STARTED - Tela de Cadastro

## ✨ Bem-vindo! Comece por aqui.

Você recebeu uma **tela de cadastro personalizada pronta para usar**!

Este arquivo te guia em **3 passos simples** para começar.

---

## 🚀 Passo 1: Preparar (2 minutos)

### Criar Especialidades
```bash
# Abrir Django Shell
python manage.py shell
```

```python
from core.models import Especialidade

# Criar algumas especialidades
Especialidade.objects.create(nome="Mecânica Geral")
Especialidade.objects.create(nome="Eletrônica Automotiva")
Especialidade.objects.create(nome="Funilaria e Pintura")
Especialidade.objects.create(nome="Alinhamento e Balanceado")
Especialidade.objects.create(nome="Sistema de Freios")

# Verificar
print(Especialidade.objects.count())  # Deve mostrar 5

# Sair
exit()
```

### Executar Migrações (se necessário)
```bash
python manage.py migrate
```

---

## 🎮 Passo 2: Rodar (1 minuto)

### Iniciar o Servidor
```bash
python manage.py runserver
```

Você deve ver algo como:
```
Django version 5.2, using settings 'oficina_prj.settings'
Starting development server at http://127.0.0.1:8000/
```

---

## 🧪 Passo 3: Testar (2 minutos)

### Abrir no Navegador

1. **Abra**: `http://localhost:8000/`
2. **Clique**: "Cadastro" (na navbar superior)
3. **Escolha**: "Cadastrar como Cliente" ou "Cadastrar como Oficina"
4. **Preencha**: O formulário com dados de teste
5. **Envie**: Clique "Confirmar Cadastro"

✅ **Pronto!** Você deve ser redirecionado para o dashboard correspondente.

---

## 📋 Teste Rápido de Cliente

```
Username: cliente_teste
Email: cliente@teste.com
Nome: João Silva
Senha: SenhaSegura123!
Confirmar: SenhaSegura123!

↓ Clica em "Confirmar Cadastro"
↓ Redireciona para /painel/cliente/
✅ Sucesso!
```

---

## 📋 Teste Rápido de Oficina

```
Username: oficina_teste
Email: oficina@teste.com
Nome: Meu Negócio
Senha: SenhaSegura123!
Confirmar: SenhaSegura123!

Nome da Oficina: AutoFix Mecânica
Endereço: Rua das Flores, 123
Especialidades: ☑ Mecânica Geral
                ☑ Sistema de Freios
                ☑ Alinhamento

↓ Clica em "Confirmar Cadastro"
↓ Redireciona para /painel/oficina/
✅ Sucesso!
```

---

## 🎯 O Que Você Pode Fazer Agora

### Usar Imediatamente
- ✅ Acessar `/cadastro/` para tela de escolha
- ✅ Cadastrar clientes
- ✅ Cadastrar oficinas
- ✅ Fazer login com novos usuários

### Explorar a Documentação
- 📖 Leia `QUICK_START.md` para mais detalhes
- 📖 Leia `DOCUMENTACAO_CADASTRO.md` para documentação completa
- 🎨 Veja `FLUXO_VISUAL_CADASTRO.md` para mockups
- 🧪 Use `GUIA_TESTES.md` para testar tudo

### Personalizar
- 🎨 Leia `GUIA_PERSONALIZACAO.md` para 20 ideias
- 🎨 Mudar cores, ícones, textos
- 🎨 Adicionar campos novos
- 🎨 Integrar com serviços externos

### Deploy
- 🚀 Leia `CHECKLIST_DEPLOYMENT.md` antes de ir para produção
- 🚀 Seguir todos os passos de segurança

---

## 🗺️ Mapa de Navegação

```
Home (/):
  ├─ Botão "Cadastro" → /cadastro/
  ├─ Botão "Entrar" → /login/
  ├─ Card "Para Clientes" → /cadastro/cliente/
  └─ Card "Para Oficinas" → /cadastro/oficina/

Cadastro (/cadastro/):
  ├─ Card "Cliente" → /cadastro/cliente/
  └─ Card "Oficina" → /cadastro/oficina/

Cadastro Cliente (/cadastro/cliente/):
  └─ Enviar → /painel/cliente/

Cadastro Oficina (/cadastro/oficina/):
  └─ Enviar → /painel/oficina/

Login (/login/):
  └─ Enviar → Home ou Dashboard
```

---

## 🔍 Verificar que Está Funcionando

### No Navegador
1. ✅ Página home mostra botão "Cadastro"
2. ✅ Clicando em "Cadastro" mostra dois cards
3. ✅ Cards têm ícones (👤 e 🔧)
4. ✅ Cards têm botões de ação
5. ✅ Formulários carregam corretamente
6. ✅ Campos aparecem conforme o tipo

### No Admin Django
1. Ir para `http://localhost:8000/admin/`
2. Login com credenciais de superuser
3. Verificar na seção "Users":
   - Novo cliente com `is_cliente=True`
   - Nova oficina com `is_oficina=True`
4. Verificar na seção "Perfil Oficina":
   - Novo perfil criado automaticamente
   - Especialidades associadas

### No Django Shell
```bash
python manage.py shell
```

```python
from core.models import User, PerfilOficina

# Contar usuarios
print(f"Total de usuários: {User.objects.count()}")
print(f"Clientes: {User.objects.filter(is_cliente=True).count()}")
print(f"Oficinas: {User.objects.filter(is_oficina=True).count()}")

# Ver último usuário criado
ultimo = User.objects.latest('date_joined')
print(f"Último: {ultimo.username} - Cliente: {ultimo.is_cliente}, Oficina: {ultimo.is_oficina}")

# Ver perfis de oficina
print(f"Perfis de Oficina: {PerfilOficina.objects.count()}")

# Ver especialidades da primeira oficina
if PerfilOficina.objects.exists():
    perfil = PerfilOficina.objects.first()
    print(f"Oficina: {perfil.nome_oficina}")
    print(f"Especialidades: {list(perfil.especialidades.values_list('nome', flat=True))}")

exit()
```

---

## 🆘 Problemas Comuns

### Erro: "No Especialidade objects"
```bash
# Solução: Criar especialidades
python manage.py shell
>>> from core.models import Especialidade
>>> Especialidade.objects.create(nome="Mecânica Geral")
>>> exit()
```

### Erro: "Campo não existe"
```bash
# Solução: Fazer migrações
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### CSS/Icons não aparecem
```bash
# Solução: Coletar static files
python manage.py collectstatic --no-input
python manage.py runserver
```

### Botão de cadastro não aparece
```bash
# Verificar arquivo base.html
# Deve ter algo como:
# <a href="{% url 'signup' %}" class="btn btn-primary btn-sm">
```

### Formulário de oficina sem campos dinâmicos
```bash
# Verificar signup.html
# Deve ter condicional:
# {% if is_oficina %}
```

---

## 📞 Próximas Etapas

### Curto Prazo (hoje)
- [ ] Criar especialidades ✅ (Passo 1)
- [ ] Rodar servidor ✅ (Passo 2)
- [ ] Testar cadastro ✅ (Passo 3)
- [ ] Verificar dados no admin
- [ ] Fazer alguns cadastros de teste

### Médio Prazo (esta semana)
- [ ] Ler documentação completa
- [ ] Testar todos os fluxos
- [ ] Personalizar conforme necessário
- [ ] Fazer testes de segurança

### Longo Prazo (antes de produção)
- [ ] Fazer testes de performance
- [ ] Seguir checklist de deployment
- [ ] Configurar monitoramento
- [ ] Fazer backup
- [ ] Deploy em produção

---

## 📚 Documentação Rápida

### Começar
- **[QUICK_START.md](QUICK_START.md)** - 5 minutos

### Aprofundar
- **[DOCUMENTACAO_CADASTRO.md](DOCUMENTACAO_CADASTRO.md)** - 15 minutos
- **[FLUXO_VISUAL_CADASTRO.md](FLUXO_VISUAL_CADASTRO.md)** - 10 minutos

### Testar
- **[GUIA_TESTES.md](GUIA_TESTES.md)** - 20 minutos

### Personalizar
- **[GUIA_PERSONALIZACAO.md](GUIA_PERSONALIZACAO.md)** - 25 minutos

### Deploy
- **[CHECKLIST_DEPLOYMENT.md](CHECKLIST_DEPLOYMENT.md)** - 15 minutos

### Índice
- **[INDICE.md](INDICE.md)** - Mapa de toda documentação

---

## ✅ Checklist de Início

- [ ] Especialidades criadas (Passo 1)
- [ ] Servidor rodando (Passo 2)
- [ ] Home page acessível
- [ ] Página `/cadastro/` funcionando
- [ ] Dois cards visíveis
- [ ] Formulário de cliente funciona
- [ ] Formulário de oficina funciona
- [ ] Dados aparecem no admin
- [ ] Documentação lida

---

## 🎉 Você está pronto!

Parabéns! Você tem uma tela de cadastro profissional e completa!

### Próximo: Leia um dos documentos
1. Rápido? → [QUICK_START.md](QUICK_START.md)
2. Detalhado? → [DOCUMENTACAO_CADASTRO.md](DOCUMENTACAO_CADASTRO.md)
3. Segurança? → [CHECKLIST_DEPLOYMENT.md](CHECKLIST_DEPLOYMENT.md)
4. Testes? → [GUIA_TESTES.md](GUIA_TESTES.md)

---

**Bom desenvolvimento!** 🚀

Qualquer dúvida, consulte os arquivos de documentação inclusos.
