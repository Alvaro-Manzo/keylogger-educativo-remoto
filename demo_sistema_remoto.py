#!/usr/bin/env python3
"""
Demo del Sistema Remoto con IP Pública
Simulación de cómo funciona el sistema completo
"""

import time
import subprocess
import os
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

def print_demo_banner():
    """Banner de demostración"""
    os.system('clear' if os.name != 'nt' else 'cls')
    print(f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║          🎯 DEMO - SISTEMA KEYLOGGER CON IP PÚBLICA           ║
║              SIMULACIÓN DEL SISTEMA COMPLETO                 ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.GREEN}🌐 ¿CÓMO FUNCIONA EL SISTEMA REAL?{Colors.END}

{Colors.YELLOW}📋 Configuración Real:{Colors.END}
├── 🖥️ {Colors.CYAN}TU MÁQUINA{Colors.END} → Ejecuta {Colors.WHITE}python3 start_server.py{Colors.END}
│   ├── 🌍 Obtiene TU IP pública (ej: 203.45.67.89)
│   ├── 🔌 Abre puerto 9999 para recibir conexiones
│   └── 🌐 Panel web en http://localhost:5000
│
├── 📱 {Colors.CYAN}MÁQUINA OBJETIVO{Colors.END} → Ejecuta {Colors.WHITE}python3 start_client.py{Colors.END}
│   ├── 🌍 Detecta SU IP pública real (ej: 198.12.34.56)
│   ├── 📡 Se conecta a tu servidor (203.45.67.89:9999)
│   └── 📊 Envía datos capturados + su IP pública
│
└── 👀 {Colors.CYAN}TU PANEL{Colors.END} → http://localhost:5000
    ├── 📋 Lista todas las IPs públicas conectadas
    ├── 🖥️ Info completa de cada máquina (SO, usuario, etc.)
    └── 📊 Datos capturados en tiempo real

{Colors.RED}🔥 RESULTADO: VES LA IP PÚBLICA REAL DE CADA KEYLOGGER{Colors.END}
    """)

def simulate_server():
    """Simular servidor recibiendo conexiones"""
    print(f"\n{Colors.PURPLE}🖥️ SIMULANDO TU SERVIDOR CENTRAL...{Colors.END}")
    
    fake_server_ip = "203.45.67.89"  # IP pública simulada tuya
    
    print(f"""
{Colors.GREEN}✅ Servidor iniciado en tu máquina:{Colors.END}
├── 🌍 Tu IP pública: {Colors.CYAN}{fake_server_ip}{Colors.END}
├── 🔌 Puerto TCP: {Colors.BLUE}9999{Colors.END}
├── 🌐 Panel web: {Colors.BLUE}http://localhost:5000{Colors.END}
└── ⏳ Esperando conexiones de keyloggers...
    """)
    
    time.sleep(2)
    
    # Simular clientes conectándose
    fake_clients = [
        {
            'ip': '198.12.34.56', 
            'hostname': 'LAPTOP-TRABAJO', 
            'os': 'Windows 11',
            'user': 'maria.gonzalez'
        },
        {
            'ip': '177.88.99.12', 
            'hostname': 'MacBook-Office', 
            'os': 'macOS Monterey',
            'user': 'carlos.lopez'
        },
        {
            'ip': '159.33.44.78', 
            'hostname': 'Ubuntu-Dev', 
            'os': 'Ubuntu 22.04',
            'user': 'admin'
        }
    ]
    
    print(f"\n{Colors.YELLOW}📡 CLIENTES CONECTÁNDOSE...{Colors.END}")
    
    for i, client in enumerate(fake_clients, 1):
        time.sleep(1.5)
        
        print(f"\n{Colors.GREEN}🔌 Nueva conexión #{i}:{Colors.END}")
        print(f"├── 🌍 IP Pública: {Colors.CYAN}{client['ip']}{Colors.END}")
        print(f"├── 🖥️ Hostname: {Colors.WHITE}{client['hostname']}{Colors.END}")
        print(f"├── 💻 Sistema: {Colors.WHITE}{client['os']}{Colors.END}")
        print(f"└── 👤 Usuario: {Colors.WHITE}{client['user']}{Colors.END}")
        
        # Simular datos llegando
        time.sleep(0.5)
        sample_data = [
            "password123", 
            "admin@empresa.com",
            "documento_secreto.pdf",
            "ctrl+c", "ctrl+v"
        ]
        
        for data in sample_data[:2]:  # Solo mostrar algunos
            print(f"  📊 Capturado: {Colors.YELLOW}'{data}'{Colors.END}")
            time.sleep(0.3)

def show_panel_simulation():
    """Simular el panel web"""
    print(f"\n{Colors.CYAN}🌐 TU PANEL DE CONTROL - http://localhost:5000{Colors.END}")
    
    panel_display = f"""
{Colors.WHITE}╔════════════════════════════════════════════════════════════╗
║                    🌐 PANEL DE CONTROL                     ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  📊 ESTADÍSTICAS:                                          ║
║  ├── Clientes Totales: 3                                  ║
║  ├── En Línea: 3                                          ║
║  └── Eventos: 1,247                                       ║
║                                                            ║
║  🔗 CLIENTES CONECTADOS:                                   ║
║                                                            ║
║  🟢 198.12.34.56 - LAPTOP-TRABAJO (Windows 11)            ║
║     └── Usuario: maria.gonzalez - Eventos: 523            ║
║                                                            ║
║  🟢 177.88.99.12 - MacBook-Office (macOS Monterey)        ║
║     └── Usuario: carlos.lopez - Eventos: 412              ║
║                                                            ║
║  🟢 159.33.44.78 - Ubuntu-Dev (Ubuntu 22.04)             ║
║     └── Usuario: admin - Eventos: 312                     ║
║                                                            ║
║  📋 ÚLTIMOS EVENTOS:                                       ║
║  ├── [15:23] 198.12.34.56: "password123"                  ║
║  ├── [15:22] 177.88.99.12: "admin@empresa.com"            ║
║  └── [15:21] 159.33.44.78: "documento_secreto.pdf"        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝{Colors.END}
    """
    
    print(panel_display)

def show_real_usage():
    """Mostrar uso real del sistema"""
    print(f"\n{Colors.GREEN}🚀 CÓMO USAR EL SISTEMA REAL:{Colors.END}")
    
    current_dir = Path(__file__).parent
    
    print(f"""
{Colors.YELLOW}1️⃣ EN TU MÁQUINA (Servidor Central):{Colors.END}
{Colors.CYAN}cd {current_dir}{Colors.END}
{Colors.WHITE}python3 start_server.py{Colors.END}

{Colors.BLUE}   ↳ Esto te dará TU IP pública para configurar clientes{Colors.END}

{Colors.YELLOW}2️⃣ EN CADA MÁQUINA OBJETIVO (Cliente):{Colors.END}
{Colors.CYAN}cd {current_dir}{Colors.END}
{Colors.WHITE}python3 start_client.py{Colors.END}

{Colors.BLUE}   ↳ Te pedirá la IP del servidor (la tuya del paso 1){Colors.END}

{Colors.YELLOW}3️⃣ MONITOREAR TODO:{Colors.END}
{Colors.WHITE}http://localhost:5000{Colors.END}

{Colors.BLUE}   ↳ Ve todas las IPs públicas y datos en tiempo real{Colors.END}

{Colors.RED}🔥 RESULTADO:{Colors.END}
✅ Verás la IP PÚBLICA REAL de cada máquina (no 192.168.x.x)
✅ Control centralizado desde tu máquina
✅ Datos de múltiples keyloggers organizados por IP
✅ Reconexión automática si se pierde conexión
    """)

def show_advantages():
    """Mostrar ventajas del sistema"""
    print(f"\n{Colors.PURPLE}💎 VENTAJAS DE ESTE SISTEMA:{Colors.END}")
    
    print(f"""
{Colors.GREEN}🆚 VS KEYLOGGER LOCAL BÁSICO:{Colors.END}
├── ❌ Local: Solo ve 192.168.1.x (IP local inútil)
└── ✅ Remoto: Ve 198.12.34.56 (IP pública real útil)

{Colors.GREEN}🆚 VS OTROS SISTEMAS:{Colors.END}  
├── ❌ Otros: Configuración complicada
└── ✅ Este: Solo 2 comandos (start_server.py y start_client.py)

{Colors.GREEN}🆚 VS HERRAMIENTAS COMERCIALES:{Colors.END}
├── ❌ Comercial: Caras y con limitaciones
└── ✅ Este: Gratis, código abierto y personalizable

{Colors.GREEN}🔥 CARACTERÍSTICAS ÚNICAS:{Colors.END}
├── 🌍 IP pública real automática
├── 🌐 Panel web profesional  
├── 📊 Estadísticas en tiempo real
├── 🔄 Reconexión automática
├── 📁 Datos organizados por IP
└── 🛡️ Encriptación de datos
    """)

def main():
    """Demo principal"""
    print_demo_banner()
    
    input(f"\n{Colors.WHITE}Presiona Enter para ver la simulación...{Colors.END}")
    
    # Simular servidor
    simulate_server()
    
    time.sleep(2)
    
    # Mostrar panel
    show_panel_simulation()
    
    input(f"\n{Colors.WHITE}Presiona Enter para ver instrucciones reales...{Colors.END}")
    
    # Mostrar uso real
    show_real_usage()
    
    input(f"\n{Colors.WHITE}Presiona Enter para ver ventajas...{Colors.END}")
    
    # Mostrar ventajas
    show_advantages()
    
    print(f"\n{Colors.GREEN}🎯 ¡El sistema está listo para usarse!{Colors.END}")
    
    choice = input(f"\n{Colors.CYAN}¿Quieres iniciar el servidor real ahora? (s/N): {Colors.END}").lower()
    
    if choice in ['s', 'si', 'y', 'yes']:
        print(f"\n{Colors.GREEN}🚀 Iniciando servidor real...{Colors.END}")
        try:
            os.system("python3 start_server.py")
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Servidor detenido{Colors.END}")
    else:
        print(f"\n{Colors.BLUE}Para iniciar manualmente:{Colors.END}")
        print(f"  {Colors.WHITE}python3 start_server.py{Colors.END}")

if __name__ == "__main__":
    main()
