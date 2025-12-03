#!/usr/bin/env bash
# Build script para Render.com

set -o errexit

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Aplicando migrações..."
python manage.py migrate

echo "✅ Build concluído com sucesso!"
