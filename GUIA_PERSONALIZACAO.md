# 🎨 Guia de Personalização - Tela de Cadastro

## 🎯 Como Personalizar a Tela de Cadastro

### 1. Mudar Cores dos Botões

**Arquivo**: `templates/registration/signup_choice.html`

```html
<!-- Encontrar esta linha -->
<button type="button" class="btn btn-primary btn-sm" ...>

<!-- Mudar para uma destas opções -->
btn-primary      <!-- Azul -->
btn-success      <!-- Verde -->
btn-danger       <!-- Vermelho -->
btn-warning      <!-- Amarelo -->
btn-info         <!-- Ciano -->
btn-dark         <!-- Preto -->
btn-light        <!-- Branco -->
```

### 2. Mudar Ícones dos Cards

**Arquivo**: `templates/registration/signup_choice.html`

```html
<!-- Encontrar -->
<div style="font-size: 3rem; margin-bottom: 1rem;">👤</div>

<!-- Mudar para qualquer emoji ou Font Awesome icon -->
<!-- Emojis -->
👤 → 🧑, 👨, 👩
🔧 → 🛠️, ⚙️, 🔩

<!-- Ou usar Font Awesome (se preferir) -->
<i class="fas fa-user" style="font-size: 3rem;"></i>
<i class="fas fa-tools" style="font-size: 3rem;"></i>
```

### 3. Adicionar Campos Obrigatórios Customizados

**Arquivo**: `core/forms.py`

```python
class ClienteSignUpForm(UserSignUpForm):
    # Adicionar campo customizado
    telefone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(11) 99999-9999'
        })
    )
    
    class Meta(UserSignUpForm.Meta):
        fields = ('username', 'email', 'telefone', 'first_name', 'password1', 'password2')
```

### 4. Mudar a Cor do Header dos Formulários

**Arquivo**: `templates/registration/signup.html`

```html
<!-- Encontrar -->
<div class="card-header bg-secondary text-white">

<!-- Mudar bg-secondary para -->
bg-primary       <!-- Azul -->
bg-success       <!-- Verde -->
bg-danger        <!-- Vermelho -->
bg-warning       <!-- Amarelo -->
bg-info          <!-- Ciano -->
bg-dark          <!-- Preto -->
```

### 5. Adicionar Logo na Página de Cadastro

**Arquivo**: `templates/registration/signup_choice.html`

```html
<!-- Adicionar antes do h3 -->
<img src="{% static 'images/logo.png' %}" alt="AutoFix" 
     style="max-width: 100px; margin-bottom: 20px;">
```

### 6. Personalizar Texto de Descrição

**Arquivo**: `templates/registration/signup_choice.html`

```html
<!-- Alterar estes textos -->
"Tenho problemas com meu veículo e preciso de uma oficina"
"Sou uma oficina e quero receber solicitações de serviços"

<!-- Para algo como -->
"Busco profissionais para consertar meu carro"
"Ofereço serviços de manutenção e reparo automotivo"
```

### 7. Mudar Redirecionamento Pós-Cadastro

**Arquivo**: `core/views.py`

```python
def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Mudar este redirecionamento
            return redirect('dashboard_cliente')  # ← Mudar aqui
            # Opções: 'home', 'dashboard_cliente', 'profile_edit', etc
```

### 8. Adicionar Validação Customizada

**Arquivo**: `core/forms.py`

```python
class OficinaSignUpForm(UserSignUpForm):
    def clean(self):
        cleaned_data = super().clean()
        
        # Validação customizada
        nome_oficina = cleaned_data.get('nome_oficina')
        if nome_oficina and len(nome_oficina) < 3:
            self.add_error('nome_oficina', 'O nome deve ter pelo menos 3 caracteres')
        
        return cleaned_data
```

### 9. Personalizar Mensagens de Erro

**Arquivo**: `core/forms.py`

```python
class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customizar mensagens
        self.fields['password1'].help_text = 'Sua senha deve ter ao menos 8 caracteres'
        self.fields['password2'].help_text = 'Digite a mesma senha, para validação'
```

### 10. Mudar Layout dos Cards

**Arquivo**: `templates/registration/signup_choice.html`

```html
<!-- De -->
<div class="col-md-6 mb-4">

<!-- Para -->
<div class="col-md-12 mb-4">    <!-- Cards em uma coluna -->
<!-- Ou -->
<div class="col-lg-4 mb-4">     <!-- Cards menores -->
```

### 11. Adicionar Animações

**Arquivo**: `templates/registration/signup_choice.html`

```html
<style>
    .card {
        transition: all 0.3s ease-in-out;
    }
    
    .card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 1rem 2rem rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Animação de entrada */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .card {
        animation: slideIn 0.5s ease-in-out;
    }
</style>
```

### 12. Tornar Campos Opcionais Obrigatórios

**Arquivo**: `core/forms.py`

```python
class ClienteSignUpForm(UserSignUpForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,  # ← Mudar de False para True
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome completo'
        })
    )
```

### 13. Adicionar Campo de Confirmação de Termos

**Arquivo**: `core/forms.py`

```python
class ClienteSignUpForm(UserSignUpForm):
    aceitar_termos = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text='Aceito os termos de serviço e política de privacidade'
    )
    
    class Meta(UserSignUpForm.Meta):
        fields = ('username', 'email', 'first_name', 'password1', 'password2', 'aceitar_termos')
```

### 14. Integrar reCAPTCHA

**Arquivo**: `core/forms.py`

```bash
# Instalar
pip install django-recaptcha
```

**Arquivo**: `settings.py`

```python
RECAPTCHA_PUBLIC_KEY = 'sua_chave_publica'
RECAPTCHA_PRIVATE_KEY = 'sua_chave_privada'
```

**Arquivo**: `core/forms.py`

```python
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ClienteSignUpForm(UserSignUpForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
```

### 15. Adicionar Upload de Imagem para Oficina

**Arquivo**: `core/models.py`

```python
class PerfilOficina(models.Model):
    # ... campos existentes ...
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    foto_fachada = models.ImageField(upload_to='fachadas/', null=True, blank=True)
```

**Arquivo**: `core/forms.py`

```python
class OficinaSignUpForm(UserSignUpForm):
    logo = forms.ImageField(required=False)
    
    class Meta(UserSignUpForm.Meta):
        fields = (..., 'logo')
```

### 16. Mudar Tema de Cores Globalmente

**Arquivo**: `templates/base.html`

```html
<!-- Adicionar CSS customizado -->
<style>
    :root {
        --primary-color: #007bff;
        --secondary-color: #6c757d;
        --success-color: #28a745;
    }
    
    .btn-primary {
        background-color: var(--primary-color);
    }
</style>
```

### 17. Adicionar Logging de Cadastros

**Arquivo**: `core/views.py`

```python
import logging

logger = logging.getLogger(__name__)

def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"Novo cliente cadastrado: {user.username}")
            login(request, user)
            return redirect('dashboard_cliente')
```

### 18. Mudar Título da Página

**Arquivo**: `templates/registration/signup.html`

```html
<!-- No topo do bloco content -->
{% block title %}Cadastro de {% if is_cliente %}Cliente{% else %}Oficina{% endif %}{% endblock %}
```

### 19. Adicionar Breadcrumb

**Arquivo**: `templates/registration/signup.html`

```html
<!-- Antes do card -->
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="{% url 'home' %}">Home</a></li>
        <li class="breadcrumb-item"><a href="{% url 'signup' %}">Cadastro</a></li>
        <li class="breadcrumb-item active">{% if is_cliente %}Cliente{% else %}Oficina{% endif %}</li>
    </ol>
</nav>
```

### 20. Integrar com Email de Confirmação

**Arquivo**: `core/views.py`

```python
from django.core.mail import send_mail

def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Desativar até confirmar email
            user.save()
            
            # Enviar email de confirmação
            send_mail(
                'Confirme seu email',
                f'Clique aqui para confirmar: http://...',
                'noreply@autofix.com',
                [user.email],
            )
            
            return redirect('email_confirmation_sent')
```

---

## 💡 Dicas Extras

1. **Teste sempre as mudanças localmente antes de fazer push**
2. **Use `python manage.py runserver` para ver mudanças em tempo real**
3. **Limpe o cache do navegador com Ctrl+Shift+Delete**
4. **Use as ferramentas do navegador (F12) para debug CSS**
5. **Considere usar Less ou SASS para melhorar manutenção de CSS**

## 📚 Recursos

- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Django Forms Docs](https://docs.djangoproject.com/en/5.0/topics/forms/)
- [Django Auth Docs](https://docs.djangoproject.com/en/5.0/topics/auth/)

---

**Precisa de ajuda?** Consulte a documentação completa em `DOCUMENTACAO_CADASTRO.md`
