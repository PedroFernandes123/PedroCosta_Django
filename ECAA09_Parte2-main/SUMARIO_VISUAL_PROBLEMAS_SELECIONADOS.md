# 🎨 SUMÁRIO VISUAL - DASHBOARD OFICINA (3 SEÇÕES)

## Visualização do Dashboard

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🛠️  PAINEL DA OFICINA                                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌─ Problemas Disponíveis ┐  ┌─ Meus Interesses ┐  ┌─ Meus Serviços ┐    ║
║  │ 📥 Inbox        [12] ⚠️ │  │ ❤️ Heart    [3] ℹ️ │  │ ✅ Check  [5] ✅ │    ║
║  ├─────────────────────────┤  ├──────────────────┤  ├────────────────┤    ║
║  │ • Toyota Corolla      │  │ • Honda Civic   │  │ • Fiat Uno    │    ║
║  │   Problema: Freio...  │  │   Problema: mot.│  │   Status: Anda│    ║
║  │   [Cliente1] [02/25]   │  │   [Cliente3] ...│  │   [Btn Conclu]│    ║
║  │                       │  │                  │  │              │    ║
║  │ • Hyundai HB20       │  │ • Volkswagen    │  │ • BMW X5      │    ║
║  │   Problema: Transmis │  │   Problema: ...  │  │   Status: Anda│    ║
║  │   [Cliente2] [01/25]   │  │   [Cliente4] ...│  │   [Btn Conclu]│    ║
║  │                       │  │                  │  │              │    ║
║  │ [+9 mais...]          │  │ • Fiat Palio    │  │ [+2 mais...]  │    ║
║  │                       │  │   Problema: Óle │  │              │    ║
║  │ 💡 Clique para ver    │  │   [Cliente5] ...│  │ 💡 Clique p/ │    ║
║  │    detalhes           │  │                  │  │    finalizar │    ║
║  └─────────────────────────┘  └──────────────────┘  └────────────────┘    ║
║                                                                              ║
║  LEGENDA:                                                                    ║
║  ⚠️  = Amarelo (Ativo/Disponível)                                           ║
║  ℹ️  = Azul (Informação/Interesse)                                          ║
║  ✅ = Verde (Sucesso/Concluído)                                             ║
║  📥📌❤️✅ = Ícones Font Awesome 6                                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Estrutura HTML da Página

```
html
├─ base.html (header, navbar, footer)
└─ dashboard_oficina.html
    ├─ <h2> Painel da Oficina
    └─ <div class="row">
       ├─ <div class="col-lg-4"> [DESKTOP: 33% width]
       │  ├─ Problemas Disponíveis
       │  ├─ Card Header (amarelo)
       │  ├─ Card Body
       │  │  ├─ for problema in problemas_abertos
       │  │  │  └─ <a> card item (clickable)
       │  │  └─ empty state (se não houver)
       │  └─ </div>
       │
       ├─ <div class="col-lg-4"> [DESKTOP: 33% width] ← NOVO
       │  ├─ Meus Interesses
       │  ├─ Card Header (azul)
       │  ├─ Card Body
       │  │  ├─ for problema in problemas_selecionados ← NOVO CONTEXT
       │  │  │  └─ <a> card item (clickable)
       │  │  └─ empty state
       │  └─ </div>
       │
       └─ <div class="col-lg-4"> [DESKTOP: 33% width]
          ├─ Meus Serviços
          ├─ Card Header (verde)
          ├─ Card Body
          │  ├─ for servico in meus_servicos
          │  │  └─ <a> card item (com botão concluir)
          │  └─ empty state
          └─ </div>
```

## Fluxo de Dados

```
┌─────────────────────────────────────────────────────────────────────┐
│                         NAVEGADOR                                    │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                        GET /dashboard-oficina/
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       DJANGO VIEW                                    │
│                   dashboard_oficina()                               │
├─────────────────────────────────────────────────────────────────────┤
│  @login_required                                                     │
│  def dashboard_oficina(request):                                    │
│      # Query 1: Problemas Disponíveis                              │
│      problemas_abertos = Problema.objects.filter(                 │
│          status='ABERTO'                                           │
│      )                                                              │
│                                                                      │
│      # Query 2: Meus Interesses [NOVO]                             │
│      problemas_selecionados = Problema.objects.filter(            │
│          interesses__oficina=request.user,                        │
│          interesses__status='INTERESSADA',                        │
│          oficina__isnull=True                                     │
│      ).distinct().order_by('-interesses__data_interesse')         │
│                                                                      │
│      # Query 3: Meus Serviços                                      │
│      meus_servicos = Problema.objects.filter(                     │
│          oficina=request.user                                      │
│      )                                                              │
│                                                                      │
│      # Render template com 3 contextos                             │
│      return render(request, 'dashboard_oficina.html', {           │
│          'problemas_abertos': problemas_abertos,                  │
│          'problemas_selecionados': problemas_selecionados, ← NOVO │
│          'meus_servicos': meus_servicos                           │
│      })                                                             │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                    {% for problema in X %}
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DJANGO TEMPLATE                                │
│                 dashboard_oficina.html                              │
├─────────────────────────────────────────────────────────────────────┤
│  Três colunas responsivas:                                          │
│  ├─ {% for problema in problemas_abertos %}                        │
│  ├─ {% for problema in problemas_selecionados %} ← NOVO LOOP       │
│  └─ {% for servico in meus_servicos %}                             │
│                                                                      │
│  Cada loop renderiza:                                              │
│  ├─ Card com border-left colorido                                 │
│  ├─ Ícones e badges                                               │
│  ├─ Dados do problema                                             │
│  └─ Link clickable para detalhe_problema                          │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
                       HTML renderizado
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       NAVEGADOR                                     │
│          Exibe 3 cards lado a lado (responsivo)                    │
└─────────────────────────────────────────────────────────────────────┘
```

## Query SQL Gerada

```sql
-- Query 1: Problemas Disponíveis
SELECT * FROM core_problema 
WHERE status = 'ABERTO'
ORDER BY data_criacao DESC;

-- Query 2: Meus Interesses [NOVO]
SELECT DISTINCT core_problema.* 
FROM core_problema
INNER JOIN core_interesse ON core_problema.id = core_interesse.problema_id
WHERE core_interesse.oficina_id = {USER_ID}
  AND core_interesse.status = 'INTERESSADA'
  AND core_problema.oficina_id IS NULL
ORDER BY core_interesse.data_interesse DESC;

-- Query 3: Meus Serviços
SELECT * FROM core_problema 
WHERE oficina_id = {USER_ID}
ORDER BY data_criacao DESC;
```

## Comparação: Antes vs Depois

### ANTES (2 Colunas)
```
┌──────────────────┬──────────────────┐
│ Disponíveis (50%)│ Meus Serviços(50%)│
│                  │                  │
│ 12 problemas     │ 5 serviços       │
│                  │                  │
│ Sem seção para   │                  │
│ interesses em    │                  │
│ andamento!       │                  │
└──────────────────┴──────────────────┘
```

### DEPOIS (3 Colunas) ✨
```
┌──────────────┬──────────────┬──────────────┐
│Disponíveis   │Meus Interesse│Meus Serviços │
│   (33%)      │    (33%)     │   (33%)      │
│              │              │              │
│12 problemas  │ 3 interesses │ 5 serviços   │
│              │              │              │
│ Seção nova   │ NOVO!        │              │
│ permite      │ Acompanhar   │ Gerenciar    │
│ explorar     │ interesse    │ trabalos     │
└──────────────┴──────────────┴──────────────┘
```

### Responsividade

**Desktop (≥1200px):**
```
┌──────────────┬──────────────┬──────────────┐
│     33%      │     33%      │     33%      │ = 3 colunas
└──────────────┴──────────────┴──────────────┘
```

**Tablet (768-1199px):**
```
┌──────────────┬──────────────┐
│     50%      │     50%      │
├──────────────┼──────────────┤
│     100%     │
└──────────────┴──────────────┘
= 2 + 1 colunas
```

**Mobile (<768px):**
```
┌──────────────────────────────┐
│         100% (full)          │
├──────────────────────────────┤
│         100% (full)          │
├──────────────────────────────┤
│         100% (full)          │
└──────────────────────────────┘
= 1 coluna empilhada
```

## Classes CSS Utilizadas

```css
/* Grid */
.row                    /* Container Bootstrap para grid */
.col-lg-4              /* 3 colunas em desktop (33%) */
.col-md-6              /* 2 colunas em tablet (50%) */
.col-12                /* 1 coluna em mobile (100%) */

/* Cards */
.card                  /* Container do card */
.card-header           /* Cabeçalho colorido */
.card-body             /* Conteúdo do card */
.card-header.bg-warning/* Fundo amarelo (disponíveis) */
.card-header.bg-primary/* Fundo azul (interesses) ← NOVO */
.card-header.bg-success/* Fundo verde (meus serviços) */

/* List items */
.list-group            /* Agrupador de itens */
.list-group-item       /* Item individual */
.list-group-item-action/* Item clicável */
.border-start          /* Borda esquerda */
.border-4              /* Espessura 4px */
.border-warning        /* Cor amarela */
.border-primary        /* Cor azul ← NOVO */
.border-success        /* Cor verde */
.rounded               /* Bordas arredondadas */

/* Badges */
.badge                 /* Etiqueta pequena */
.bg-danger             /* Vermelho (contador) */
.bg-light              /* Claro (info) */
.text-dark             /* Texto escuro */

/* Spacing */
.mb-4                  /* Margin bottom 1.5rem */
.mb-2                  /* Margin bottom 0.5rem */
.ms-2                  /* Margin start 0.5rem */
.p-3                   /* Padding 1rem */
.gap-2                 /* Gap entre flex items */
.ms-3                  /* Margin start 1rem */

/* Utilities */
.shadow-sm             /* Sombra suave */
.h-100                 /* Altura 100% */
.d-flex                /* Display flex */
.flex-grow-1           /* Flex grow 1 */
.justify-content-between /* Space between items */
.align-items-start     /* Align items no topo */
.text-muted            /* Texto cinza */
.text-white            /* Texto branco */

/* Custom hovers */
.card:hover            /* Sombra aumenta */
.list-group-item:hover /* Fundo claro + translação */
```

## Pseudocódigo da Template Loop

```python
def render_dashboard():
    for problema in problemas_abertos:
        render_card({
            'titulo': problema.titulo,
            'cliente': problema.cliente.first_name,
            'data': problema.data_criacao,
            'contador': problema.total_interessadas(),
            'link': f'/problema/{problema.id}/',
            'cor': 'warning',  # amarelo
            'icone': 'inbox'
        })
    
    # NOVO: Meus Interesses
    for problema in problemas_selecionados:
        render_card({
            'titulo': problema.titulo,
            'cliente': problema.cliente.first_name,
            'data': problema.data_criacao,
            'contador': problema.total_interessadas(),
            'link': f'/problema/{problema.id}/',
            'cor': 'primary',  # azul ← NOVO
            'icone': 'heart'   # ← NOVO
        })
    
    for servico in meus_servicos:
        render_card({
            'titulo': servico.titulo,
            'cliente': servico.cliente.first_name,
            'data': servico.data_criacao,
            'link': f'/problema/{servico.id}/',
            'cor': 'success',  # verde
            'icone': 'wrench',
            'botao': 'Concluir'
        })
```

## Estados Possíveis

### Estado 1: Sem dados
```
Seção vazia com mensagem:
"Você ainda não manifestou interesse em nenhum problema."
"Procure nos 'Problemas Disponíveis'!"
```

### Estado 2: Com 1 problema
```
┌─ Meus Interesses ─────┐
│ ❤️ Heart         [1]  │
├───────────────────────┤
│ • Honda Civic (1 item)│
│   [Cliente] [Data]    │
└───────────────────────┘
```

### Estado 3: Com múltiplos problemas
```
┌─ Meus Interesses ─────┐
│ ❤️ Heart         [5]  │
├───────────────────────┤
│ • Honda Civic         │
│ • Fiat Palio          │
│ • Volkswagen          │
│ • Toyota Corolla      │
│ • Hyundai HB20        │
└───────────────────────┘
```

## Interações do Usuário

```
┌─────────────────────────────────────────────────────┐
│ Oficina no Dashboard                                │
└─────────────────────────────────────────────────────┘
           │
           ├─ HOVER sobre card de problema
           │  └─ Efeito visual: fundo muda, sombra aumenta
           │
           └─ CLICK no card
              └─ Navegar para /problema/{id}/
                 └─ Ver detalhes do problema
                    ├─ Botão: Manifestar Interesse
                    │  └─ Cria Interesse(status='INTERESSADA')
                    │     └─ Problema aparece em "Meus Interesses"
                    │
                    ├─ Ou voltar ao dashboard
                    │  └─ Ver problema em nova seção
                    │
                    └─ Esperar cliente decidir
                       ├─ ACEITA
                       │  └─ problema.oficina = oficina
                       │     └─ Problema sai de "Interesses"
                       │        └─ Aparece em "Meus Serviços"
                       │
                       └─ REJEITA
                          └─ interesse.status = 'REJEITADA'
                             └─ Problema sai de "Interesses"
```

## Resumo das Mudanças

| Aspecto | Antes | Depois |
|---------|-------|--------|
| **Colunas** | 2 (50%/50%) | 3 (33%/33%/33%) |
| **Seções** | 2 | 3 |
| **Interesses Visíveis** | Não | Sim ✨ |
| **Ícones** | 2 | 3 |
| **Cores** | Warning, Success | Warning, Primary, Success |
| **Template Lines** | ~150 | ~240 |
| **CSS** | ~30 | ~80 |
| **Context Vars** | 2 | 3 |
| **Queries** | 2 | 3 |

---

**Status:** ✅ Implementado  
**Versão:** 1.0  
**Data:** 2024
