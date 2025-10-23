"""
Módulo de la ventana principal de la aplicación.
"""

from PyQt6 import QtWidgets, QtCore, QtGui


class VentanaPrincipal(QtWidgets.QWidget):
    """Ventana principal con información del autor y navegación."""

    def __init__(self, cambiar_ventana_callback):
        super().__init__()
        self.cambiar_ventana = cambiar_ventana_callback
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de la ventana principal."""
        layout = QtWidgets.QVBoxLayout()

        # Título
        titulo = QtWidgets.QLabel("Bienvenido a la Aplicación de Cifrado")
        titulo_font = QtGui.QFont()
        titulo_font.setPointSize(16)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        # Información del autor
        info_label = QtWidgets.QLabel("Información del Autor")
        info_font = QtGui.QFont()
        info_font.setPointSize(12)
        info_font.setBold(True)
        info_label.setFont(info_font)
        layout.addWidget(info_label)

        # Datos autor
        datos_layout = QtWidgets.QVBoxLayout()
        datos_layout.addWidget(QtWidgets.QLabel("Nombre: Orlando Duque Cantor"))
        datos_layout.addWidget(QtWidgets.QLabel("Cédula: 80171794"))
        datos_layout.addWidget(QtWidgets.QLabel("Correo: oduque94@unisalle.edu.co"))
        datos_layout.addWidget(QtWidgets.QLabel("Asignatura: Aplicaciones I"))
        layout.addLayout(datos_layout)

        layout.addSpacing(30)

        # Botones de navegación
        botones_layout = QtWidgets.QHBoxLayout()

        btn_cifrado = QtWidgets.QPushButton("Ir a Cifrado")
        btn_cifrado.setMinimumHeight(40)
        btn_cifrado.clicked.connect(lambda: self.cambiar_ventana("cifrado"))
        botones_layout.addWidget(btn_cifrado)

        btn_descifrado = QtWidgets.QPushButton("Ir a Descifrado")
        btn_descifrado.setMinimumHeight(40)
        btn_descifrado.clicked.connect(lambda: self.cambiar_ventana("descifrado"))
        botones_layout.addWidget(btn_descifrado)

        layout.addLayout(botones_layout)
        layout.addStretch()

        self.setLayout(layout)
