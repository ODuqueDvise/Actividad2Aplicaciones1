"""
Módulo de validación de datos.
Contiene funciones para validar entradas del usuario.
"""

from typing import Tuple


class Validator:
    """Clase que encapsula las validaciones de entrada."""

    @staticmethod
    def validar_numero_6_digitos(numero_str: str) -> Tuple[bool, str]:
        """
        Valida que la entrada sea un número de 6 dígitos.

        Args:
            numero_str: Cadena a validar

        Returns:
            Tupla (es_valido, mensaje_error)
            - es_valido: True si la validación pasa, False en caso contrario
            - mensaje_error: Mensaje descriptivo del error (vacío si es válido)
        """
        # Validar que no esté vacío
        if not numero_str:
            return False, "Por favor ingrese un número"

        # Validar longitud
        if len(numero_str) != 6:
            return False, "El número debe tener exactamente 6 dígitos"

        # Validar que sean solo dígitos
        if not numero_str.isdigit():
            return False, "Solo se aceptan dígitos numéricos"

        return True, ""
