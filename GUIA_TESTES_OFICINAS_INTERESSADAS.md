# 🧪 Guia de Teste - Oficinas Interessadas

## ✅ Funcionalidade: Oficinas Interessadas

Sistema de manifestação de interesse onde:
- **Oficinas** se interessam em problemas
- **Clientes** aceitam/rejeitam interesse

---

## 🚀 Pré-requisitos

1. Servidor rodando
   ```bash
   .\.venv\Scripts\python manage.py runserver
   ```

2. Dois usuários criados:
   - **Cliente**: email: `cliente@test.com` | senha: `teste123`
   - **Oficina**: email: `oficina@test.com` | senha: `teste123`

3. Um problema registrado pelo cliente

---

## 🧪 Teste 1: Manifestar Interesse (Oficina)

### Passo 1: Login como Oficina

1. Abra: http://localhost:8000/login/
2. Use:
   - Email: `oficina@test.com`
   - Senha: `teste123`
3. Clique em "Login"

### Passo 2: Ir para Dashboard Oficina

1. Acesse: http://localhost:8000/painel/oficina/
2. Você verá:
   - Problemas em Aberto (esquerda)
   - Meus Serviços (direita)

### Passo 3: Ver Problema Disponível

1. Na seção "Problemas em Aberto", procure por um problema
2. Clique no card do problema

### Passo 4: Manifestar Interesse

1. Você verá o botão **"🤝 Manifestar Interesse"**
2. (Opcional) Preencha uma mensagem:
   - "Consigo resolver em 1 dia"
   - "Tenho experiência com este modelo"
3. Clique em **"Confirmar Interesse"**

✅ **Sucesso!** Você manifestou interesse

---

## 🧪 Teste 2: Ver Interesse (Cliente)

### Passo 1: Login como Cliente

1. Abra: http://localhost:8000/logout/ (para deslogar)
2. Abra: http://localhost:8000/login/
3. Use:
   - Email: `cliente@test.com`
   - Senha: `teste123`
4. Clique em "Login"

### Passo 2: Ir para Dashboard Cliente

1. Acesse: http://localhost:8000/painel/cliente/
2. Você verá seus problemas

### Passo 3: Ver Oficinas Interessadas

1. Encontre o problema que criou interesse
2. Você verá um badge: **"🤝 1 oficina"** (ou mais)

### Passo 4: Expandir Detalhes

1. Abaixo do status, clique ou expanda "Oficinas Interessadas"
2. Você verá:
   - Nome da oficina
   - Nome do negócio
   - Mensagem enviada
   - Botões ✅ (aceitar) e ❌ (rejeitar)

✅ **Sucesso!** Você vê o interesse da oficina

---

## 🧪 Teste 3: Aceitar Interesse (Cliente)

### Continuando do Teste 2...

1. Na lista de "Oficinas Interessadas"
2. Clique no botão **✅ (Aceitar)**
3. A página recarrega

### Verificar Resultado

1. O problema agora mostra:
   - Status: **"🟢 Em Andamento"**
   - Badge: **"🟢 Oficina: [Nome da Oficina]"** (em verde)
   - Seção "Oficinas Interessadas" **desaparece**

✅ **Sucesso!** Problema aceito e oficina definida

---

## 🧪 Teste 4: Rejeitar Interesse (Cliente)

### Setup: Criar Novo Cenário

1. **Como Cliente:**
   - Registre um novo problema (outro carro, outro título)

2. **Como Oficina:**
   - Login e manifeste interesse neste novo problema
   - Deixe a mensagem em branco (ou não)

3. **Como Cliente:**
   - Volta ao dashboard
   - Deve ver "🤝 1 oficina"

### Rejeitar

1. Expanda "Oficinas Interessadas"
2. Clique no botão **❌ (Rejeitar)**
3. A página recarrega

### Verificar Resultado

1. A seção "Oficinas Interessadas" **desaparece**
2. Badge volta a: **"🔴 Aguardando interesse"**
3. Problema continua em **"Em Aberto"**

✅ **Sucesso!** Interesse rejeitado

---

## 🧪 Teste 5: Múltiplas Oficinas

### Setup: 3 Oficinas Interessadas

1. Crie dois usuários adicionais (oficina 2 e 3)
   - Email: `oficina2@test.com`
   - Email: `oficina3@test.com`

2. **Como Oficina 2 e 3:**
   - Manifeste interesse no mesmo problema

3. **Como Cliente:**
   - Dashboard deve mostrar: **"🤝 3 oficinas"**

### Aceitar Uma, Rejeitar as Outras

1. Expanda "Oficinas Interessadas"
2. Você vê 3 oficinas listadas
3. Clique ✅ na **Oficina 1**

### Verificar Resultado

1. Badge muda para: **"🟢 Oficina: [Nome da Oficina 1]"**
2. Lista de interessadas **desaparece**
3. Problema vai para: **"Em Andamento"**
4. As outras 2 oficinas são **automaticamente rejeitadas**

✅ **Sucesso!** Somente a aceita é mantida, as outras rejeitadas automaticamente

---

## 🧪 Teste 6: Oficina Vê Seus Serviços

### Setup

1. Tenha um problema que você (oficina) foi aceito

2. **Como Oficina:**
   - Login: `oficina@test.com`
   - Acesse: http://localhost:8000/painel/oficina/

### Verificar

1. Na seção **"Meus Serviços"** (direita)
2. Você deve ver o problema que foi aceito
3. Status: **"Em Andamento"**

✅ **Sucesso!** Oficina vê seu serviço aceito

---

## 📊 Checklist de Testes

```
☐ Login como cliente funciona
☐ Login como oficina funciona
☐ Cliente vê badge de interesse
☐ Oficina consegue manifestar interesse
☐ Cliente vê detalhes do interesse
☐ Cliente vê nome da oficina
☐ Cliente vê nome do negócio
☐ Cliente vê mensagem da oficina
☐ Cliente consegue aceitar interesse
☐ Cliente consegue rejeitar interesse
☐ Ao aceitar, status muda para "Em Andamento"
☐ Ao aceitar, outras oficinas são rejeitadas
☐ Oficina vê o serviço em "Meus Serviços"
☐ Problema sem interesse mostra "Aguardando"
☐ Múltiplas oficinas aparecem na lista
☐ Responsividade em mobile funciona
☐ Botões não aparecem quando problema já tem oficina
☐ Mensagem da oficina aparece corretamente
☐ Sem erros no console (F12)
☐ Sem erros no terminal Django
```

---

## 🐛 Troubleshooting

### "Badge de interesse não aparece"
**Solução:**
- Recarregar página (F5)
- Limpar cache (Ctrl+Shift+Delete)
- Reiniciar servidor Django

### "Botão de manifestar interesse não aparece"
**Solução:**
- Verificar se está logado como oficina (não cliente)
- Verificar se o problema está em "Em Aberto"
- Verificar se não é seu próprio problema

### "Não consigo aceitar/rejeitar"
**Solução:**
- Verificar se está logado como cliente (proprietário do problema)
- Recarregar página
- Verificar console do navegador (F12 → Console)

### "Erro 500 ao aceitar"
**Solução:**
- Verificar terminal do Django (erros aparecem lá)
- Verificar se interesse existe no banco de dados
- Executar: `python manage.py check`

---

## 📱 Teste de Responsividade

1. Abrir DevTools (F12)
2. Clicar em ícone móvel (Ctrl+Shift+M)
3. Testar diferentes tamanhos:
   - Mobile (320px)
   - Tablet (768px)
   - Desktop (1024px)

**Esperado:**
- ✅ Badges aparecem corretamente
- ✅ Botões são clicáveis
- ✅ Sem scroll horizontal
- ✅ Texto legível

---

## 📊 Dados no Banco

**Para ver todos os interesses:**
```bash
python manage.py shell
```

```python
from core.models import Interesse

# Ver todos
Interesse.objects.all()

# Ver por status
Interesse.objects.filter(status='INTERESSADA')
Interesse.objects.filter(status='REJEITADA')

# Ver de um problema específico
problema = Problema.objects.first()
problema.interesses.all()

# Ver de uma oficina
oficina = User.objects.filter(is_oficina=True).first()
oficina.interesses_manifesto.all()

# Contar
problema.total_interessadas()

# Sair
exit()
```

---

## 🎯 Casos de Teste Avançados

### Teste: Deletar Interesse (Admin)

1. Acesse: http://localhost:8000/admin/
2. Vá para: "Interesses"
3. Selecione um interesse e delete
4. Verifique no dashboard do cliente

### Teste: Editar Mensagem (Admin)

1. Acesse: http://localhost:8000/admin/
2. Vá para: "Interesses"
3. Edite a mensagem
4. Salve
5. Verifique no dashboard do cliente

### Teste: Mudar Status (Admin)

1. Acesse: http://localhost:8000/admin/
2. Vá para: "Interesses"
3. Mude status de INTERESSADA para REJEITADA
4. Verifique no dashboard do cliente

---

## 📋 Resultado Esperado Final

Ao concluir todos os testes:

```
✅ Cliente pode ver quantas oficinas estão interessadas
✅ Oficina pode manifestar interesse
✅ Cliente pode aceitar uma oficina
✅ Cliente pode rejeitar uma oficina
✅ Ao aceitar, problema vai para "Em Andamento"
✅ Ao aceitar, outras oficinas são rejeitadas
✅ Oficina vê seu serviço em "Meus Serviços"
✅ Mensagem da oficina aparece corretamente
✅ Responsivo em todos os tamanhos
✅ Sem erros no navegador ou servidor
```

---

**Status**: ✅ Testes Prontos  
**Versão**: 1.0  
**Data**: Dezembro 2024
