"""
Módulo de la ventana de descifrado.
"""

from PyQt6 import QtWidgets, QtCore, QtGui
from src.logic.cipher import CipherLogic
from src.utils.validators import Validator


class VentanaDescifrado(QtWidgets.QWidget):
    """Ventana para descifrar números de 6 dígitos."""

    def __init__(self, cambiar_ventana_callback):
        super().__init__()
        self.cambiar_ventana = cambiar_ventana_callback
        self.cipher = CipherLogic()
        self.validator = Validator()
        self.entrada = QtWidgets.QLineEdit()
        self.resultado_label = QtWidgets.QLabel("Número original:")
        self.resultado = QtWidgets.QLineEdit()
        self.btn_copiar = QtWidgets.QPushButton("Copiar resultado")
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de la ventana de descifrado."""
        layout = QtWidgets.QVBoxLayout()

        # Título
        titulo = QtWidgets.QLabel("Ventana de Descifrado")
        titulo_font = QtGui.QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        # Instrucciones
        instrucciones = QtWidgets.QLabel("Ingrese el número cifrado de 6 dígitos:")
        layout.addWidget(instrucciones)

        # Campo de entrada
        self.entrada.setPlaceholderText("Ej: 890123")
        self.entrada.setMaxLength(6)
        # Validador para solo aceptar números
        validador = QtGui.QIntValidator(0, 999999, self)
        self.entrada.setValidator(validador)
        layout.addWidget(self.entrada)

        # Botón de descifrado
        btn_descifrar = QtWidgets.QPushButton("Descifrar")
        btn_descifrar.setMinimumHeight(40)
        btn_descifrar.clicked.connect(self.descifrar)
        layout.addWidget(btn_descifrar)

        # Etiqueta para resultado
        self.resultado_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold))
        layout.addWidget(self.resultado_label)

        # Campo de resultado (solo lectura)
        self.resultado.setReadOnly(True)
        self.resultado.setStyleSheet("background-color: #ffffff; color: #000000; padding: 5px; border: 1px solid #cccccc;")
        layout.addWidget(self.resultado)

        # Botón copiar resultado
        self.btn_copiar.setMinimumHeight(35)
        self.btn_copiar.clicked.connect(self.copiar_resultado)
        self.btn_copiar.setEnabled(False)  # Deshabilitado hasta que haya resultado
        layout.addWidget(self.btn_copiar)

        layout.addSpacing(20)

        # Botón de retorno
        btn_volver = QtWidgets.QPushButton("Volver a Principal")
        btn_volver.setMinimumHeight(40)
        btn_volver.clicked.connect(lambda: self.cambiar_ventana("principal"))
        layout.addWidget(btn_volver)

        layout.addStretch()

        self.setLayout(layout)

    def descifrar(self):
        """Realiza el descifrado del número ingresado."""
        numero_str = self.entrada.text().strip()

        # Validar entrada
        es_valido, mensaje_error = self.validator.validar_numero_6_digitos(numero_str)
        if not es_valido:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje_error)
            return

        # Descifrar número
        numero_original = self.cipher.descifrar(numero_str)

        # Mostrar resultado en el campo
        self.resultado.setText(numero_original)

        # Habilitar el botón de copiar
        self.btn_copiar.setEnabled(True)

    def copiar_resultado(self):
        """Copia el resultado al portapapeles."""
        texto_resultado = self.resultado.text()
        if texto_resultado:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(texto_resultado)
            QtWidgets.QMessageBox.information(self, "Copiado", "Resultado copiado al portapapeles")
