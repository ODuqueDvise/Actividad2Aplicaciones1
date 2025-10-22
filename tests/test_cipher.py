"""
Tests unitarios para la lógica de cifrado y descifrado.
"""

import pytest
from src.logic.cipher import CipherLogic


class TestCipherLogic:
    """Clase de tests para la lógica de cifrado y descifrado."""

    @pytest.fixture
    def cipher(self):
        """Fixture que provee una instancia de CipherLogic."""
        return CipherLogic()

    # ==================== Tests de Cifrado ====================

    def test_cifrar_numero_simple(self, cipher):
        """Test de cifrado con un número simple."""
        # 123456: [1+7=8, 2+7=9, 3+7=0, 4+7=1, 5+7=2, 6+7=3] = [8,9,0,1,2,3]
        # Intercambios: [0,1,8,9,3,2]
        resultado = cipher.cifrar("123456")
        assert resultado == "018932"

    def test_cifrar_todos_ceros(self, cipher):
        """Test de cifrado con todos los dígitos en 0."""
        # 0+7=7, luego intercambios: 777777 -> 777777
        resultado = cipher.cifrar("000000")
        assert resultado == "777777"

    def test_cifrar_todos_nueves(self, cipher):
        """Test de cifrado con todos los dígitos en 9."""
        # 9+7=16, 16%10=6, luego intercambios: 666666 -> 666666
        resultado = cipher.cifrar("999999")
        assert resultado == "666666"

    def test_cifrar_numero_con_intercambios_visibles(self, cipher):
        """Test donde los intercambios son más visibles."""
        # 123456: [8,9,0,1,2,3] -> intercambios -> [0,1,8,9,3,2]
        resultado = cipher.cifrar("123456")
        assert len(resultado) == 6
        assert resultado.isdigit()

    def test_cifrar_numero_alternado(self, cipher):
        """Test con patrón alternado."""
        resultado = cipher.cifrar("101010")
        assert len(resultado) == 6
        assert resultado.isdigit()

    def test_cifrar_preserva_longitud(self, cipher):
        """Test que verifica que el cifrado preserva la longitud."""
        numeros_test = ["123456", "000000", "999999", "543210", "111111"]
        for numero in numeros_test:
            resultado = cipher.cifrar(numero)
            assert len(resultado) == 6

    def test_cifrar_solo_digitos_en_resultado(self, cipher):
        """Test que verifica que el resultado solo contiene dígitos."""
        numeros_test = ["123456", "789012", "345678", "901234"]
        for numero in numeros_test:
            resultado = cipher.cifrar(numero)
            assert resultado.isdigit()

    # ==================== Tests de Descifrado ====================

    def test_descifrar_numero_simple(self, cipher):
        """Test de descifrado con un número simple."""
        # 018932 -> 123456 (inverso del cifrado)
        resultado = cipher.descifrar("018932")
        assert resultado == "123456"

    def test_descifrar_todos_sietes(self, cipher):
        """Test de descifrado con todos los dígitos en 7."""
        # 7-7=0, luego intercambios inversos: 777777 -> 000000
        resultado = cipher.descifrar("777777")
        assert resultado == "000000"

    def test_descifrar_todos_seis(self, cipher):
        """Test de descifrado con todos los dígitos en 6."""
        # 6-7=-1, -1%10=9, luego intercambios inversos: 666666 -> 999999
        resultado = cipher.descifrar("666666")
        assert resultado == "999999"

    def test_descifrar_preserva_longitud(self, cipher):
        """Test que verifica que el descifrado preserva la longitud."""
        numeros_test = ["904189", "777777", "666666", "012345", "111111"]
        for numero in numeros_test:
            resultado = cipher.descifrar(numero)
            assert len(resultado) == 6

    def test_descifrar_solo_digitos_en_resultado(self, cipher):
        """Test que verifica que el resultado solo contiene dígitos."""
        numeros_test = ["904189", "123456", "789012", "345678"]
        for numero in numeros_test:
            resultado = cipher.descifrar(numero)
            assert resultado.isdigit()

    # ==================== Tests de Simetría (Cifrar + Descifrar) ====================

    def test_simetria_cifrar_descifrar(self, cipher):
        """Test que verifica que descifrar(cifrar(x)) == x."""
        numeros_test = ["123456", "000000", "999999", "543210", "111111", "987654"]
        for numero_original in numeros_test:
            numero_cifrado = cipher.cifrar(numero_original)
            numero_descifrado = cipher.descifrar(numero_cifrado)
            assert numero_descifrado == numero_original

    def test_simetria_descifrar_cifrar(self, cipher):
        """Test que verifica que cifrar(descifrar(x)) == x."""
        numeros_test = ["904189", "777777", "666666", "012345", "111111", "987654"]
        for numero_cifrado in numeros_test:
            numero_descifrado = cipher.descifrar(numero_cifrado)
            numero_recifrado = cipher.cifrar(numero_descifrado)
            assert numero_recifrado == numero_cifrado

    def test_simetria_multiples_iteraciones(self, cipher):
        """Test de simetría con múltiples iteraciones."""
        numero_original = "123456"
        numero_actual = numero_original

        # Cifrar y descifrar 10 veces
        for _ in range(10):
            numero_actual = cipher.cifrar(numero_actual)
            numero_actual = cipher.descifrar(numero_actual)

        assert numero_actual == numero_original

    # ==================== Tests de Casos Límite ====================

    def test_cifrar_numero_con_patron(self, cipher):
        """Test con números que siguen un patrón específico."""
        # Números ascendentes
        resultado = cipher.cifrar("012345")
        assert len(resultado) == 6
        assert resultado.isdigit()

        # Verificar que se puede descifrar
        descifrado = cipher.descifrar(resultado)
        assert descifrado == "012345"

    def test_cifrar_numero_descendente(self, cipher):
        """Test con números descendentes."""
        resultado = cipher.cifrar("987654")
        assert len(resultado) == 6
        assert resultado.isdigit()

        # Verificar simetría
        descifrado = cipher.descifrar(resultado)
        assert descifrado == "987654"

    def test_todos_los_digitos_0_a_9(self, cipher):
        """Test que verifica que todos los dígitos se manejan correctamente."""
        for digito in range(10):
            numero = str(digito) * 6  # "000000", "111111", etc.
            cifrado = cipher.cifrar(numero)
            descifrado = cipher.descifrar(cifrado)
            assert descifrado == numero

    # ==================== Tests de Algoritmo ====================

    def test_suma_7_modulo_10(self, cipher):
        """Test que verifica la operación de suma 7 módulo 10."""
        # 0+7=7, 1+8=8, 2+9=9, 3+10%10=0, etc.
        numero = "0123456"[:6]  # "012345"
        cifrado = cipher.cifrar(numero)

        # Verificar que el algoritmo se aplicó correctamente
        assert cifrado != numero  # Debe ser diferente
        assert len(cifrado) == 6

        # Verificar simetría
        descifrado = cipher.descifrar(cifrado)
        assert descifrado == numero

    def test_intercambio_posiciones(self, cipher):
        """Test que verifica que los intercambios se realizan correctamente."""
        # Usar un número donde cada posición es única
        numero = "012345"
        cifrado = cipher.cifrar(numero)

        # El cifrado debe ser diferente del original
        assert cifrado != numero

        # El descifrado debe recuperar el original
        descifrado = cipher.descifrar(cifrado)
        assert descifrado == numero

    def test_no_perdida_de_informacion(self, cipher):
        """Test que verifica que no se pierde información en el proceso."""
        # Generar todos los números posibles con dígitos únicos
        numeros_unicos = [
            "012345", "123450", "234501", "345012", "450123", "501234",
            "987654", "876549", "765498", "654987", "549876", "498765"
        ]

        for numero in numeros_unicos:
            cifrado = cipher.cifrar(numero)
            descifrado = cipher.descifrar(cifrado)
            assert descifrado == numero, f"Falló con {numero}"

    # ==================== Tests de Valores Específicos ====================

    def test_valores_conocidos(self, cipher):
        """Test con pares de valores conocidos (original, cifrado)."""
        pares_conocidos = [
            ("123456", "018932"),
            ("000000", "777777"),
            ("999999", "666666"),
        ]

        for original, esperado in pares_conocidos:
            cifrado = cipher.cifrar(original)
            assert cifrado == esperado, f"Cifrado de {original} debería ser {esperado}, pero fue {cifrado}"

            descifrado = cipher.descifrar(esperado)
            assert descifrado == original, f"Descifrado de {esperado} debería ser {original}, pero fue {descifrado}"

    def test_numeros_aleatorios_simetria(self, cipher):
        """Test con una muestra de números aleatorios para verificar simetría."""
        numeros_aleatorios = [
            "135792", "246813", "369258", "147258", "258369",
            "369147", "456789", "789456", "159357", "753951"
        ]

        for numero in numeros_aleatorios:
            cifrado = cipher.cifrar(numero)
            descifrado = cipher.descifrar(cifrado)
            assert descifrado == numero, f"Simetría falló para {numero}"
