
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
