#!/bin/bash
# Script para subir el keylogger educativo a GitHub
# Ejecuta este script para crear el repositorio automáticamente

echo "🌐 SUBIENDO KEYLOGGER EDUCATIVO CON SISTEMA REMOTO A GITHUB"
echo "=========================================================="

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}📁 Verificando archivos del proyecto...${NC}"

# Verificar que estamos en el directorio correcto
if [ ! -f "main.py" ] || [ ! -f "setup_remote.py" ]; then
    echo -e "${RED}❌ Error: No estás en el directorio del keylogger-educativo${NC}"
    echo "Navega al directorio correcto y ejecuta este script"
    exit 1
fi

echo -e "${GREEN}✅ Archivos del proyecto encontrados${NC}"

# Mostrar archivos principales que se van a subir
echo -e "\n${YELLOW}📋 Archivos principales a incluir:${NC}"
echo "├── 🚀 main.py (Launcher principal)"
echo "├── 🌐 src/central_server.py (Servidor para IPs públicas)"
echo "├── 📡 src/remote_keylogger.py (Cliente remoto)"
echo "├── ⚙️ setup_remote.py (Configurador automático)"
echo "├── 🚀 start_server.py & start_client.py (Launchers)"
echo "├── 📖 README.md (Documentación completa)"
echo "├── 📋 INSTRUCCIONES.md (Manual de uso)"
echo "└── 📄 LICENSE (Licencia MIT)"

# Inicializar Git si no está inicializado
if [ ! -d ".git" ]; then
    echo -e "\n${BLUE}🔄 Inicializando repositorio Git...${NC}"
    git init
    echo -e "${GREEN}✅ Repositorio Git inicializado${NC}"
else
    echo -e "\n${GREEN}✅ Repositorio Git ya existe${NC}"
fi

# Agregar todos los archivos
echo -e "\n${BLUE}📦 Agregando archivos al repositorio...${NC}"
git add .

# Mostrar el status
echo -e "\n${YELLOW}📊 Estado del repositorio:${NC}"
git status --short

# Crear commit inicial
echo -e "\n${BLUE}💾 Creando commit inicial...${NC}"
git commit -m "🌐 Keylogger Educativo con Sistema Remoto - IP Pública Real

✨ Características principales:
- 🔥 Obtiene IP pública real (no 192.168.x.x)  
- 🌐 Sistema cliente-servidor centralizado
- 📊 Panel web para monitoreo en tiempo real
- ⚡ Configuración automática en 1 comando
- 🔄 Reconexión automática de clientes
- 📁 Organización profesional de archivos

🚀 Uso rápido:
1. python3 setup_remote.py (configuración)
2. python3 start_server.py (tu máquina)  
3. python3 start_client.py (máquinas objetivo)

⚠️ Solo para uso educativo y sistemas autorizados"

echo -e "${GREEN}✅ Commit creado exitosamente${NC}"

# Instrucciones para GitHub
echo -e "\n${YELLOW}🔗 SIGUIENTE PASO - CREAR REPOSITORIO EN GITHUB:${NC}"
echo ""
echo -e "${BLUE}1️⃣ Ve a GitHub.com y crea un nuevo repositorio:${NC}"
echo "   └── Nombre sugerido: keylogger-educativo-remoto"
echo "   └── Descripción: Sistema de keylogger educativo con servidor centralizado para obtener IPs públicas reales"
echo "   └── ✅ Público (para compartir)"
echo "   └── ❌ NO inicialices con README (ya tienes uno)"
echo ""
echo -e "${BLUE}2️⃣ Copia los comandos que GitHub te muestre, o usa estos:${NC}"
echo ""
echo -e "${GREEN}# Conectar con tu repositorio GitHub:${NC}"
echo "git branch -M main"
echo "git remote add origin https://github.com/TU_USUARIO/keylogger-educativo-remoto.git"
echo "git push -u origin main"
echo ""
echo -e "${BLUE}3️⃣ Reemplaza TU_USUARIO con tu username de GitHub${NC}"
echo ""

# Comandos automáticos si el usuario quiere
echo -e "${YELLOW}¿Quieres que ejecute los comandos automáticamente?${NC}"
echo "Necesitarás proporcionar tu username de GitHub"
echo ""
read -p "Introduce tu username de GitHub (o presiona Enter para saltar): " github_username

if [ ! -z "$github_username" ]; then
    echo -e "\n${BLUE}🚀 Configurando repositorio remoto...${NC}"
    
    git branch -M main
    git remote add origin "https://github.com/${github_username}/keylogger-educativo-remoto.git"
    
    echo -e "${GREEN}✅ Repositorio remoto configurado${NC}"
    echo -e "${YELLOW}📤 Ahora ejecuta: git push -u origin main${NC}"
    echo -e "${BLUE}💡 Te pedirá tu token de GitHub o credenciales${NC}"
    
    echo ""
    echo -e "${YELLOW}¿Hacer push ahora? (y/n):${NC}"
    read -p "" do_push
    
    if [ "$do_push" = "y" ] || [ "$do_push" = "yes" ]; then
        echo -e "\n${BLUE}📤 Subiendo al repositorio...${NC}"
        git push -u origin main
        
        if [ $? -eq 0 ]; then
            echo -e "\n${GREEN}🎉 ¡REPOSITORIO SUBIDO EXITOSAMENTE!${NC}"
            echo -e "${BLUE}🔗 Tu repositorio está disponible en:${NC}"
            echo "https://github.com/${github_username}/keylogger-educativo-remoto"
        else
            echo -e "\n${RED}❌ Error en el push. Posibles causas:${NC}"
            echo "- Token de GitHub incorrecto"
            echo "- El repositorio no existe en GitHub"
            echo "- Problemas de conectividad"
            echo ""
            echo -e "${YELLOW}💡 Crear el repositorio manualmente en GitHub.com y ejecutar:${NC}"
            echo "git push -u origin main"
        fi
    fi
else
    echo -e "\n${YELLOW}📝 COMANDOS PARA EJECUTAR MANUALMENTE:${NC}"
    echo ""
    echo "git branch -M main"
    echo "git remote add origin https://github.com/TU_USUARIO/keylogger-educativo-remoto.git"  
    echo "git push -u origin main"
    echo ""
    echo -e "${BLUE}💡 Reemplaza TU_USUARIO con tu username real${NC}"
fi

echo ""
echo -e "${GREEN}🎯 RESUMEN DEL PROYECTO LISTO PARA GITHUB:${NC}"
echo "├── ✅ Sistema cliente-servidor completo"
echo "├── ✅ Obtención de IP pública real automática"
echo "├── ✅ Panel web profesional de monitoreo"
echo "├── ✅ Configuración automática en 1 comando"
echo "├── ✅ Documentación completa (README + INSTRUCCIONES)"
echo "├── ✅ Licencia MIT con disclaimer educativo"
echo "└── ✅ Estructura profesional de archivos"

echo ""
echo -e "${YELLOW}🔥 Tu keylogger avanzado está listo para ser compartido!${NC}"
echo -e "${BLUE}📖 Los usuarios podrán clonarlo y usar: python3 setup_remote.py${NC}"
