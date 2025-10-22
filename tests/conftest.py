"""
Configuración de pytest para los tests del proyecto.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path de Python para permitir imports
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
