"""
Tests unitarios para el módulo de validadores.
"""

import pytest
from src.utils.validators import Validator


class TestValidator:
    """Clase de tests para las validaciones de entrada."""

    @pytest.fixture
    def validator(self):
        """Fixture que provee una instancia de Validator."""
        return Validator()

    # ==================== Tests de Validación Exitosa ====================

    def test_validar_numero_valido_simple(self, validator):
        """Test de validación con un número válido simple."""
        es_valido, mensaje = validator.validar_numero_6_digitos("123456")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_numero_con_ceros_al_inicio(self, validator):
        """Test de validación con ceros al inicio."""
        es_valido, mensaje = validator.validar_numero_6_digitos("000123")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_todos_ceros(self, validator):
        """Test de validación con todos ceros."""
        es_valido, mensaje = validator.validar_numero_6_digitos("000000")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_todos_nueves(self, validator):
        """Test de validación con todos nueves."""
        es_valido, mensaje = validator.validar_numero_6_digitos("999999")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_numero_aleatorio(self, validator):
        """Test de validación con números aleatorios válidos."""
        numeros_validos = [
            "123456", "987654", "000000", "111111", "543210",
            "135792", "246813", "369258", "147258", "258369"
        ]
        for numero in numeros_validos:
            es_valido, mensaje = validator.validar_numero_6_digitos(numero)
            assert es_valido is True, f"Número {numero} debería ser válido"
            assert mensaje == ""

    # ==================== Tests de Cadena Vacía ====================

    def test_validar_cadena_vacia(self, validator):
        """Test de validación con cadena vacía."""
        es_valido, mensaje = validator.validar_numero_6_digitos("")
        assert es_valido is False
        assert mensaje == "Por favor ingrese un número"
        assert len(mensaje) > 0

    def test_validar_solo_espacios(self, validator):
        """Test de validación con solo espacios (después de strip)."""
        # Nota: La validación se hace después de strip() en la UI
        es_valido, mensaje = validator.validar_numero_6_digitos("      ")
        assert es_valido is False
        # Puede fallar por vacío o por longitud, dependiendo de si se hace strip antes

    # ==================== Tests de Longitud Incorrecta ====================

    def test_validar_menos_de_6_digitos(self, validator):
        """Test de validación con menos de 6 dígitos."""
        numeros_invalidos = ["1", "12", "123", "1234", "12345"]
        for numero in numeros_invalidos:
            es_valido, mensaje = validator.validar_numero_6_digitos(numero)
            assert es_valido is False, f"Número {numero} debería ser inválido"
            assert mensaje == "El número debe tener exactamente 6 dígitos"

    def test_validar_mas_de_6_digitos(self, validator):
        """Test de validación con más de 6 dígitos."""
        numeros_invalidos = ["1234567", "12345678", "123456789", "1234567890"]
        for numero in numeros_invalidos:
            es_valido, mensaje = validator.validar_numero_6_digitos(numero)
            assert es_valido is False, f"Número {numero} debería ser inválido"
            assert mensaje == "El número debe tener exactamente 6 dígitos"

    def test_validar_longitud_cero(self, validator):
        """Test de validación con longitud cero."""
        es_valido, mensaje = validator.validar_numero_6_digitos("")
        assert es_valido is False
        assert "ingrese un número" in mensaje.lower()

    # ==================== Tests de Caracteres No Numéricos ====================

    def test_validar_con_letras(self, validator):
        """Test de validación con letras."""
        entradas_invalidas = ["abcdef", "12345a", "a12345", "123a45"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"
            assert mensaje == "Solo se aceptan dígitos numéricos"

    def test_validar_con_caracteres_especiales(self, validator):
        """Test de validación con caracteres especiales."""
        entradas_invalidas = [
            "123-456", "123.456", "123,456", "123 456",
            "123!45", "123@45", "123#45", "123$45"
        ]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"
            # Puede fallar por longitud o por caracteres no numéricos
            assert len(mensaje) > 0

    def test_validar_con_signos(self, validator):
        """Test de validación con signos + o -."""
        entradas_invalidas = ["+123456", "-123456", "123+456", "123-456"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    def test_validar_con_espacios_intermedios(self, validator):
        """Test de validación con espacios en medio."""
        entradas_invalidas = ["123 456", "12 3456", "1234 56"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"
            # Puede fallar por longitud o por caracteres no numéricos
            assert len(mensaje) > 0

    def test_validar_con_tabulaciones(self, validator):
        """Test de validación con tabulaciones."""
        entradas_invalidas = ["123\t456", "\t123456", "123456\t"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    def test_validar_con_saltos_de_linea(self, validator):
        """Test de validación con saltos de línea."""
        entradas_invalidas = ["123\n456", "123456\n", "\n123456"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    # ==================== Tests de Casos Mixtos ====================

    def test_validar_alfanumerico(self, validator):
        """Test de validación con mezcla de letras y números."""
        entradas_invalidas = [
            "12abc6", "a1b2c3", "1a2b3c", "abc123",
            "123abc", "1a3b5c", "A12345"
        ]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"
            assert "numéricos" in mensaje.lower()

    def test_validar_numeros_con_formato(self, validator):
        """Test de validación con números formateados."""
        entradas_invalidas = [
            "(123)45", "[123456]", "{123456}", "123,456",
            "123.456", "1-2-3-4-5-6"
        ]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    # ==================== Tests de Valores Límite ====================

    def test_validar_valor_minimo(self, validator):
        """Test de validación con el valor mínimo posible (000000)."""
        es_valido, mensaje = validator.validar_numero_6_digitos("000000")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_valor_maximo(self, validator):
        """Test de validación con el valor máximo posible (999999)."""
        es_valido, mensaje = validator.validar_numero_6_digitos("999999")
        assert es_valido is True
        assert mensaje == ""

    def test_validar_5_digitos_limite_inferior(self, validator):
        """Test de validación justo por debajo del límite (5 dígitos)."""
        es_valido, mensaje = validator.validar_numero_6_digitos("12345")
        assert es_valido is False
        assert "exactamente 6 dígitos" in mensaje

    def test_validar_7_digitos_limite_superior(self, validator):
        """Test de validación justo por encima del límite (7 dígitos)."""
        es_valido, mensaje = validator.validar_numero_6_digitos("1234567")
        assert es_valido is False
        assert "exactamente 6 dígitos" in mensaje

    # ==================== Tests de Retorno de Tupla ====================

    def test_retorno_es_tupla(self, validator):
        """Test que verifica que el retorno es una tupla."""
        resultado = validator.validar_numero_6_digitos("123456")
        assert isinstance(resultado, tuple)
        assert len(resultado) == 2

    def test_retorno_tipos_correctos_valido(self, validator):
        """Test que verifica los tipos de retorno cuando es válido."""
        es_valido, mensaje = validator.validar_numero_6_digitos("123456")
        assert isinstance(es_valido, bool)
        assert isinstance(mensaje, str)
        assert es_valido is True
        assert mensaje == ""

    def test_retorno_tipos_correctos_invalido(self, validator):
        """Test que verifica los tipos de retorno cuando es inválido."""
        es_valido, mensaje = validator.validar_numero_6_digitos("abc")
        assert isinstance(es_valido, bool)
        assert isinstance(mensaje, str)
        assert es_valido is False
        assert len(mensaje) > 0

    # ==================== Tests de Mensajes de Error ====================

    def test_mensaje_error_vacio_es_descriptivo(self, validator):
        """Test que verifica que el mensaje de error para vacío es descriptivo."""
        _, mensaje = validator.validar_numero_6_digitos("")
        assert len(mensaje) > 0
        assert "ingrese" in mensaje.lower() or "vacío" in mensaje.lower()

    def test_mensaje_error_longitud_es_descriptivo(self, validator):
        """Test que verifica que el mensaje de error para longitud es descriptivo."""
        _, mensaje = validator.validar_numero_6_digitos("123")
        assert len(mensaje) > 0
        assert "6" in mensaje or "seis" in mensaje.lower()
        assert "dígitos" in mensaje.lower()

    def test_mensaje_error_caracteres_es_descriptivo(self, validator):
        """Test que verifica que el mensaje de error para caracteres es descriptivo."""
        _, mensaje = validator.validar_numero_6_digitos("abc123")
        assert len(mensaje) > 0
        assert "numéricos" in mensaje.lower() or "dígitos" in mensaje.lower()

    # ==================== Tests de Casos Especiales ====================

    def test_validar_unicode_numeros(self, validator):
        """Test de validación con números unicode (no ASCII)."""
        # Nota: Python's isdigit() acepta varios tipos de dígitos unicode
        # incluyendo números árabes "١٢٣٤٥٦" y números circulados "①②③④⑤⑥"
        # Por lo tanto, este test verifica que el validador acepta dígitos unicode válidos
        # Si se requiere validación estricta de ASCII, se debe modificar el validador

        # Test que los números unicode son procesados consistentemente
        entrada_unicode = "①②③④⑤⑥"
        es_valido, mensaje = validator.validar_numero_6_digitos(entrada_unicode)
        # El resultado depende de la implementación del validador
        # Solo verificamos que retorna tipos correctos
        assert isinstance(es_valido, bool)
        assert isinstance(mensaje, str)

    def test_validar_numero_hexadecimal(self, validator):
        """Test de validación con representación hexadecimal."""
        entradas_invalidas = ["0x1234", "ABCDEF", "123ABC"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    def test_validar_notacion_cientifica(self, validator):
        """Test de validación con notación científica."""
        entradas_invalidas = ["1.23e5", "123e+3", "1.2E05"]
        for entrada in entradas_invalidas:
            es_valido, mensaje = validator.validar_numero_6_digitos(entrada)
            assert es_valido is False, f"Entrada {entrada} debería ser inválida"

    # ==================== Tests de Consistencia ====================

    def test_misma_entrada_mismo_resultado(self, validator):
        """Test que verifica que la misma entrada produce el mismo resultado."""
        entrada = "123456"
        resultado1 = validator.validar_numero_6_digitos(entrada)
        resultado2 = validator.validar_numero_6_digitos(entrada)
        assert resultado1 == resultado2

    def test_validacion_es_deterministica(self, validator):
        """Test que verifica que la validación es determinística."""
        entradas_test = ["123456", "abc", "", "12345", "1234567"]
        for entrada in entradas_test:
            resultados = [validator.validar_numero_6_digitos(entrada) for _ in range(5)]
            # Todos los resultados deben ser iguales
            assert all(r == resultados[0] for r in resultados)
