"""
Módulo de lógica de cifrado y descifrado.
Contiene las funciones para cifrar y descifrar números de 6 dígitos.
"""


class CipherLogic:
    """Clase que encapsula la lógica de cifrado y descifrado."""

    @staticmethod
    def cifrar(numero_str: str) -> str:
        """
        Cifra un número de 6 dígitos.

        Algoritmo:
        1. Suma 7 a cada dígito y obtiene el residuo de división entre 10
        2. Intercambia posiciones: 1º con 3º, 2º con 4º, 5º con 6º

        Args:
            numero_str: Cadena con el número de 6 dígitos

        Returns:
            Cadena con el número cifrado
        """
        # Cifrado: sumar 7 y obtener residuo de división entre 10
        digitos_cifrados = []
        for digito in numero_str:
            cifrado = (int(digito) + 7) % 10
            digitos_cifrados.append(str(cifrado))

        # Intercambiar posiciones: 1er con 3er, 2do con 4to, 5to con 6to
        digitos_intercambiados = digitos_cifrados.copy()
        digitos_intercambiados[0], digitos_intercambiados[2] = digitos_cifrados[2], digitos_cifrados[0]
        digitos_intercambiados[1], digitos_intercambiados[3] = digitos_cifrados[3], digitos_cifrados[1]
        digitos_intercambiados[4], digitos_intercambiados[5] = digitos_cifrados[5], digitos_cifrados[4]

        return ''.join(digitos_intercambiados)

    @staticmethod
    def descifrar(numero_str: str) -> str:
        """
        Descifra un número de 6 dígitos.

        Algoritmo (inverso al cifrado):
        1. Intercambia posiciones: 1º con 3º, 2º con 4º, 5º con 6º
        2. Resta 7 a cada dígito (módulo 10)

        Args:
            numero_str: Cadena con el número cifrado de 6 dígitos

        Returns:
            Cadena con el número original
        """
        # Paso 1: Invertir los intercambios (1er con 3er, 2do con 4to, 5to con 6to)
        digitos_desintercambiados = list(numero_str)
        digitos_desintercambiados[0], digitos_desintercambiados[2] = numero_str[2], numero_str[0]
        digitos_desintercambiados[1], digitos_desintercambiados[3] = numero_str[3], numero_str[1]
        digitos_desintercambiados[4], digitos_desintercambiados[5] = numero_str[5], numero_str[4]

        # Paso 2: Revertir el cifrado (restar 7 mod 10)
        digitos_originales = []
        for digito in digitos_desintercambiados:
            original = (int(digito) - 7) % 10
            digitos_originales.append(str(original))

        return ''.join(digitos_originales)
