# 🚀 Checklist de Deployment - Tela de Cadastro

## ✅ Pré-Deployment

### Código
- [ ] Todos os testes passam (execute: `python manage.py test`)
- [ ] Sem erros no linter (execute: `flake8 .`)
- [ ] Sem warnings de importações não utilizadas
- [ ] Código segue PEP 8
- [ ] Docstrings adicionadas aos novos métodos
- [ ] Comments explicando lógica complexa

### Segurança
- [ ] CSRF tokens em todos os formulários
- [ ] Senhas protegidas (não exibidas)
- [ ] Input sanitizado (sem XSS)
- [ ] SQL Injection prevenido (usando ORM)
- [ ] Secrets não expostos (SECRET_KEY fora do git)
- [ ] Debug=False em produção
- [ ] ALLOWED_HOSTS configurado corretamente

### Performance
- [ ] Templates cached
- [ ] Queries otimizadas (sem N+1)
- [ ] Static files minificados
- [ ] Imagens otimizadas
- [ ] CSS/JS minimizados

### Banco de Dados
- [ ] Migrações criadas: `python manage.py makemigrations`
- [ ] Migrações testadas localmente
- [ ] Backup do banco anterior feito
- [ ] Rollback plan criado

### Testes
- [ ] Testes unitários criados
- [ ] Testes de integração passam
- [ ] Coverage > 80%
- [ ] Testes em mobile passam
- [ ] Testes em diferentes navegadores

### Documentação
- [ ] README atualizado
- [ ] API documentada (se aplicável)
- [ ] Mudanças documentadas
- [ ] Instruções de setup claras
- [ ] Troubleshooting section adicionado

## 📋 Checklist de Deployment

### Antes do Deploy
```bash
# 1. Listar mudanças
git status

# 2. Verificar testes
python manage.py test

# 3. Coletar static files
python manage.py collectstatic --no-input

# 4. Fazer backup
python manage.py dumpdata > backup_antes_deploy.json

# 5. Verificar migrações
python manage.py showmigrations

# 6. Verificar settings de produção
python manage.py check --deploy
```

### Executar Migrações
```bash
# Em produção
python manage.py migrate

# Verificar se tudo ok
python manage.py shell
>>> from core.models import User, PerfilOficina
>>> User.objects.count()
>>> PerfilOficina.objects.count()
```

### Verificações Finais
- [ ] URLs funcionam
- [ ] Cadastro funciona
- [ ] Email de confirmação funciona (se implementado)
- [ ] Redirecionamentos funcionam
- [ ] Dashboards acessíveis
- [ ] Sem erros em logs
- [ ] Performance aceitável

## 🔍 Testes em Produção

### Teste de Cadastro Cliente
1. Acessar `/cadastro/`
2. Clicar em "Cadastrar como Cliente"
3. Preencher formulário completamente
4. Enviar
5. Verificar redirecionamento para `/painel/cliente/`
6. Verificar no banco: `is_cliente=True`

### Teste de Cadastro Oficina
1. Acessar `/cadastro/`
2. Clicar em "Cadastrar como Oficina"
3. Preencher formulário completamente
4. Selecionar especialidades
5. Enviar
6. Verificar redirecionamento para `/painel/oficina/`
7. Verificar no banco: `is_oficina=True` e `PerfilOficina` criado

### Testes de Segurança
- [ ] Tentar acessar `/painel/cliente/` sem estar logado (deve redirecionar)
- [ ] Tentar acessar `/painel/oficina/` sem estar logado (deve redirecionar)
- [ ] Cliente acessar `/painel/oficina/` (deve ser negado)
- [ ] Oficina acessar `/painel/cliente/` (deve ser negado)

### Testes de Performance
```bash
# Medir tempo de resposta
curl -w "@curl-format.txt" -o /dev/null -s http://seu-site.com/cadastro/

# Monitorar uso de recursos
top
df -h
free -h
```

## 📊 Monitoramento Pós-Deploy

### Logs
- [ ] Verificar logs de erros
- [ ] Verificar logs de acesso
- [ ] Alertas configurados

### Métricas
- [ ] Acompanhar taxa de cadastro
- [ ] Taxa de conversão (cliente vs oficina)
- [ ] Tempo de resposta das páginas
- [ ] Uso de CPU/Memória

### Alertas
```bash
# Configurar alertas para:
# - Erros 500+
# - Taxa de erro > 1%
# - Tempo de resposta > 2s
# - Espaço em disco < 10%
# - Memória > 80%
```

## 🆘 Rollback Plan

Se algo der errado:

```bash
# 1. Revert código
git revert <commit-hash>
git push

# 2. Revert banco de dados
python manage.py migrate <app-name> <migration-number>

# 3. Restaurar backup
python manage.py loaddata backup_antes_deploy.json

# 4. Reiniciar serviços
systemctl restart gunicorn
systemctl restart nginx
```

## 📝 Post-Deployment

### Comunicação
- [ ] Informar usuários sobre novas rotas
- [ ] Email de confirmação enviado aos admins
- [ ] Social media atualizado (se aplicável)

### Monitoramento (primeira semana)
- [ ] Verificar logs diariamente
- [ ] Acompanhar taxa de cadastro
- [ ] Responder a issues rapidamente
- [ ] Fazer backups diários

### Otimização
- [ ] Analisar dados de uso
- [ ] Identificar gargalos
- [ ] Fazer ajustes necessários
- [ ] Documentar lições aprendidas

## 🎯 Métricas de Sucesso

| Métrica | Target | Atual |
|---------|--------|-------|
| Tempo resposta | < 200ms | ? |
| Taxa de erro | < 0.1% | ? |
| Cadastros/dia | > 10 | ? |
| Taxa conversão | > 80% | ? |
| Uptime | > 99.9% | ? |

## 📞 Contatos Importantes

| Papel | Nome | Email | Telefone |
|------|------|-------|----------|
| DevOps | - | - | - |
| DBA | - | - | - |
| Support | - | - | - |
| Manager | - | - | - |

## 🔗 Recursos Úteis

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [OWASP Security Checklist](https://owasp.org/www-project-web-security-testing-guide/)
- [Performance Testing](https://en.wikipedia.org/wiki/Software_performance_testing)

---

## ✅ Final Checklist

- [ ] Código revisado por pelo menos 1 pessoa
- [ ] Testes aprovados
- [ ] Segurança verificada
- [ ] Performance aceita
- [ ] Documentação completa
- [ ] Backup feito
- [ ] Plano de rollback pronto
- [ ] Time informado
- [ ] Monitoramento ativo
- [ ] Pronto para deploy! 🚀

---

**Data de Deploy**: ___/___/______
**Responsável**: _________________
**Status**: ⏳ Pendente

Após completar este checklist, você pode fazer o deploy com confiança!
