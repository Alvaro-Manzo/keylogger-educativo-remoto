#!/bin/bash

# Script para preparar el proyecto para GitHub
# Autor: Alvaro Manzo

echo "🚀 Preparando Keylogger Educativo para GitHub..."

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}📁 Verificando estructura del proyecto...${NC}"

# Crear directorios si no existen
mkdir -p logs
mkdir -p docs

echo -e "${GREEN}✅ Estructura verificada${NC}"

echo -e "${BLUE}🔒 Configurando .gitignore...${NC}"
# El .gitignore ya está creado

echo -e "${BLUE}📄 Verificando archivos principales...${NC}"

files=(
    "main.py"
    "README.md" 
    "LICENSE"
    ".gitignore"
    "requirements.txt"
    "install.sh"
    "src/keylogger_visual.py"
    "src/data_viewer.py"
    "web/dashboard.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✅ $file${NC}"
    else
        echo -e "  ${RED}❌ $file${NC}"
    fi
done

echo -e "\n${YELLOW}📊 Estadísticas del proyecto:${NC}"
echo -e "  Archivos Python: $(find . -name '*.py' | wc -l)"
echo -e "  Líneas de código: $(find . -name '*.py' -exec wc -l {} + | tail -1 | awk '{print $1}')"
echo -e "  Archivos de documentación: $(find . -name '*.md' | wc -l)"

echo -e "\n${GREEN}🎯 INSTRUCCIONES PARA GITHUB:${NC}"
echo -e "${BLUE}1. Crear repositorio en GitHub:${NC}"
echo "   - Ve a github.com y crea un nuevo repositorio"
echo "   - Nombre sugerido: 'keylogger-educativo'"
echo "   - Descripción: 'Keylogger educativo con captura visual en tiempo real'"

echo -e "\n${BLUE}2. Subir el código:${NC}"
echo "   cd $(pwd)"
echo "   git init"
echo "   git add ."
echo "   git commit -m \"🚀 Keylogger Educativo v2.0 - Captura visual en tiempo real\""
echo "   git branch -M main"
echo "   git remote add origin https://github.com/TU-USUARIO/keylogger-educativo.git"
echo "   git push -u origin main"

echo -e "\n${BLUE}3. Configurar el repositorio:${NC}"
echo "   - Añadir topics: 'keylogger', 'educativo', 'seguridad', 'python', 'visual'"
echo "   - Activar Issues para reportes"
echo "   - Configurar GitHub Pages si quieres documentación web"

echo -e "\n${YELLOW}📋 CARACTERÍSTICAS DESTACADAS PARA EL README:${NC}"
echo "   ✨ Captura visual en tiempo real"
echo "   🎯 Súper fácil de usar (solo 'python3 main.py')"
echo "   📁 Organización perfecta en carpetas"
echo "   🔐 Encriptación de datos"
echo "   🌐 Dashboard web interactivo"
echo "   📱 Transferencia con códigos QR"

echo -e "\n${GREEN}🎉 ¡Proyecto listo para GitHub!${NC}"
echo -e "${CYAN}Estructura final del proyecto:${NC}"
tree . -I '__pycache__|*.pyc|logs' 2>/dev/null || ls -la

echo -e "\n${RED}⚠️  RECORDATORIO IMPORTANTE:${NC}"
echo -e "${YELLOW}Este proyecto es SOLO para fines educativos.${NC}"
echo -e "${YELLOW}Asegúrate de incluir todos los avisos legales.${NC}"
