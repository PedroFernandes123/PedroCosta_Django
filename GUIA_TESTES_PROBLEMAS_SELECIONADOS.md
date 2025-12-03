# 📋 GUIA DE TESTES - PROBLEMAS SELECIONADOS

## Visão Geral
O sistema agora exibe no dashboard da oficina uma nova seção chamada **"Meus Interesses"** que lista todos os problemas em que a oficina manifestou interesse, mas ainda não foi aceita pelo cliente.

## Arquitetura da Feature

### 📊 Modelo de Dados
```
Problema (ABERTO) ──→ Interesse (INTERESSADA) ──→ Oficina (atual user)
```

### 🎯 Lógica de Filtragem
A view `dashboard_oficina()` executa:

```python
problemas_selecionados = Problema.objects.filter(
    interesses__oficina=request.user,           # Interesse da oficina
    interesses__status='INTERESSADA',           # Status: INTERESSADA
    oficina__isnull=True                        # Ainda não atribuído
).distinct().order_by('-interesses__data_interesse')
```

### 📈 Fluxo do Dashboard (3 Seções)

#### Seção 1: **Problemas Disponíveis** (Amarelo)
- ✅ Todos os problemas com `status='ABERTO'`
- ✅ A oficina ainda não tem interesse manifestado
- 🔵 Ação: Clicar → Ir para detalhe e manifestar interesse

#### Seção 2: **Meus Interesses** (Azul) ← NOVA
- ✅ Problemas em que a oficina manifestou interesse
- ✅ Status do interesse = 'INTERESSADA'
- ✅ Oficina ainda não foi atribuída ao problema
- 🔵 Ação: Clicar → Ver detalhes / Acompanhar interesse
- ℹ️ Aguardando decisão do cliente (aceitar/rejeitar)

#### Seção 3: **Meus Serviços** (Verde)
- ✅ Problemas já aceitos (oficina atribuída)
- ✅ Em andamento ou concluído
- 🔵 Ação: Clicar → Ver detalhes / Marcar como concluído

## 🧪 Cenários de Teste

### Teste 1: Verificar Exibição da Seção
**Dados Necessários:**
- 1 Oficina logada (user.is_oficina = True)
- 1 Problema ABERTO cadastrado
- 1 Interesse com status='INTERESSADA' da oficina

**Passos:**
1. Fazer login como oficina
2. Ir para dashboard_oficina
3. Verificar se existe a seção "Meus Interesses"

**Resultado Esperado:**
```
✅ Seção "Meus Interesses" visível
✅ Badge com contador > 0
✅ Problema listado na seção
```

### Teste 2: Problema Não Aparece em Meus Interesses
**Dados Necessários:**
- 1 Oficina logada
- 1 Problema ABERTO
- 1 Interesse com status='REJEITADA'

**Passos:**
1. Fazer login como oficina
2. Verificar "Meus Interesses"

**Resultado Esperado:**
```
✅ Problema NÃO aparece em "Meus Interesses"
✅ Interesse rejeitado não afeta seção
```

### Teste 3: Problema Sai de Meus Interesses Quando Atribuído
**Dados Necessários:**
- 1 Oficina logada
- 1 Problema com interesse='INTERESSADA'
- Cliente aceita e atribui a oficina

**Passos:**
1. Verificar "Meus Interesses" (problema visível)
2. Cliente aceita via dashboard (problema.oficina = oficina)
3. Oficina faz refresh no dashboard

**Resultado Esperado:**
```
✅ Problema some de "Meus Interesses"
✅ Problema aparece em "Meus Serviços"
```

### Teste 4: Contador Dinâmico
**Dados Necessários:**
- Múltiplos problemas com interesse INTERESSADA

**Passos:**
1. Dashboard mostra N problemas
2. Badge exibe N

**Resultado Esperado:**
```
✅ Badge mostra quantidade correta
✅ Lista corresponde ao contador
```

### Teste 5: Responsividade
**Testes em Diferentes Resoluções:**

**Desktop (≥1200px):**
```
┌─────────────┬─────────────┬─────────────┐
│ Disponíveis │  Interesses │  Meus Svc   │
└─────────────┴─────────────┴─────────────┘
✅ 3 colunas lado a lado
```

**Tablet (768-1199px):**
```
┌──────────────┬──────────────┐
│ Disponíveis  │  Interesses  │
├──────────────┼──────────────┤
│  Meus Svc    │              │
└──────────────┴──────────────┘
✅ 2 colunas
```

**Mobile (<768px):**
```
┌──────────────────────────────┐
│     Problemas Disponíveis    │
├──────────────────────────────┤
│      Meus Interesses         │
├──────────────────────────────┤
│       Meus Serviços          │
└──────────────────────────────┘
✅ 1 coluna empilhada
```

### Teste 6: Clickability e Navegação
**Passos:**
1. Clicar em um problema em "Meus Interesses"
2. Verificar navegação

**Resultado Esperado:**
```
✅ Navega para detalhe_problema
✅ URL contém problema_id correto
✅ Detalhes do problema exibem corretamente
```

### Teste 7: Ordenação
**Dados:**
- 3 Problemas com interesses em datas diferentes
- Interesse 1: 2024-01-15 10:00
- Interesse 2: 2024-01-16 14:30
- Interesse 3: 2024-01-14 09:00

**Passos:**
1. Verificar ordem de exibição

**Resultado Esperado:**
```
✅ Ordem: Interesse 2 → Interesse 1 → Interesse 3
✅ Ordenado por data DESC (mais recente primeiro)
```

### Teste 8: Sem Interesses (Empty State)
**Dados:**
- 1 Oficina sem nenhum interesse manifestado

**Passos:**
1. Fazer login como oficina
2. Verificar seção "Meus Interesses"

**Resultado Esperado:**
```
✅ Mensagem: "Você ainda não manifestou interesse em nenhum problema."
✅ Sugestão: "Procure nos 'Problemas Disponíveis'!"
✅ Badge: 0
```

## 📊 Verificação de Dados SQL

### Query de Debugging
```sql
-- Verificar dados em Meus Interesses
SELECT p.*, i.* 
FROM core_problema p
JOIN core_interesse i ON p.id = i.problema_id
WHERE i.oficina_id = {OFICINA_ID}
  AND i.status = 'INTERESSADA'
  AND p.oficina_id IS NULL;
```

### Django Shell
```python
from core.models import Problema, Interesse
from django.contrib.auth.models import User

oficina = User.objects.get(username='oficina1')
interesses = Interesse.objects.filter(
    oficina=oficina,
    status='INTERESSADA'
)
for interesse in interesses:
    print(f"Problema: {interesse.problema.titulo}")
    print(f"Atribuído a: {interesse.problema.oficina}")
```

## 🎨 Verificação Visual

### Cores e Ícones
| Seção | Cor | Ícone | Border |
|-------|-----|-------|--------|
| Disponíveis | Amarelo (warning) | 📥 inbox | border-warning |
| **Meus Interesses** | **Azul (primary)** | **❤️ heart** | **border-primary** |
| Meus Serviços | Verde (success) | ✅ check-circle | border-success |

### Elementos da Card
```
┌─ Card Header ──────────────────────────┐
│ 📥 Título         [Badge: Contador]   │
├────────────────────────────────────────┤
│ • List Item 1                          │
│ • List Item 2                          │
│ • Empty State (se necessário)          │
└────────────────────────────────────────┘
```

## 📋 Checklist de Validação

- [ ] View `dashboard_oficina()` retorna `problemas_selecionados` no context
- [ ] Query filtra apenas problemas com interesse INTERESSADA
- [ ] Query filtra apenas problemas onde `oficina_id IS NULL`
- [ ] Query usa `.distinct()` para evitar duplicatas
- [ ] Query ordena por `data_interesse` DESC
- [ ] Template exibe nova seção entre Disponíveis e Meus Serviços
- [ ] Badge mostra contador correto
- [ ] Empty state exibe corretamente
- [ ] Problemas são clicáveis
- [ ] Navegação funciona (link para detalhe)
- [ ] Responsividade em 3 breakpoints (mobile, tablet, desktop)
- [ ] Cores e ícones consistentes
- [ ] Hover effects funcionam
- [ ] System check retorna 0 issues
- [ ] Sem erros JavaScript no console
- [ ] Sem SQL queries redundantes/lentas

## 🚀 Execução dos Testes

### Teste Rápido Local
```bash
# Terminal 1: Iniciar servidor
python manage.py runserver

# Terminal 2: Django Shell
python manage.py shell
>>> from core.models import Problema, Interesse, User
>>> oficina = User.objects.filter(is_oficina=True).first()
>>> problemas = Problema.objects.filter(
...     interesses__oficina=oficina,
...     interesses__status='INTERESSADA',
...     oficina__isnull=True
... ).distinct()
>>> print(f"Problemas em interesses: {problemas.count()}")
```

### Navegação Manual
1. Abrir browser
2. Login como oficina
3. Visitar `/dashboard-oficina/`
4. Verificar se seção está visível
5. Clicar em um problema
6. Verificar se detalhe carrega

## 📝 Logs e Debugging

### Verificar View Debug
```python
# Adicionar em views.py temporariamente
print(f"Oficina: {request.user}")
print(f"Problemas selecionados: {problemas_selecionados.count()}")
for p in problemas_selecionados:
    print(f"  - {p.titulo} (cliente: {p.cliente})")
```

### Verificar Template Debug
```html
<!-- Adicionar em template -->
{% comment %}
DEBUG: problemas_selecionados = {{ problemas_selecionados|length }}
{% endcomment %}
```

## 🔍 Possíveis Problemas

| Problema | Solução |
|----------|---------|
| Seção não aparece | Verificar se oficina tem interesse INTERESSADA |
| Problemas incorretos exibidos | Verificar query filter (oficina__isnull=True) |
| Contador errado | Verificar .distinct() na query |
| Não clicável | Verificar tag `<a>` e URL reverse |
| Layout quebrado | Verificar classes Bootstrap (col-lg-4) |
| Sem hover | Verificar CSS .list-group-item:hover |

---

**Status:** ✅ Implementado e Testável  
**Data:** 2024  
**Versão:** 1.0
