"""
Módulo de la ventana principal de la aplicación.
Gestiona la navegación entre las diferentes ventanas.
"""

from PyQt6 import QtWidgets
from src.ui.ventana_principal import VentanaPrincipal
from src.ui.ventana_cifrado import VentanaCifrado
from src.ui.ventana_descifrado import VentanaDescifrado


class AplicacionCifrado(QtWidgets.QMainWindow):
    """Ventana principal de la aplicación que gestiona la navegación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación de Cifrado y Descifrado")
        self.setGeometry(100, 100, 600, 400)

        # Widget principal con stack para cambiar entre ventanas
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)

        # Crear las tres ventanas
        self.ventana_principal = VentanaPrincipal(self.cambiar_ventana)
        self.ventana_cifrado = VentanaCifrado(self.cambiar_ventana)
        self.ventana_descifrado = VentanaDescifrado(self.cambiar_ventana)

        # Agregar ventanas al stack
        self.stack.addWidget(self.ventana_principal)
        self.stack.addWidget(self.ventana_cifrado)
        self.stack.addWidget(self.ventana_descifrado)

        # Mostrar ventana principal
        self.stack.setCurrentWidget(self.ventana_principal)

    def cambiar_ventana(self, ventana_id: str):
        """
        Cambia entre las diferentes ventanas.

        Args:
            ventana_id: Identificador de la ventana ("principal", "cifrado", "descifrado")
        """
        if ventana_id == "principal":
            self.stack.setCurrentWidget(self.ventana_principal)
        elif ventana_id == "cifrado":
            self.stack.setCurrentWidget(self.ventana_cifrado)
        elif ventana_id == "descifrado":
            self.stack.setCurrentWidget(self.ventana_descifrado)
