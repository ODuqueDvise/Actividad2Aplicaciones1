"""
Punto de entrada principal de la aplicación de cifrado y descifrado.

Autor: Orlando Duque Cantor
Cédula: 80171794
Correo: oduque94@unisalle.edu.co
Asignatura: Aplicaciones I
"""

import sys
from PyQt6 import QtWidgets
from src.ui.app_window import AplicacionCifrado


def main():
    """Función principal que inicia la aplicación."""
    app = QtWidgets.QApplication(sys.argv)
    ventana = AplicacionCifrado()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
