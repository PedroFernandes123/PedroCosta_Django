# 🔄 DIAGRAMAS DE FLUXO - Tela de Cadastro

## 1️⃣ Fluxo Geral do Sistema

```
┌──────────────────────────────────────────────────────────────────────┐
│                         SISTEMA DE CADASTRO                          │
└──────────────────────────────────────────────────────────────────────┘

                            PÚBLICO
                         (não autenticado)
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 Home       Navbar       Footer
                  │       "Cadastro"    "Cadastro"
                  │           │             │
                  └───────────┴─────────────┘
                          ▼
                  /cadastro/ (GET)
                  signup_choice.html
                          │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ▼                                   ▼
   [👤 CLIENTE]                        [🔧 OFICINA]
          │                                   │
          ▼                                   ▼
/cadastro/cliente/              /cadastro/oficina/
   (GET → formulário)              (GET → formulário)
          │                                   │
          ▼ (POST com dados)                  ▼ (POST com dados)
    Validar formulário              Validar formulário
    ClienteSignUpForm               OficinaSignUpForm
          │                                   │
      VALIDO?                             VALIDO?
    ┌──┴──┐                           ┌──┴──┐
    │     │                           │     │
   NÃO   SIM                         NÃO   SIM
    │     │                           │     │
    ▼     ▼                           ▼     ▼
  Erro  Criar User              Erro  Criar User
  (redisplayer)            (redisplayer)  |
            │                             ├─ set is_oficina=True
            ├─ set is_cliente=True        ├─ Criar PerfilOficina
            └─────────┬──────────         ├─ Associar especialidades
                      │                   └─────────┬──────────
                      │                             │
                      ▼                             ▼
                   Login automático            Login automático
                      │                             │
       ┌──────────────┴──────────────┐             │
       │                             │             │
       ▼                             ▼             ▼
  /painel/cliente/            /painel/oficina/
  (Cliente logado)            (Oficina logada)
       │                             │
       ▼                             ▼
    AUTENTICADO                  AUTENTICADO
    (Cliente)                    (Oficina)
```

---

## 2️⃣ Fluxo Detalhado - Cadastro de Cliente

```
┌─────────────────────────────────────────────────────────────────┐
│                 CADASTRO DE CLIENTE                              │
└─────────────────────────────────────────────────────────────────┘

ETAPA 1: Acesso
─────────────────
User: Clica "Cadastro" na navbar/home
         ▼
Servidor: GET /cadastro/
         ▼
View: signup()
         ▼
Response: signup_choice.html (com 2 cards)
         ▼
User: Clica "Cadastrar como Cliente"
         ▼
Browser: GET /cadastro/cliente/

ETAPA 2: Carregamento do Formulário
─────────────────────────────────
Servidor: GET /cadastro/cliente/
         ▼
View: signup_cliente() - GET
         ▼
Form: ClienteSignUpForm()
         ▼
Template: signup.html (is_cliente=True)
         ▼
Response: Formulário vazio renderizado
         ▼
User: Vê formulário com campos:
      • Username
      • Email
      • Nome (opcional)
      • Senha
      • Confirmar Senha
      • [Confirmar Cadastro]

ETAPA 3: Preenchimento e Submissão
─────────────────────────────
User: Preenche os campos
       └─ username: "cliente1"
       └─ email: "cliente@teste.com"
       └─ first_name: "João" (opcional)
       └─ password1: "SenhaSegura123!"
       └─ password2: "SenhaSegura123!"
         ▼
User: Clica "Confirmar Cadastro"
         ▼
Browser: POST /cadastro/cliente/

ETAPA 4: Validação e Processamento
─────────────────────────────────
Servidor: POST /cadastro/cliente/
         ▼
View: signup_cliente() - POST
         ▼
Form: ClienteSignUpForm(data)
         ▼
Django: Validar
        ├─ Username único?
        ├─ Email válido?
        ├─ Email único?
        ├─ Senhas combinam?
        ├─ Senha forte?
        └─ Campos obrigatórios?
         ▼
      TUDO OK? Sim ▼
         
Form: save() → form.save(commit=False)
         ▼
Django: Criar User object
         ├─ username = "cliente1"
         ├─ email = "cliente@teste.com"
         ├─ first_name = "João"
         ├─ password_hash = hash("SenhaSegura123!")
         └─ is_cliente = True  ← IMPORTANTE
         ▼
Database: INSERT INTO core_user
         ▼
Django: user.save()
         ▼
Auth: login(request, user)
         ▼
Response: redirect('dashboard_cliente')
         ▼
Browser: GET /painel/cliente/
         ▼
View: dashboard_cliente() → @login_required
         ▼
Template: dashboard_cliente.html
         ▼
Response: Dashboard do cliente
         ▼
User: ✅ SUCESSO! Logado como cliente

ETAPA 5: Pós-Cadastro
──────────────────
User vê:
  ├─ Navbar: "Olá, cliente1" + "Sair"
  ├─ Dashboard com funcionalidades
  └─ Redirecionamento automático

Database State:
  ├─ User criado com is_cliente=True
  ├─ is_oficina=False
  ├─ Email confirmado
  └─ Session ativa
```

---

## 3️⃣ Fluxo Detalhado - Cadastro de Oficina

```
┌─────────────────────────────────────────────────────────────────┐
│                 CADASTRO DE OFICINA                              │
└─────────────────────────────────────────────────────────────────┘

[Mesmas ETAPAS 1-2 do Cliente]

ETAPA 3: Preenchimento e Submissão
─────────────────────────────
User: Preenche os campos BÁSICOS
       └─ username: "oficina1"
       └─ email: "oficina@teste.com"
       └─ first_name: "Meu Negócio"
       └─ password1: "SenhaSegura123!"
       └─ password2: "SenhaSegura123!"
         ▼
User: Preenche os campos DE OFICINA
       └─ nome_oficina: "AutoFix Mecânica"
       └─ endereco: "Rua das Flores, 123"
       └─ especialidades: [✓] Mecânica Geral
                          [✓] Sistema de Freios
                          [ ] Alinhamento
         ▼
User: Clica "Confirmar Cadastro"
         ▼
Browser: POST /cadastro/oficina/

ETAPA 4: Validação e Processamento
─────────────────────────────────
Servidor: POST /cadastro/oficina/
         ▼
View: signup_oficina() - POST
         ▼
Form: OficinaSignUpForm(data)
         ▼
Django: Validar
        ├─ Username único?
        ├─ Email válido?
        ├─ Email único?
        ├─ Senhas combinam?
        ├─ Senha forte?
        ├─ Nome oficina preenchido?
        ├─ Endereço preenchido?
        ├─ Especialidades selecionadas? (min 1)
        └─ Especialidades válidas?
         ▼
      TUDO OK? Sim ▼

Form: save(commit=False)
         ▼
Django: Criar User object
         ├─ username = "oficina1"
         ├─ email = "oficina@teste.com"
         ├─ first_name = "Meu Negócio"
         ├─ password_hash = hash("SenhaSegura123!")
         └─ is_oficina = True  ← IMPORTANTE
         ▼
Database: INSERT INTO core_user
         ▼
Django: PerfilOficina.objects.create()
         ├─ usuario = user (referência)
         ├─ nome_oficina = "AutoFix Mecânica"
         ├─ endereco = "Rua das Flores, 123"
         └─ [outros campos]
         ▼
Database: INSERT INTO core_perilofoicina
         ▼
Django: perfil.especialidades.set([...])
         ├─ Especialidade(1) = "Mecânica Geral"
         └─ Especialidade(2) = "Sistema de Freios"
         ▼
Database: INSERT INTO core_perilofoicina_especialidades
         ▼
Auth: login(request, user)
         ▼
Response: redirect('dashboard_oficina')
         ▼
Browser: GET /painel/oficina/
         ▼
View: dashboard_oficina() → @login_required
         ▼
Template: dashboard_oficina.html
         ▼
Response: Dashboard da oficina
         ▼
User: ✅ SUCESSO! Logado como oficina

ETAPA 5: Pós-Cadastro
──────────────────
User vê:
  ├─ Navbar: "Olá, oficina1" + "Sair"
  ├─ Dashboard com funcionalidades
  ├─ Serviços disponíveis para pegar
  └─ Redirecionamento automático

Database State:
  ├─ User criado com is_oficina=True
  ├─ is_cliente=False
  ├─ PerfilOficina criado
  ├─ Especialidades associadas
  └─ Session ativa
```

---

## 4️⃣ Fluxo de Validação

```
┌─────────────────────────────────────────────────────────────────┐
│            VALIDAÇÃO DE FORMULÁRIOS                              │
└─────────────────────────────────────────────────────────────────┘

CLIENT SIDE (JavaScript/HTML5)
┌──────────────────────────────────
│ Input type validation
├─ email: type="email"
├─ password: type="password"
├─ text: required attribute
└─ Select: required attribute

SERVER SIDE (Django)
┌──────────────────────────────────
│ Form.is_valid() → Valida:
├─ Email format (email validator)
├─ Username format (django native)
├─ Username unique (DB query)
├─ Email unique (DB query)
├─ Password length (min 8 chars)
├─ Password complexity (numbers, symbols, etc)
├─ Passwords match (clean_password2)
├─ Especialidades (Model validator)
├─ Especialidades count > 0
└─ Name length (if required)

ERROS POSSÍVEIS
┌──────────────────────────────────
├─ "Username already exists"
├─ "Email already registered"
├─ "Password too short"
├─ "Passwords don't match"
├─ "Invalid email"
├─ "This field is required"
├─ "Please select at least one specialty"
└─ [Email username similarity warning]

RESPONSE APÓS VALIDAÇÃO
┌──────────────────────────────────
│
├─ Se inválido → Redisplayer formulário
│               com mensagens de erro
│               em vermelho destacadas
│
└─ Se válido → Salvar e
              Redirect para dashboard
```

---

## 5️⃣ Fluxo de Autenticação

```
┌─────────────────────────────────────────────────────────────────┐
│            FLUXO DE AUTENTICAÇÃO                                 │
└─────────────────────────────────────────────────────────────────┘

APÓS CADASTRO BEM-SUCEDIDO
┌────────────────────────────
│ form.save() → User criado
│      ▼
│ login(request, user)
│      ▼
│ Django Auth Backend:
│  ├─ Create session
│  ├─ Set session cookie
│  ├─ Update request.user
│  └─ Mark user as authenticated
│      ▼
│ redirect('dashboard_cliente/oficina')
│      ▼
│ Browser: GET /painel/cliente/
│      ▼
│ View: @login_required
│  ├─ Verifica request.user.is_authenticated
│  └─ Permite acesso se True
│      ▼
│ Template renderizado
│      ▼
│ User vê dashboard com dados pessoais

REDIRECIONAMENTO INTELIGENTE
┌────────────────────────────
│ if user.is_cliente:
│    redirect('dashboard_cliente')
│ elif user.is_oficina:
│    redirect('dashboard_oficina')
│ else:
│    redirect('home')

SEGURANÇA
┌────────────────────────────
│ ✅ Senha hasheada (PBKDF2)
│ ✅ Session timeout (Django default)
│ ✅ Session data server-side
│ ✅ CSRF token validado
│ ✅ Secure cookie flags
│ ✅ HttpOnly flag set
│ ✅ SameSite=Lax (default)
```

---

## 6️⃣ Fluxo de Dados no Banco

```
┌─────────────────────────────────────────────────────────────────┐
│            ARMAZENAMENTO DE DADOS                                │
└─────────────────────────────────────────────────────────────────┘

CLIENTE
┌──────────────────────────────────
│ Tabela: core_user
│ ├─ id: 1
│ ├─ username: "cliente1"
│ ├─ email: "cliente@teste.com"
│ ├─ first_name: "João"
│ ├─ last_name: ""
│ ├─ password: "pbkdf2_sha256$...[hash]"
│ ├─ is_active: True
│ ├─ is_staff: False
│ ├─ is_superuser: False
│ ├─ is_cliente: True  ← IMPORTANTE
│ ├─ is_oficina: False
│ ├─ date_joined: 2024-12-02 10:00:00
│ └─ last_login: 2024-12-02 10:00:05

OFICINA
┌──────────────────────────────────
│ Tabela: core_user
│ ├─ id: 2
│ ├─ username: "oficina1"
│ ├─ email: "oficina@teste.com"
│ ├─ first_name: "Meu Negócio"
│ ├─ last_name: ""
│ ├─ password: "pbkdf2_sha256$...[hash]"
│ ├─ is_active: True
│ ├─ is_staff: False
│ ├─ is_superuser: False
│ ├─ is_cliente: False
│ ├─ is_oficina: True  ← IMPORTANTE
│ ├─ date_joined: 2024-12-02 10:05:00
│ └─ last_login: 2024-12-02 10:05:10
│
│ Tabela: core_perilofoicina
│ ├─ id: 1
│ ├─ usuario_id: 2 (FK para user)
│ ├─ nome_oficina: "AutoFix Mecânica"
│ ├─ endereco: "Rua das Flores, 123"
│ └─ [outros campos]
│
│ Tabela: core_perilofoicina_especialidades (ManyToMany)
│ ├─ id: 1, perilofoicina_id: 1, especialidade_id: 1
│ └─ id: 2, perilofoicina_id: 1, especialidade_id: 2
```

---

## 7️⃣ Fluxo de Redirecionamento

```
┌─────────────────────────────────────────────────────────────────┐
│            REDIRECIONAMENTO INTELIGENTE                          │
└─────────────────────────────────────────────────────────────────┘

HOME PAGE (/)
┌──────────────────────
│ if not user.is_authenticated:
│    return render('home.html')  ← Mostra opções de cadastro
│ elif user.is_cliente:
│    redirect('dashboard_cliente')
│ elif user.is_oficina:
│    redirect('dashboard_oficina')

CADASTRO (/)
┌──────────────────────
│ if user.is_authenticated:
│    redirect('home')  ← Se já logado
│ else:
│    return render('signup_choice.html')

DASHBOARDS (/painel/cliente/ & /painel/oficina/)
┌──────────────────────
│ @login_required
│ if user.is_cliente and path == '/painel/cliente/':
│    return render(...)  ✅ PERMITIDO
│ elif user.is_cliente and path == '/painel/oficina/':
│    redirect('home')  ❌ NEGADO
│ elif user.is_oficina and path == '/painel/oficina/':
│    return render(...)  ✅ PERMITIDO
│ elif user.is_oficina and path == '/painel/cliente/':
│    redirect('home')  ❌ NEGADO
```

---

## 8️⃣ Fluxo de Segurança (CSRF)

```
┌─────────────────────────────────────────────────────────────────┐
│            PROTEÇÃO CONTRA CSRF                                  │
└─────────────────────────────────────────────────────────────────┘

REQUEST INICIAL (GET /cadastro/cliente/)
┌──────────────────────────────────────────
│ Django Middleware:
│ ├─ Gera CSRF token
│ ├─ Armazena em session
│ └─ Passa para template

TEMPLATE RENDERIZADO
┌──────────────────────────────────────────
│ {% csrf_token %}
│ <form method="post">
│    <input type="hidden" name="csrfmiddlewaretoken"
│           value="[token_aleatorio]">
│    <!-- campos do formulário -->
│ </form>

SUBMISSÃO DO FORMULÁRIO (POST /cadastro/cliente/)
┌──────────────────────────────────────────
│ Browser envia:
│ ├─ csrfmiddlewaretoken=[token_aleatorio]
│ ├─ username=...
│ ├─ email=...
│ └─ password=...

VALIDAÇÃO NO SERVIDOR
┌──────────────────────────────────────────
│ CsrfViewMiddleware:
│ ├─ Extrai token do POST
│ ├─ Compara com token da session
│ ├─ Se diferente: HTTP 403 Forbidden
│ └─ Se igual: Continua processamento

PROTEÇÃO CONTRA:
├─ Cross-site request forgery
├─ Forged form submissions
├─ Unauthorized actions
└─ Cookie-based attacks
```

---

**Diagramas completos de todo o fluxo!** ✅
