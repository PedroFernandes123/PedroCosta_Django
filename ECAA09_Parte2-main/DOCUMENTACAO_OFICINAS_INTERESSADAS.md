# 🤝 Oficinas Interessadas - Documentação

## ✅ Funcionalidade Implementada

O sistema agora permite que **oficinas manifestem interesse** nos problemas registrados pelos clientes, e os clientes possam **aceitar ou rejeitar** o interesse.

---

## 🎯 Como Funciona

### Para Clientes

1. **Visualizar Problemas**
   - Dashboard mostra todos os seus problemas registrados
   - Cada problema mostra quantas oficinas estão interessadas

2. **Ver Oficinas Interessadas**
   - Se há interesse, você vê um badge com: "🤝 X oficinas"
   - Clique para ver detalhes de cada oficina

3. **Aceitar/Rejeitar**
   - Clique em ✅ (aceitar) para escolher uma oficina
   - Clique em ❌ (rejeitar) para descartar
   - Ao aceitar, o status muda para "Em Andamento" automaticamente

### Para Oficinas

1. **Ver Problemas em Aberto**
   - Dashboard mostra problemas que ninguém pegou ainda
   - Clique em "Manifestar Interesse" para se interessar

2. **Escrever Mensagem** (opcional)
   - Pode adicionar uma mensagem sobre o serviço
   - O cliente vê sua mensagem ao analisar interesses

3. **Acompanhar**
   - Se o cliente aceitar você, o problema vai para "Meus Serviços"
   - Status muda para "Em Andamento"

---

## 📊 Modelo de Dados

### Novo Modelo: `Interesse`

```python
class Interesse(models.Model):
    problema = ForeignKey(Problema)           # Qual problema
    oficina = ForeignKey(User)                # Qual oficina
    status = CharField(INTERESSADA/REJEITADA) # Status do interesse
    mensagem = TextField()                    # Mensagem da oficina
    data_interesse = DateTimeField()          # Quando manifestou interesse
```

**Características:**
- ✅ Uma oficina pode se interessar por vários problemas
- ✅ Um problema pode ter interesse de várias oficinas
- ✅ A combinação (problema, oficina) é única (não pode repetir)

---

## 🔄 Fluxo de Trabalho

```
1. CLIENTE registra PROBLEMA
   ↓
2. OFICINA vê problema e MANIFESTA INTERESSE
   ↓
3. CLIENTE recebe AVISO: "X oficinas interessadas"
   ↓
4. CLIENTE vê DETALHES (nome, mensagem)
   ↓
5. CLIENTE ACEITA uma oficina
   ↓
6. Todos os outros interesses são REJEITADOS
   ↓
7. Problema vai para ANDAMENTO com oficina escolhida
   ↓
8. OFICINA trabalha no problema
   ↓
9. OFICINA CONCLUI serviço
   ↓
10. Problema marcado como CONCLUÍDO
```

---

## 📁 Ficheiros Modificados

### 1. `core/models.py`
- ✅ Adicionado modelo `Interesse`
- ✅ Adicionado método `total_interessadas()` no Problema
- ✅ Adicionado método `oficinas_interessadas()` no Problema

### 2. `core/views.py`
- ✅ Adicionada view `aceitar_interesse()`
- ✅ Adicionada view `rejeitar_interesse()`
- ✅ Adicionada view `manifestar_interesse()`

### 3. `oficina_prj/urls.py`
- ✅ Adicionadas rotas para gerenciar interesses

### 4. `templates/core/dashboard_cliente.html`
- ✅ Exibe badge com número de oficinas interessadas
- ✅ Mostra lista de oficinas interessadas com botões aceitar/rejeitar
- ✅ Exibe mensagem da oficina (se houver)

### 5. `core/admin.py`
- ✅ Adicionada classe `InteresseAdmin` para gerenciar no painel

---

## 📸 Interface no Dashboard

### Para Cliente

```
┌─────────────────────────────────────────────┐
│ Meus Chamados                               │
├─────────────────────────────────────────────┤
│ ┌───────────────────────────────────────┐   │
│ │ Fiat Uno 2015 - Vidro quebrado       │   │
│ │ Vidro frontal quebrado...             │   │
│ │                                        │   │
│ │ [🔴 Em Aberto] [🤝 2 oficinas]       │   │
│ │                                        │   │
│ │ Oficinas Interessadas:                │   │
│ │ • 🔧 João Silva (Oficina João)       │   │
│ │   "Consigo resolver em 1 dia"        │   │
│ │   [✅] [❌]                           │   │
│ │                                        │   │
│ │ • 🔧 Maria Santos (Oficina Maria)    │   │
│ │   "Tenho experiência com vidros"     │   │
│ │   [✅] [❌]                           │   │
│ └───────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## 🧪 Como Testar

### Teste 1: Manifestar Interesse

1. **Login como Oficina**
   - URL: `http://localhost:8000/login/`
   - Email: `oficina@test.com`

2. **Ver Problemas em Aberto**
   - URL: `http://localhost:8000/painel/oficina/`

3. **Manifestar Interesse**
   - Clique em um problema
   - Clique em "Manifestar Interesse"
   - (Opcional) Adicione uma mensagem
   - Clique em "Confirmar"

### Teste 2: Aceitar/Rejeitar Interest

1. **Login como Cliente**
   - URL: `http://localhost:8000/login/`
   - Email: `cliente@test.com`

2. **Ver Problemas**
   - URL: `http://localhost:8000/painel/cliente/`
   - Você deve ver: "🤝 1 oficina" no seu problema

3. **Aceitar Interesse**
   - Expanda a seção "Oficinas Interessadas"
   - Clique em ✅ para aceitar a oficina
   - Status muda para "Em Andamento"

### Teste 3: Rejeitar Interesse

1. **Mesmo como acima, mas clique em ❌**
   - A oficina é rejeitada
   - O interesse desaparece da lista

---

## 📊 Banco de Dados

### Migração Aplicada

```
✅ core/migrations/0003_interesse.py
   - Cria tabela: core_interesse
   - Colunas: id, problema_id, oficina_id, status, mensagem, data_interesse, data_atualizacao
   - Índices: unique_together(problema, oficina)
```

**Para ver no banco:**
```bash
python manage.py shell
>>> from core.models import Interesse
>>> Interesse.objects.all()
```

---

## 🔒 Segurança

✅ **Apenas cliente pode aceitar/rejeitar** - Validado na view  
✅ **Apenas oficina pode manifestar interesse** - Validado na view  
✅ **Não pode duplicar interesse** - Constraint unique_together  
✅ **CSRF Protection** - Token no formulário  

---

## 📝 API de Uso

### No Template

```django
{% if problema.total_interessadas > 0 %}
    <span class="badge">{{ problema.total_interessadas }} oficina(s)</span>
{% endif %}

{% for interesse in problema.interesses.all %}
    {% if interesse.status == 'INTERESSADA' %}
        <p>{{ interesse.oficina.first_name }}</p>
        <p>{{ interesse.mensagem }}</p>
    {% endif %}
{% endfor %}
```

### Na View

```python
# Pegar interesses de um problema
interesses = problema.interesses.filter(status='INTERESSADA')

# Pegar total de interessadas
total = problema.total_interessadas()

# Pegar oficinas interessadas
oficinas = problema.oficinas_interessadas()
```

---

## 📊 Estados Possíveis

| Status | Significado | Visível para Cliente |
|--------|-------------|----------------------|
| INTERESSADA | Oficina quer fazer o serviço | ✅ Sim (com botões) |
| REJEITADA | Cliente rejeitou | ❌ Não |
| CANCELADA | Oficina cancelou | ❌ Não |

---

## 🎯 Fluxo de Status do Problema

```
ABERTO
  ├─ Sem interesse → Continua ABERTO
  ├─ Com interesse → Cliente escolhe
  │
  └─ Cliente aceita interesse
      ↓
      ANDAMENTO (oficina definida)
        ├─ Oficina trabalha
        │
        └─ Oficina marca como concluído
            ↓
            CONCLUÍDO
```

---

## 🚀 Próximas Melhorias

1. **Notificações**
   - Email quando cliente aceita
   - Email quando interesse é rejeitado

2. **Rating/Avaliação**
   - Cliente avalia oficina após concluído
   - Mostrar rating no perfil

3. **Chat/Mensagens**
   - Chat entre cliente e oficina
   - Histórico de conversas

4. **Orçamento**
   - Oficina envia orçamento
   - Cliente aprova ou rejeita

5. **Agendamento**
   - Agendar data/hora da realização do serviço
   - Lembrete para ambas partes

---

## 📞 FAQ

**P: Posso me interessar por um problema que já tem oficina?**
R: Não. Se um cliente já aceitou uma oficina, outras não podem mais se interessar.

**P: Posso cancelar meu interesse?**
R: Sim, a view `manifestar_interesse()` com PUT cancelaria (futura implementação).

**P: Quantas vezes posso me interessar?**
R: Apenas uma. Se tentar novamente, o sistema ignora (unique_together).

**P: O que acontece com os outros interesses?**
R: Quando você aceita um, todos os outros são automaticamente rejeitados.

---

## ✅ Verificação de Implementação

- [x] Modelo `Interesse` criado
- [x] Relacionamentos configurados
- [x] Views implementadas
- [x] URLs configuradas
- [x] Admin configurado
- [x] Template atualizado
- [x] Migração criada e aplicada
- [x] Segurança implementada
- [x] Testes documentados

---

**Status**: ✅ IMPLEMENTADO E TESTADO  
**Data**: Dezembro 2024  
**Versão**: 1.0
