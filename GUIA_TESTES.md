# 🧪 Guia de Testes - Tela de Cadastro Personalizada

## ✅ Checklist de Testes

### 1. Tela de Escolha (Signup Choice)
- [ ] Acessar `/cadastro/` sem estar logado
- [ ] Ver dois cards: Cliente e Oficina
- [ ] Clicar em "Cadastrar como Cliente" redireciona para `/cadastro/cliente/`
- [ ] Clicar em "Cadastrar como Oficina" redireciona para `/cadastro/oficina/`
- [ ] Botão "Voltar" aparece em ambos os formulários
- [ ] Design responsivo em mobile, tablet e desktop

### 2. Cadastro de Cliente
- [ ] Formulário mostra campos: Username, Email, Nome, Senha, Confirmar Senha
- [ ] Campo email é obrigatório
- [ ] Mensagens de erro aparecem para senhas que não combinam
- [ ] Após cadastro bem-sucedido:
  - [ ] Usuário é marcado com `is_cliente=True`
  - [ ] Usuário é marcado com `is_oficina=False`
  - [ ] Usuário é redirecionado para `/painel/cliente/`
  - [ ] Usuário fica automaticamente logado
- [ ] Nome de usuário único é validado
- [ ] Email único é validado

### 3. Cadastro de Oficina
- [ ] Formulário mostra campos básicos + informações da oficina
- [ ] Campos específicos aparecem:
  - [ ] Nome da Oficina (obrigatório)
  - [ ] Endereço (obrigatório)
  - [ ] Especialidades (checkboxes, obrigatório selecionar pelo menos 1)
- [ ] Após cadastro bem-sucedido:
  - [ ] Usuário é marcado com `is_oficina=True`
  - [ ] Usuário é marcado com `is_cliente=False`
  - [ ] Perfil de Oficina é criado automaticamente
  - [ ] Especialidades são associadas ao perfil
  - [ ] Usuário é redirecionado para `/painel/oficina/`
  - [ ] Usuário fica automaticamente logado
- [ ] Especialidades estão preenchidas (deve existir pelo menos 1)
- [ ] Validação de campos obrigatórios funciona

### 4. Navbar e Links
- [ ] Navbar mostra "Entrar" e "Cadastro" quando não autenticado
- [ ] Navbar mostra "Olá, [username]" e "Sair" quando autenticado
- [ ] Link "Cadastro" no navbar leva para `/cadastro/`
- [ ] Ícones aparecem corretamente com Font Awesome
- [ ] Responsividade do navbar em mobile (menu hambúrguer)

### 5. Home Page
- [ ] Mostra dois cards (Para Oficinas e Para Clientes)
- [ ] Botões "Cadastrar Cliente" e "Cadastrar Oficina" aparecem
- [ ] Usuário logado vê botão para seu painel
- [ ] Redirecionamentos funcionam

### 6. Integração com Dashboards
- [ ] Cliente cadastrado consegue acessar `/painel/cliente/`
- [ ] Oficina cadastrada consegue acessar `/painel/oficina/`
- [ ] Cliente não consegue acessar `/painel/oficina/` (redirecionamento)
- [ ] Oficina não consegue acessar `/painel/cliente/` (redirecionamento)

### 7. Validações de Segurança
- [ ] CSRF token em todos os formulários
- [ ] Senhas não são exibidas em texto plano
- [ ] Usuários não autenticados não conseguem acessar dashboards (login_required)
- [ ] Mensagens de erro não revelam senhas

### 8. Banco de Dados
- [ ] Novo usuário cliente tem `is_cliente=True` e `is_oficina=False`
- [ ] Novo usuário oficina tem `is_oficina=True` e `is_cliente=False`
- [ ] Perfil de Oficina é criado no banco de dados
- [ ] Especialidades são associadas corretamente

## 🚀 Passos para Testar

### Teste 1: Cadastro de Cliente
```bash
1. Ir para http://localhost:8000/
2. Clicar em "Criar Conta" ou "Cadastro"
3. Clicar em "Cadastrar como Cliente"
4. Preencher formulário:
   - Username: cliente_teste
   - Email: cliente@teste.com
   - Nome: João Silva (opcional)
   - Senha: senhaSegura123!
   - Confirmar Senha: senhaSegura123!
5. Clicar em "Confirmar Cadastro"
6. Verificar se foi redirecionado para /painel/cliente/
7. Verificar no admin se is_cliente=True
```

### Teste 2: Cadastro de Oficina
```bash
1. Fazer logout se necessário
2. Ir para http://localhost:8000/cadastro/
3. Clicar em "Cadastrar como Oficina"
4. Preencher formulário:
   - Username: oficina_teste
   - Email: oficina@teste.com
   - Nome: Meu Negócio (opcional)
   - Senha: senhaSegura123!
   - Confirmar Senha: senhaSegura123!
   - Nome da Oficina: AutoFix Mecânica
   - Endereço: Rua das Flores, 123
   - Especialidades: Selecionar 2 ou mais
5. Clicar em "Confirmar Cadastro"
6. Verificar se foi redirecionado para /painel/oficina/
7. Verificar no admin se is_oficina=True
8. Verificar se PerfilOficina foi criado com especialidades
```

### Teste 3: Erros de Validação
```bash
1. Tentar cadastrar com username já existente
2. Tentar cadastrar com email inválido
3. Tentar cadastrar com senhas que não combinam
4. Tentar cadastrar oficina sem especialidades
5. Tentar cadastrar oficina sem nome
```

## 📊 Comandos Úteis no Django Shell

```python
# Listar todos os clientes
from core.models import User
User.objects.filter(is_cliente=True)

# Listar todas as oficinas
User.objects.filter(is_oficina=True)

# Ver perfil de uma oficina
from core.models import PerfilOficina
PerfilOficina.objects.all()

# Ver especialidades de uma oficina
oficina = PerfilOficina.objects.first()
oficina.especialidades.all()

# Contar usuários por tipo
print(f"Clientes: {User.objects.filter(is_cliente=True).count()}")
print(f"Oficinas: {User.objects.filter(is_oficina=True).count()}")
```

## 🔍 Verificações no Admin Django

1. Acessar `http://localhost:8000/admin/`
2. Verificar na seção "Users":
   - Novos clientes com `is_cliente` marcado
   - Novas oficinas com `is_oficina` marcado
3. Verificar na seção "Perfil Oficina":
   - Perfis criados automaticamente
   - Especialidades associadas

## 📱 Testes de Responsividade

- [ ] Chrome Desktop (1920x1080)
- [ ] Chrome Tablet (768x1024)
- [ ] Chrome Mobile (375x667)
- [ ] Firefox Desktop
- [ ] Safari Desktop
- [ ] Safari Mobile (iPhone)

## 🐛 Problemas Conhecidos a Verificar

- Especialidades vazias causam erro?
- Redirecionamento funciona após erro de validação?
- Mensagens de sucesso aparecem?
- Styling CSS aplica corretamente em todos os navegadores?

## ✅ Checklist Final

- [ ] Todos os testes passaram
- [ ] Não há erros no console do navegador
- [ ] Não há erros no terminal Django
- [ ] Banco de dados possui dados corretos
- [ ] URLs funcionam conforme esperado
- [ ] Segurança CSRF implementada
- [ ] Validações funcionam
- [ ] Responsividade em todos os tamanhos
- [ ] Redirecionamentos inteligentes funcionam
- [ ] Perfil de oficina criado automaticamente

---

**Todos os testes passaram?** 🎉 A implementação está pronta para produção!
