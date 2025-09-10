#!/usr/bin/env python3
"""
Demo Rápido del Keylogger Educativo
Autor: Alvaro Manzo

Una demostración rápida de las capacidades del keylogger
"""

import os
import sys
import time
import json
from datetime import datetime

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

def print_banner():
    """Mostrar banner de demo"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════╗
║              KEYLOGGER EDUCATIVO - DEMO                  ║
║                 Demostración Rápida                      ║
╚══════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.RED}{Colors.BOLD}⚠️  DEMO EDUCATIVO ⚠️{Colors.END}
{Colors.YELLOW}Esta es una demostración de las capacidades del keylogger.{Colors.END}
{Colors.YELLOW}Solo para fines educativos y sistemas propios.{Colors.END}
    """
    print(banner)

def check_dependencies():
    """Verificar dependencias necesarias"""
    print(f"\n{Colors.BLUE}🔍 Verificando dependencias...{Colors.END}")
    
    required_modules = [
        ('pynput', 'Captura de teclado y mouse'),
        ('cryptography', 'Encriptación de datos'),
        ('flask', 'Dashboard web'),
        ('psutil', 'Información del sistema'),
        ('qrcode', 'Generación de códigos QR')
    ]
    
    missing_modules = []
    
    for module, description in required_modules:
        try:
            __import__(module)
            print(f"{Colors.GREEN}✅ {module:<15} - {description}{Colors.END}")
        except ImportError:
            print(f"{Colors.RED}❌ {module:<15} - {description} (FALTANTE){Colors.END}")
            missing_modules.append(module)
        time.sleep(0.1)
    
    if missing_modules:
        print(f"\n{Colors.YELLOW}📦 Dependencias faltantes detectadas:{Colors.END}")
        for module in missing_modules:
            print(f"   - {module}")
        print(f"\n{Colors.CYAN}Para instalar, ejecuta:{Colors.END}")
        print(f"{Colors.WHITE}pip install {' '.join(missing_modules)}{Colors.END}")
        print(f"\n{Colors.CYAN}O usa el instalador automático:{Colors.END}")
        print(f"{Colors.WHITE}./install.sh{Colors.END}")
        return False
    
    return True

def demo_encryption():
    """Demostrar encriptación"""
    print(f"\n{Colors.PURPLE}🔐 Demostración de Encriptación{Colors.END}")
    
    try:
        from cryptography.fernet import Fernet
        
        # Generar clave
        key = Fernet.generate_key()
        cipher = Fernet(key)
        
        # Datos de ejemplo
        test_data = {
            "timestamp": datetime.now().isoformat(),
            "type": "demo",
            "data": "Esta es una prueba de encriptación",
            "user": "demo_user"
        }
        
        # Encriptar
        original_text = json.dumps(test_data)
        encrypted = cipher.encrypt(original_text.encode())
        
        # Desencriptar
        decrypted = cipher.decrypt(encrypted).decode()
        
        print(f"{Colors.GREEN}✅ Datos originales:{Colors.END}")
        print(f"   {original_text[:50]}...")
        
        print(f"{Colors.BLUE}🔒 Datos encriptados:{Colors.END}")
        print(f"   {encrypted.hex()[:50]}...")
        
        print(f"{Colors.GREEN}🔓 Datos desencriptados:{Colors.END}")
        print(f"   {decrypted[:50]}...")
        
        print(f"{Colors.CYAN}✨ Encriptación funcional!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error en demo de encriptación: {e}{Colors.END}")

def demo_system_info():
    """Demostrar información del sistema"""
    print(f"\n{Colors.BLUE}💻 Información del Sistema{Colors.END}")
    
    try:
        import psutil
        import socket
        import platform
        
        # Información básica
        system_info = {
            "SO": platform.system(),
            "Versión": platform.release(),
            "Arquitectura": platform.machine(),
            "Procesador": platform.processor(),
            "Memoria RAM": f"{psutil.virtual_memory().total // (1024**3)} GB",
            "CPU Cores": psutil.cpu_count(),
        }
        
        # IP Local
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            system_info["IP Local"] = ip
        except:
            system_info["IP Local"] = "No disponible"
        
        # Mostrar información
        for key, value in system_info.items():
            print(f"{Colors.GREEN}├── {key:<15}: {Colors.WHITE}{value}{Colors.END}")
        
        print(f"{Colors.CYAN}✨ Información del sistema obtenida!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error obteniendo info del sistema: {e}{Colors.END}")

def demo_file_operations():
    """Demostrar operaciones de archivos"""
    print(f"\n{Colors.YELLOW}📁 Demostración de Archivos{Colors.END}")
    
    demo_file = "demo_keylogger.txt"
    
    try:
        # Crear archivo de demo
        demo_data = f"""# KEYLOGGER DEMO - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Archivo de demostración generado automáticamente

[INFO] Demo iniciado
[KEYPRESS] H e l l o   W o r l d
[MOUSE] Click en (100, 200)
[INFO] Demo finalizado
"""
        
        with open(demo_file, 'w', encoding='utf-8') as f:
            f.write(demo_data)
        
        print(f"{Colors.GREEN}✅ Archivo creado: {demo_file}{Colors.END}")
        
        # Leer archivo
        with open(demo_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"{Colors.BLUE}📄 Contenido del archivo:{Colors.END}")
        for line in content.split('\n')[:5]:  # Mostrar solo las primeras 5 líneas
            if line.strip():
                print(f"   {line}")
        
        # Información del archivo
        file_size = os.path.getsize(demo_file)
        print(f"{Colors.CYAN}📊 Tamaño: {file_size} bytes{Colors.END}")
        
        # Limpiar
        os.remove(demo_file)
        print(f"{Colors.GREEN}🧹 Archivo de demo eliminado{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error en demo de archivos: {e}{Colors.END}")

def demo_config():
    """Demostrar configuración JSON"""
    print(f"\n{Colors.PURPLE}⚙️ Demostración de Configuración{Colors.END}")
    
    config_demo = {
        "version": "2.0",
        "demo_mode": True,
        "features": {
            "encryption": True,
            "web_dashboard": True,
            "mouse_capture": True,
            "window_titles": True,
            "secure_transfer": True
        },
        "limits": {
            "max_file_size": "5MB",
            "retention_days": 30,
            "max_events_per_hour": 10000
        },
        "security": {
            "auto_backup": True,
            "key_rotation": False,
            "remote_logging": False
        }
    }
    
    try:
        # Mostrar configuración
        print(f"{Colors.BLUE}📋 Configuración de ejemplo:{Colors.END}")
        
        def print_dict(d, indent=0):
            for key, value in d.items():
                spaces = "   " * indent
                if isinstance(value, dict):
                    print(f"{spaces}{Colors.CYAN}{key}:{Colors.END}")
                    print_dict(value, indent + 1)
                else:
                    color = Colors.GREEN if value else Colors.RED if value is False else Colors.WHITE
                    print(f"{spaces}{Colors.BLUE}{key}:{Colors.END} {color}{value}{Colors.END}")
        
        print_dict(config_demo)
        
        print(f"{Colors.CYAN}✨ Configuración JSON funcional!{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Error en demo de configuración: {e}{Colors.END}")

def show_features():
    """Mostrar características principales"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}🚀 Características Principales:{Colors.END}")
    
    features = [
        ("🎨 Interfaz Colorida", "Terminal moderna con colores y emojis"),
        ("🔐 Encriptación AES", "Logs seguros con Fernet"),
        ("📊 Dashboard Web", "Visualización en tiempo real"),
        ("🖱️ Captura Completa", "Teclado, mouse y ventanas"),
        ("📱 Códigos QR", "Transferencia fácil entre dispositivos"),
        ("⚙️ Configurable", "Personalización completa"),
        ("📈 Estadísticas", "Análisis detallado de actividad"),
        ("🔄 Auto-rotación", "Gestión automática de archivos"),
        ("🌐 Servidor HTTP", "Transferencia segura integrada"),
        ("📋 Logs JSON", "Formato estructurado y legible")
    ]
    
    for feature, description in features:
        print(f"{Colors.GREEN}✅ {feature:<20} - {Colors.WHITE}{description}{Colors.END}")
        time.sleep(0.1)

def interactive_menu():
    """Menú interactivo de demostración"""
    while True:
        print(f"\n{Colors.BOLD}🎮 Menú de Demostración:{Colors.END}")
        print(f"{Colors.GREEN}1.{Colors.END} Verificar dependencias")
        print(f"{Colors.BLUE}2.{Colors.END} Demo de encriptación")
        print(f"{Colors.YELLOW}3.{Colors.END} Información del sistema")
        print(f"{Colors.PURPLE}4.{Colors.END} Demo de archivos")
        print(f"{Colors.CYAN}5.{Colors.END} Demo de configuración")
        print(f"{Colors.WHITE}6.{Colors.END} Mostrar características")
        print(f"{Colors.RED}7.{Colors.END} Salir")
        
        try:
            choice = input(f"\n{Colors.CYAN}Selecciona una opción (1-7):{Colors.END} ").strip()
            
            if choice == '1':
                check_dependencies()
            elif choice == '2':
                demo_encryption()
            elif choice == '3':
                demo_system_info()
            elif choice == '4':
                demo_file_operations()
            elif choice == '5':
                demo_config()
            elif choice == '6':
                show_features()
            elif choice == '7':
                print(f"\n{Colors.GREEN}👋 ¡Gracias por probar el demo!{Colors.END}")
                print(f"{Colors.CYAN}Para usar el keylogger completo:{Colors.END}")
                print(f"{Colors.WHITE}python keylogger_advanced.py{Colors.END}")
                break
            else:
                print(f"{Colors.RED}❌ Opción inválida{Colors.END}")
            
            input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.GREEN}👋 ¡Hasta luego!{Colors.END}")
            break
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

def main():
    """Función principal del demo"""
    try:
        print_banner()
        
        print(f"{Colors.GREEN}🎯 ¡Bienvenido al demo del Keylogger Educativo!{Colors.END}")
        print(f"{Colors.BLUE}Este demo te mostrará las capacidades del sistema sin ejecutar el keylogger real.{Colors.END}")
        
        interactive_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}👋 Demo interrumpido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error inesperado: {e}{Colors.END}")

if __name__ == "__main__":
    main()
