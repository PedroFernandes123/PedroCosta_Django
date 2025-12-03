# 📸 Quick Reference - Upload de Imagem

## ⚡ Começar em 10 Segundos

```bash
# Terminal (Windows PowerShell)
cd "c:\Users\phfer\OneDrive\Área de Trabalho\UNIFEI\AUTOMÁTICA\ECAA09_Parte2-main\ECAA09_Parte2-main"
.\.venv\Scripts\python manage.py runserver
```

Acesse: **http://localhost:8000/painel/cliente/**

---

## 🎯 O Que Funciona

| Ação | Resultado | Status |
|------|-----------|--------|
| Upload de JPG | Salva em `/media/problemas/` | ✅ |
| Upload de PNG | Salva em `/media/problemas/` | ✅ |
| Upload de GIF | Salva em `/media/problemas/` | ✅ |
| Arquivo > 5MB | Rejeita com erro | ✅ |
| Não-imagem | Rejeita com erro | ✅ |
| Sem imagem | Problema criado ok | ✅ |
| Imagem no card | Mostra miniatura | ✅ |
| Mobile | Responsivo | ✅ |

---

## 📋 Ficheiros

### Código
- `core/models.py` - Campo `imagem` (ImageField)
- `core/forms.py` - Validação `clean_imagem()`
- `core/views.py` - `request.FILES` em dashboard_cliente
- `oficina_prj/settings.py` - MEDIA_URL, MEDIA_ROOT
- `oficina_prj/urls.py` - Media serving
- `templates/core/dashboard_cliente.html` - Form + Display

### Migrations
- `core/migrations/0002_problema_imagem.py` - ✅ Aplicada

### Documentação
- `README_UPLOAD_IMAGEM.md` - Guia completo
- `GUIA_TESTES_IMAGEM.md` - Testes
- `STATUS_FINAL_UPLOAD.md` - Status
- `UPLOAD_STATUS_RESUMO.md` - Resumo
- `RESUMO_VISUAL_UPLOAD.md` - Visual

---

## 🔧 Configuração

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ Checklist

- [x] Pillow instalado (12.0.0)
- [x] Migration criada
- [x] Database atualizado
- [x] Code validado
- [x] Tests prontos
- [x] Docs completa
- [x] System check OK

---

## 📞 Suporte

**Erro**: Imagem não aparece?
→ Reinicie servidor + limpe cache (Ctrl+Shift+Delete)

**Erro**: "Arquivo muito grande"?
→ Arquivo > 5MB, comprimir ou converter

**Erro**: "Deve ser uma imagem"?
→ Selecione JPG, PNG ou GIF válido

**Erro**: "Pillow não instalado"?
→ `.\.venv\Scripts\pip install Pillow`

---

## 🚀 Próximas Melhorias

1. Crop de imagem
2. Múltiplas imagens
3. Compressão automática
4. AWS S3/Azure Blob (produção)
5. Galeria de fotos

---

**Status**: ✅ Pronto para usar!  
**Versão**: 1.0  
**Data**: Dez 2024
