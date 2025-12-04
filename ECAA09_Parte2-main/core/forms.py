from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Problema, PerfilOficina, Especialidade

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome (opcional)'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'})

class ClienteSignUpForm(UserSignUpForm):
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True
        if commit:
            user.save()
        return user

class OficinaSignUpForm(UserSignUpForm):
    nome_oficina = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da oficina'}))
    endereco = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}))
    especialidades = forms.ModelMultipleChoiceField(
        queryset=Especialidade.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
    
    class Meta(UserSignUpForm.Meta):
        fields = ('username', 'email', 'first_name', 'password1', 'password2', 'nome_oficina', 'endereco', 'especialidades')
    
    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.is_oficina = True
        if commit:
            user.save()
            # Criar perfil de oficina
            perfil = PerfilOficina.objects.create(
                usuario=user,
                nome_oficina=self.cleaned_data['nome_oficina'],
                endereco=self.cleaned_data['endereco']
            )
            perfil.especialidades.set(self.cleaned_data['especialidades'])
        return user

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['titulo', 'modelo_carro', 'descricao', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do problema'
            }),
            'modelo_carro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Fiat Uno 2015'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva o problema com detalhes'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'data-toggle': 'tooltip',
                'title': 'Selecione uma foto do problema'
            }),
        }
    
    def clean_imagem(self):
        imagem = self.cleaned_data.get('imagem')
        if imagem:
            # Verificar tamanho (máximo 5MB)
            if imagem.size > 5 * 1024 * 1024:
                raise forms.ValidationError('A imagem não pode ser maior que 5MB')
            
            # Verificar tipo de arquivo
            if not imagem.content_type.startswith('image/'):
                raise forms.ValidationError('O arquivo deve ser uma imagem')
        return imagem

class OficinaPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilOficina
        fields = ['nome_oficina', 'endereco', 'especialidades']
        widgets = {
            'nome_oficina': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidades': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }