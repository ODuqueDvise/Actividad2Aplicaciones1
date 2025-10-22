"""
Módulo de la ventana de cifrado.
"""

from PyQt6 import QtWidgets, QtCore, QtGui
from src.logic.cipher import CipherLogic
from src.utils.validators import Validator


class VentanaCifrado(QtWidgets.QWidget):
    """Ventana para cifrar números de 6 dígitos."""

    def __init__(self, cambiar_ventana_callback):
        super().__init__()
        self.cambiar_ventana = cambiar_ventana_callback
        self.cipher = CipherLogic()
        self.validator = Validator()
        self.entrada = QtWidgets.QLineEdit()
        self.resultado_label = QtWidgets.QLabel("Número cifrado:")
        self.resultado = QtWidgets.QLineEdit()
        self.init_ui()

    def init_ui(self):
        """Inicializa la interfaz de la ventana de cifrado."""
        layout = QtWidgets.QVBoxLayout()

        # Título
        titulo = QtWidgets.QLabel("Ventana de Cifrado")
        titulo_font = QtGui.QFont()
        titulo_font.setPointSize(14)
        titulo_font.setBold(True)
        titulo.setFont(titulo_font)
        titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        # Instrucciones
        instrucciones = QtWidgets.QLabel("Ingrese un número entero de 6 dígitos:")
        layout.addWidget(instrucciones)

        # Campo de entrada
        self.entrada.setPlaceholderText("Ej: 123456")
        self.entrada.setMaxLength(6)
        # Validador para solo aceptar números
        validador = QtGui.QIntValidator(0, 999999, self)
        self.entrada.setValidator(validador)
        layout.addWidget(self.entrada)

        # Botón de cifrado
        btn_cifrar = QtWidgets.QPushButton("Cifrar")
        btn_cifrar.setMinimumHeight(40)
        btn_cifrar.clicked.connect(self.cifrar)
        layout.addWidget(btn_cifrar)

        # Etiqueta para resultado
        self.resultado_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold))
        layout.addWidget(self.resultado_label)

        # Campo de resultado (solo lectura)
        self.resultado.setReadOnly(True)
        self.resultado.setStyleSheet("background-color: #f0f0f0;")
        layout.addWidget(self.resultado)

        layout.addSpacing(20)

        # Botón de retorno
        btn_volver = QtWidgets.QPushButton("Volver a Principal")
        btn_volver.setMinimumHeight(40)
        btn_volver.clicked.connect(lambda: self.cambiar_ventana("principal"))
        layout.addWidget(btn_volver)

        layout.addStretch()

        self.setLayout(layout)

    def cifrar(self):
        """Realiza el cifrado del número ingresado."""
        numero_str = self.entrada.text().strip()

        # Validar entrada
        es_valido, mensaje_error = self.validator.validar_numero_6_digitos(numero_str)
        if not es_valido:
            QtWidgets.QMessageBox.warning(self, "Error", mensaje_error)
            return

        # Cifrar número
        numero_cifrado = self.cipher.cifrar(numero_str)

        # Mostrar resultado
        self.resultado.setText(numero_cifrado)

        # Crear diálogo personalizado con botón de copiar
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Éxito")
        msg_box.setText(f"Número original: {numero_str}\nNúmero cifrado: {numero_cifrado}")
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)

        # Agregar botones
        btn_copiar = msg_box.addButton("Copiar resultado", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg_box.addButton(QtWidgets.QMessageBox.StandardButton.Ok)

        msg_box.exec()

        # Si se presionó el botón copiar
        if msg_box.clickedButton() == btn_copiar:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(numero_cifrado)
            QtWidgets.QMessageBox.information(self, "Copiado", "Resultado copiado al portapapeles")
