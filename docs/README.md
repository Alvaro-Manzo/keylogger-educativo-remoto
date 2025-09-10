# 🔍 Keylogger Educativo Avanzado

Un keylogger educativo potente y ético con interfaz moderna y dashboard web interactivo.

## ⚠️ AVISO LEGAL

**Este software es únicamente para fines educativos y uso en sistemas propios.**
- Solo usar en equipos de tu propiedad
- Informar a otros usuarios cuando sea requerido por ley
- Respetar la privacidad de terceros
- Cumplir con las leyes locales de tu país

El uso indebido puede ser ilegal. El autor no se hace responsable del mal uso del software.

## 🚀 Características

### ✨ Interfaz Moderna
- **Colores vibrantes** en terminal
- **Menú interactivo** fácil de usar
- **Estadísticas en tiempo real**
- **Progreso visual** de actividad

### 🔐 Seguridad
- **Encriptación** de logs con Fernet
- **Claves únicas** por instalación
- **Rotación automática** de archivos
- **Configuración personalizable**

### 📊 Dashboard Web
- **Interfaz web moderna** con gráficos
- **Estadísticas interactivas**
- **Mapas de calor** de actividad
- **Visualización en tiempo real**

### 🖱️ Captura Avanzada
- **Teclas presionadas** con timestamp
- **Clicks de mouse** con coordenadas
- **Títulos de ventanas** activas
- **Información del sistema**

### 🌐 Transferencia Segura
- **Servidor HTTP** integrado
- **Códigos QR** para fácil transferencia
- **Paquetes ZIP** autocontenidos
- **Claves de transferencia** únicas

## 📋 Requisitos del Sistema

- **Python 3.7+**
- **macOS, Windows o Linux**
- **Permisos de administrador** (para captura de teclado)
- **Conexión a internet** (para instalación de dependencias)

## 🛠️ Instalación

### Opción 1: Instalación Manual

1. **Clonar o descargar** este proyecto
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el keylogger**:
   ```bash
   python keylogger_advanced.py
   ```

### Opción 2: Usando el Script de Instalación

1. **Ejecutar script automático**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

### Opción 3: Transferencia Remota

1. **En el equipo origen**, ejecutar:
   ```bash
   python transfer_utility.py
   ```

2. **Crear paquete e iniciar servidor**
3. **Escanear código QR** o visitar la URL mostrada
4. **Descargar e instalar** en el dispositivo destino

## 🎮 Uso

### Keylogger Principal

```bash
python keylogger_advanced.py
```

**Menú principal:**
- `1` - Iniciar keylogger
- `2` - Ver logs recientes  
- `3` - Configurar opciones
- `4` - Ver estadísticas
- `5` - Salir

### Dashboard Web

```bash
python dashboard.py
```

Luego visita: http://localhost:5000

**Características del dashboard:**
- 📊 Estadísticas en tiempo real
- 📈 Gráficos de actividad por hora
- 📋 Lista de eventos recientes
- 🔄 Auto-actualización cada 30 segundos

### Utilidad de Transferencia

```bash
python transfer_utility.py
```

**Opciones disponibles:**
- Crear paquete ZIP
- Iniciar servidor de transferencia
- Generar código QR
- Transferencia segura entre dispositivos

## ⚙️ Configuración

El archivo `config.json` permite personalizar:

```json
{
    "log_file": "keylogger_data.enc",
    "max_file_size": 5242880,
    "capture_mouse": true,
    "capture_window_titles": true,
    "auto_backup": true,
    "backup_interval": 3600,
    "encryption_enabled": true,
    "remote_logging": false
}
```

### Opciones principales:

| Opción | Descripción | Valores |
|--------|-------------|---------|
| `capture_mouse` | Capturar clicks del mouse | `true`/`false` |
| `capture_window_titles` | Capturar títulos de ventana | `true`/`false` |
| `encryption_enabled` | Encriptar logs | `true`/`false` |
| `max_file_size` | Tamaño máximo de archivo (bytes) | Número |
| `auto_backup` | Backup automático | `true`/`false` |

## 📁 Estructura de Archivos

```
keylogger-educativo/
├── keylogger_advanced.py    # Keylogger principal
├── dashboard.py             # Dashboard web
├── transfer_utility.py      # Utilidad de transferencia
├── requirements.txt         # Dependencias Python
├── config.json             # Configuración (se crea automáticamente)
├── keylogger.key           # Clave de encriptación (se crea automáticamente)
├── keylogger_data.enc      # Logs encriptados
├── templates/
│   └── dashboard.html      # Plantilla web del dashboard
└── README.md               # Este archivo
```

## 🔒 Seguridad y Privacidad

### Encriptación
- Los logs se encriptan usando **Fernet (AES 128)**
- Cada instalación genera su **clave única**
- La clave se almacena en `keylogger.key`

### Transferencias
- Las transferencias usan **claves temporales**
- Los servidores son **locales** (no externos)
- Los códigos QR contienen **URLs temporales**

### Buenas Prácticas
- ✅ Cambiar passwords después de usar
- ✅ Eliminar logs antiguos regularmente  
- ✅ Usar solo en redes seguras
- ✅ Informar sobre el monitoreo cuando sea legal requerido

## 🚨 Solución de Problemas

### Error de Permisos (macOS)
```bash
# Dar permisos de accesibilidad
Sistema > Seguridad y Privacidad > Privacidad > Accesibilidad
# Añadir Terminal o tu editor de código
```

### Error de Dependencias
```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias individuales
pip install cryptography pynput psutil flask flask-cors qrcode pillow
```

### Puerto en Uso (Dashboard)
```bash
# Cambiar puerto en dashboard.py línea final:
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar 5000 por 5001
```

### Problemas de Encriptación
```bash
# Eliminar clave corrupta y regenerar
rm keylogger.key
python keylogger_advanced.py
```

## 🎯 Casos de Uso Educativos

### 1. Análisis de Comportamiento
- Estudiar patrones de escritura
- Analizar productividad personal
- Identificar hábitos de navegación

### 2. Seguridad Informática
- Demostrar vulnerabilidades
- Enseñar sobre keyloggers maliciosos
- Practicar detección de malware

### 3. Desarrollo de Software
- Aprender sobre APIs del sistema
- Práctica de programación GUI
- Manejo de eventos del sistema

### 4. Análisis Forense
- Investigación de incidentes (propios)
- Recuperación de datos
- Auditoría de actividad

## 🤝 Contribuir

¿Quieres mejorar el proyecto?

1. **Fork** el repositorio
2. **Crea** una rama para tu feature
3. **Commit** tus cambios
4. **Push** a la rama
5. **Abre** un Pull Request

## 📄 Licencia

Este proyecto es para **fines educativos únicamente**.

### Permitido:
- ✅ Uso personal en equipos propios
- ✅ Enseñanza y educación
- ✅ Investigación académica
- ✅ Auditorías de seguridad propias

### Prohibido:
- ❌ Uso comercial sin permiso
- ❌ Instalación en equipos ajenos sin consentimiento
- ❌ Actividades ilegales
- ❌ Violación de privacidad

## 👨‍💻 Autor

**Alvaro Manzo**
- Enfocado en educación y ética
- Desarrollo de herramientas de seguridad
- Promoción del uso responsable de la tecnología

## 🆘 Soporte

¿Necesitas ayuda? 

1. **Revisa** este README
2. **Busca** en la sección de problemas comunes
3. **Verifica** que tengas todos los permisos necesarios
4. **Asegúrate** de usar Python 3.7+

---

**⚠️ Recuerda: Con gran poder viene gran responsabilidad. Usa esta herramienta de manera ética y legal.**
