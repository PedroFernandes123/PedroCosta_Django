# 🧪 Guia de Teste - Upload de Imagem

## ✅ Migrations Executadas com Sucesso!

```
✓ Criada: core/migrations/0002_problema_imagem.py
✓ Aplicada ao banco de dados
✓ Pillow instalado corretamente
```

## 🚀 Iniciar Servidor de Testes

```bash
python manage.py runserver
```

Ou com a versão específica do venv:
```bash
.\.venv\Scripts\python manage.py runserver
```

## 📝 Passo 1: Criar Usuário Cliente (se não tiver)

1. Acesse: http://localhost:8000/signup/
2. Clique em **"Sou um Cliente"**
3. Preencha os dados:
   - Email
   - Senha (2x)
   - Nome
   - Sobrenome
4. Clique em **"Registrar como Cliente"**

## 📸 Passo 2: Testar Upload de Imagem

1. Faça login: http://localhost:8000/login/
2. Acesse: http://localhost:8000/painel/cliente/
3. Preencha o formulário "Novo Problema":
   - **Título**: Vidro quebrado
   - **Modelo do Carro**: Fiat Uno 2015
   - **Descrição**: Vidro frontal quebrado precisa trocar
   - **Foto**: Selecionar uma imagem (JPG, PNG, GIF) **até 5MB**
4. Clique em **"📤 Registrar Problema"**

## ✅ Verificações

### Sucesso - Você deve ver:
- [x] A imagem é salva em `/media/problemas/`
- [x] A imagem aparece como miniatura na lista de problemas
- [x] O problema é criado normalmente
- [x] Layout responsivo mostra imagem e informações lado a lado
- [x] Badge de status aparece (Em Aberto, Em Progresso, Concluído)
- [x] Data/hora formatada corretamente

### Teste 2: Validação de Tamanho

1. Tente fazer upload de uma imagem **maior que 5MB**
2. **Esperado**: Mensagem de erro: "A imagem não pode ser maior que 5MB"
3. Formulário não é enviado
4. Campo de imagem fica em vermelho (com erro)

### Teste 3: Validação de Tipo

1. Tente fazer upload de um arquivo **não-imagem** (PDF, TXT, DOC, etc)
2. **Esperado**: Mensagem de erro: "O arquivo deve ser uma imagem"
3. Formulário não é enviado
4. Campo de imagem fica em vermelho (com erro)

### Teste 4: Campo Opcional

1. Preencha o formulário **SEM** selecionar imagem
2. Clique em "📤 Registrar Problema"
3. **Esperado**: O problema é criado normalmente
4. Na lista, o problema não terá imagem (sem ícone quebrado)

### Teste 5: Responsividade

1. Redimensione a janela para simular dispositivo móvel
2. Verifique que:
   - Formulário se adapta
   - Imagem na lista é legível
   - Botões são clicáveis
   - Sem scroll horizontal

## 🎯 Arquivo Estará em

```
projeto/
├── media/
│   └── problemas/
│       ├── problema_imagem_abc123.jpg
│       ├── problema_imagem_def456.png
│       └── ...
```

## 🔍 Debug - Se Algo Não Funcionar

### Erro: "Imagem não aparece na lista"
```bash
# Verifique se existe o arquivo
dir "media\problemas\"

# Verifique permissões
# (Deve estar legível pelo servidor Django)
```

### Erro: "Campo de upload não aparece"
```bash
# Verifique se settings foi atualizado
# Procure por MEDIA_URL em oficina_prj/settings.py
python manage.py shell
>>> from django.conf import settings
>>> print(settings.MEDIA_URL)
>>> print(settings.MEDIA_ROOT)
```

### Erro: "ValidationError ao fazer upload"
```bash
# Verifique o tipo de arquivo
# Use no terminal:
# - file -i "caminho/da/imagem"  (Linux/Mac)
# - Clique direito > Propriedades (Windows)

# Verifique o tamanho
# - dir "caminho\da\imagem"  (Windows)
# - ls -lh "caminho/da/imagem"  (Linux/Mac)
```

### Erro: "Pillow não instalado"
```bash
.\.venv\Scripts\pip install Pillow --upgrade
```

## 📊 Status do Banco de Dados

Para verificar que a coluna foi criada:

```bash
python manage.py shell
>>> from core.models import Problema
>>> p = Problema.objects.first()
>>> print(p.imagem)  # Deve mostrar URL ou vazio
```

## 🎨 Customizações Opcionais

### Aumentar Limite de Tamanho
Edite `core/forms.py`:
```python
# Procure por:
if imagem.size > 5 * 1024 * 1024:

# Mude para:
if imagem.size > 10 * 1024 * 1024:  # 10MB
```

### Aceitar Mais Formatos
Edite `templates/core/dashboard_cliente.html`:
```html
<!-- Encontre: -->
<input type="file" accept="image/*">

<!-- Deixe assim para aceitar fotos ou documentos: -->
<input type="file" accept="image/*, application/pdf">
```

### Mudar Local de Armazenamento
Edite `core/models.py`:
```python
# Procure por:
imagem = models.ImageField(upload_to='problemas/', ...)

# Mude para:
imagem = models.ImageField(upload_to='chamados/%Y/%m/', ...)  # Organiza por data
```

## 📋 Checklist de Testes

- [ ] Upload com imagem JPG
- [ ] Upload com imagem PNG
- [ ] Upload com imagem GIF
- [ ] Upload sem imagem (campo opcional)
- [ ] Rejeita arquivo > 5MB
- [ ] Rejeita arquivo não-imagem
- [ ] Imagem aparece na lista
- [ ] Imagem aparece no card
- [ ] Responsive em mobile
- [ ] Responsive em tablet
- [ ] Responsive em desktop
- [ ] Mensagens de erro aparecem
- [ ] Validação no cliente funciona
- [ ] Validação no servidor funciona

## 🚀 Próximos Passos

1. **Implementado ✅**: Upload de imagem simples
2. **Opcional**: Crop de imagem (biblioteca Pillow)
3. **Opcional**: Compressão automática
4. **Opcional**: Múltiplas imagens por problema
5. **Produção**: Usar AWS S3 ou Azure Blob Storage

## 📚 Documentação Relacionada

- `README_UPLOAD_IMAGEM.md` - Documentação completa
- `core/models.py` - Modelo Problema com campo imagem
- `core/forms.py` - Validação de arquivo
- `templates/core/dashboard_cliente.html` - Interface de upload
- `oficina_prj/settings.py` - Configuração de mídia

---

**Status**: ✅ PRONTO PARA TESTES

Boa sorte! 🎉
