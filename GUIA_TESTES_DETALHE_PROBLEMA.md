# 🧪 Guia de Teste - Seleção de Problemas (Dashboard Oficina)

## ✅ Funcionalidade: Selecionar Problema para Ver Detalhes

Oficina pode clicar em um problema no dashboard para ver **detalhes completos** e **manifestar interesse**.

---

## 🚀 Pré-requisitos

1. **Servidor rodando**
   ```bash
   .\.venv\Scripts\python manage.py runserver
   ```

2. **Dados de Teste**
   - Cliente: `cliente@test.com` / `teste123`
   - Oficina: `oficina@test.com` / `teste123`
   - Problema registrado pelo cliente

---

## 🧪 Teste 1: Dashboard Oficina Melhorado

### Passo 1: Login como Oficina

1. Acesse: http://localhost:8000/login/
2. Use:
   - Email: `oficina@test.com`
   - Senha: `teste123`
3. Clique em "Login"

### Passo 2: Ir para Dashboard Oficina

1. Acesse: http://localhost:8000/painel/oficina/

### Passo 3: Verificar Interface

**Esperado:**
- ✅ Seção "Problemas Disponíveis" com lista de cards
- ✅ Seção "Meus Serviços em Andamento"
- ✅ Cada card tem:
  - Modelo do carro
  - Título do problema
  - Cliente
  - Data
  - Badge com número de interessadas
- ✅ Cards têm **fundo que muda ao passar o mouse** (hover)
- ✅ **Seta → no lado direito** indicando clicabilidade

---

## 🧪 Teste 2: Clicar em um Problema

### Passo 1: Selecionar um Problema

1. No dashboard, localize um problema em "Problemas Disponíveis"
2. **Clique em qualquer lugar do card** (não só no texto)

### Passo 2: Verificar Redirecionamento

**Esperado:**
- ✅ Página de detalhes carrega
- ✅ URL muda para: `http://localhost:8000/problema/[ID]/`
- ✅ **Sem erros** no console (F12)

---

## 🧪 Teste 3: Página de Detalhes

### Passo 1: Análise da Página

**Esperado ver:**
- ✅ Botão "Voltar" no topo
- ✅ Título do problema grande
- ✅ Badge de status (🔴 Em Aberto)
- ✅ **Imagem do problema** (se tiver enviado uma)

### Passo 2: Seção de Descrição

**Esperado:**
- ✅ "Descrição do Problema" com texto completo
- ✅ Modelo do carro
- ✅ Data de registro formatada

### Passo 3: Seção de Cliente

**Esperado:**
- ✅ Nome: "João Silva"
- ✅ Email: "cliente@test.com"
- ✅ Card com fundo claro

---

## 🧪 Teste 4: Manifestar Interesse

### Passo 1: Formulário de Interesse

Na página de detalhes, procure:
- ✅ "Deixe uma mensagem (opcional)"
- ✅ Campo de texto para mensagem

### Passo 2: Preencher Mensagem

1. Clique no campo de texto
2. Escreva uma mensagem como:
   - "Consigo resolver em 1 dia"
   - "Tenho experiência com este modelo"
   - "Peças em estoque, pronto para começar"

### Passo 3: Enviar

1. Clique em **"Manifestar Interesse"**

**Esperado:**
- ✅ Botão muda de cor (feedback visual)
- ✅ Página recarrega o dashboard
- ✅ **Sem erros**
- ✅ URL volta para: `http://localhost:8000/painel/oficina/`

---

## 🧪 Teste 5: Ver Interesse Manifestado

### Passo 1: Verificar No Dashboard

1. Volta ao dashboard
2. Procure pelo problema que manifestou interesse
3. **Procure por um badge**: "👥 1 interesse"

### Passo 2: Clicar Novamente

1. Clique no mesmo problema novamente
2. Vá para página de detalhes

### Passo 3: Verificar Alerta

**Esperado:**
- ✅ Alerta azul: "Você já manifestou interesse!"
- ✅ Status: "Interessada"
- ✅ Sua mensagem aparece na caixa de alerta
- ✅ **Botão desabilitado** (não deixa clicar novamente)

---

## 🧪 Teste 6: Múltiplos Problemas

### Passo 1: Manifestar Interesse em Outro

1. Volte ao dashboard
2. Encontre um problema **diferente**
3. Clique nele

### Passo 2: Manifeste Interesse (sem mensagem)

1. Deixe o campo de mensagem **em branco**
2. Clique em "Manifestar Interesse"

**Esperado:**
- ✅ Funciona normalmente
- ✅ Mensagem vazia é permitida
- ✅ Alerta agora mostra: "Sem mensagem enviada"

---

## 🧪 Teste 7: Visão do Cliente

### Passo 1: Login como Cliente

1. Logout: http://localhost:8000/logout/
2. Login: `cliente@test.com`

### Passo 2: Acesse um de Seus Problemas

1. Dashboard Cliente: http://localhost:8000/painel/cliente/
2. Clique em um de seus problemas

### Passo 3: Verificar Diferenças

**Esperado:**
- ✅ **Layout diferente** (sidebar à direita)
- ✅ Seção "Oficinas Interessadas" com lista
- ✅ Botões ✅ e ❌ para aceitar/rejeitar
- ✅ **Sem campo de mensagem** (só vê)

---

## 🧪 Teste 8: Responsividade

### Teste Mobile (320px)

1. Abra DevTools: F12
2. Ative modo móvel: Ctrl+Shift+M
3. Selecione "iPhone SE" (375px)

**Esperado:**
- ✅ Cards em coluna única
- ✅ Texto legível
- ✅ Botões clicáveis
- ✅ Sem scroll horizontal

### Teste Tablet (768px)

1. Altere para tamanho 768px
2. Verifique layout

**Esperado:**
- ✅ Cards lado a lado
- ✅ Tudo proporcional

### Teste Desktop (1200px)

1. Desative modo móvel
2. Maximize janela

**Esperado:**
- ✅ Layout completo com sidebar
- ✅ Tudo bem alinhado

---

## 📊 Checklist Detalhado

### Dashboard Oficina
```
☐ Seção "Problemas Disponíveis" aparece
☐ Seção "Meus Serviços em Andamento" aparece
☐ Cards têm bordas coloridas (esquerda)
☐ Cards têm ícones apropriados
☐ Cards mostram badges (cliente, data, interessadas)
☐ Cards têm efeito hover (mudam de cor/sombra)
☐ Seta → está visível à direita
☐ Total de problemas está correto
```

### Página de Detalhes
```
☐ Botão "Voltar" funciona
☐ Título do problema em grande
☐ Badge de status aparece
☐ Imagem carrega (se houver)
☐ Descrição aparece corretamente
☐ Dados do cliente estão corretos
☐ Formul mensagem está acessível
☐ Botão "Manifestar Interesse" é visível
```

### Manifestar Interesse
```
☐ Mensagem fica salva
☐ Redireciona ao dashboard
☐ Badge de interesse atualiza
☐ Alerta aparece ao tentar novamente
☐ Funciona sem mensagem (vazio)
☐ Funciona com mensagem longa
☐ Funciona com caracteres especiais
```

### Responsividade
```
☐ Mobile (320px) - OK
☐ Mobile (375px) - OK
☐ Tablet (768px) - OK
☐ Desktop (1200px) - OK
☐ Sem scroll horizontal em nenhum tamanho
☐ Botões clicáveis em todos os tamanhos
```

---

## 🐛 Troubleshooting

### "Não consigo clicar no card"
**Solução:**
- Certifique que clicou no card, não em um botão
- Tente clicar no texto principal

### "Página não carrega"
**Solução:**
- Verificar console (F12 → Console)
- Verificar terminal Django
- Tentar `python manage.py check`

### "Mensagem não aparece na próxima vez"
**Solução:**
- Recarregar página (F5)
- Verificar se salvou no banco: `python manage.py shell`

### "Alerta não aparece"
**Solução:**
- Verificar se o interesse foi criado
- Verificar browser console para erros

### "Responsividade ruim"
**Solução:**
- Limpar cache (Ctrl+Shift+Delete)
- Abrir em abeta privada
- Verificar zoom do navegador (deve ser 100%)

---

## 📱 Teste de Performance

**Tempo de carregamento esperado:**
- Dashboard: < 500ms
- Página de detalhes: < 300ms
- Manifestar interesse: < 1s

---

## 🎯 Resultado Final Esperado

Ao concluir todos os testes, você terá:

✅ Dashboard oficina visual e intuitiva  
✅ Cards clicáveis para ver detalhes  
✅ Página de detalhes completa  
✅ Manifestar interesse com mensagem  
✅ Responsivo em todos os tamanhos  
✅ Sem erros ou lentidões  

---

**Status**: ✅ Testes Prontos  
**Data**: Dezembro 2024  
**Versão**: 1.0
