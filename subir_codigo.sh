#!/bin/bash

# Pega todos os arquivos modificados
git add .

# Faz o commit. Se você não digitar uma mensagem, ele usa uma padrão.
MENSAGEM=${1:-"feat: atualizando exercicios e aulas do curso"}
git commit -m "$MENSAGEM"

# Envia para o GitHub
git push origin main

echo "✅ Arquivos enviados com sucesso para o GitHub!"

