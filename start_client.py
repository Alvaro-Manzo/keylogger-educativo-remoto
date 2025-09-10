#!/usr/bin/env python3
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
