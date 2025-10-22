quit# Aplicación de Cifrado y Descifrado

Aplicación de escritorio desarrollada en Python con PyQt6 para cifrar y descifrar números de 6 dígitos usando un algoritmo personalizado.

## 📋 Información del Proyecto

- **Autor:** Orlando Duque Cantor
- **Cédula:** 80171794
- **Correo:** oduque94@unisalle.edu.co
- **Asignatura:** Aplicaciones I
- **Universidad:** Universidad de La Salle

## 🎯 Descripción

Esta aplicación permite cifrar y descifrar números enteros de 6 dígitos mediante un algoritmo que:
1. Suma 7 a cada dígito y obtiene el residuo de la división entre 10
2. Intercambia posiciones específicas: 1º↔3º, 2º↔4º, 5º↔6º

El proceso de descifrado invierte estas operaciones para recuperar el número original.

## 🏗️ Estructura del Proyecto

```
Actividad3Aplicaciones1/
├── main.py                          # Punto de entrada de la aplicación
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
├── .venv/                          # Entorno virtual de Python (local)
├── .idea/                          # Configuración de PyCharm
│   └── runConfigurations/
│       └── main.xml                # Configuración de ejecución
└── src/
    ├── __init__.py
    ├── logic/                       # Lógica de negocio
    │   ├── __init__.py
    │   └── cipher.py               # Algoritmos de cifrado/descifrado
    ├── ui/                         # Interfaz de usuario
    │   ├── __init__.py
    │   ├── app_window.py           # Ventana principal con navegación
    │   ├── ventana_principal.py    # Pantalla de bienvenida
    │   ├── ventana_cifrado.py      # Pantalla de cifrado
    │   └── ventana_descifrado.py   # Pantalla de descifrado
    └── utils/                      # Utilidades
        ├── __init__.py
        └── validators.py           # Validaciones de entrada
```

## 🔧 Requisitos

- **Python:** 3.8 o superior
- **PyQt6:** 6.6.1
- **Sistema Operativo:** Windows, macOS, o Linux

## 📦 Instalación

### 1. Clonar o descargar el proyecto

```bash
cd Actividad3Aplicaciones1
```

### 2. Crear y activar el entorno virtual

**En Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

### Desde la línea de comandos

```bash
python main.py
```

### Desde PyCharm

1. Abrir el proyecto en PyCharm
2. Seleccionar la configuración "main" en el dropdown superior
3. Hacer clic en el botón Run (▶️) o presionar `Shift + F10`

### Modo Debug en PyCharm

1. Agregar breakpoints haciendo clic en el margen izquierdo del código
2. Hacer clic en el botón Debug (🐛) o presionar `Shift + F9`
3. La aplicación se detendrá en los breakpoints para inspección

## 📖 Uso de la Aplicación

### Pantalla Principal
- Muestra información del autor
- Botones para navegar a las funciones de cifrado y descifrado

### Cifrado
1. Ingresar un número de exactamente 6 dígitos
2. Hacer clic en "Cifrar"
3. El número cifrado se muestra en el campo de resultado

**Ejemplo:**
- Entrada: `123456`
- Salida: `018932`

### Descifrado
1. Ingresar el número cifrado de 6 dígitos
2. Hacer clic en "Descifrar"
3. El número original se muestra en el campo de resultado

**Ejemplo:**
- Entrada: `018932`
- Salida: `123456`

## 🔐 Algoritmo de Cifrado

### Proceso de Cifrado

```python
# Ejemplo: 123456
# Paso 1: Sumar 7 a cada dígito (mod 10)
1+7=8, 2+7=9, 3+7=0, 4+7=1, 5+7=2, 6+7=3
# Resultado: [8, 9, 0, 1, 2, 3]

# Paso 2: Intercambiar posiciones
# 1º↔3º: [8,9,0,1,2,3] → [0,9,8,1,2,3]
# 2º↔4º: [0,9,8,1,2,3] → [0,1,8,9,2,3]
# 5º↔6º: [0,1,8,9,2,3] → [0,1,8,9,3,2]
# Resultado final: 018932
```

### Proceso de Descifrado

```python
# Ejemplo: 018932
# Paso 1: Invertir intercambios
# 1º↔3º: [0,1,8,9,3,2] → [8,1,0,9,3,2]
# 2º↔4º: [8,1,0,9,3,2] → [8,9,0,1,3,2]
# 5º↔6º: [8,9,0,1,3,2] → [8,9,0,1,2,3]
# Resultado: [8, 9, 0, 1, 2, 3]

# Paso 2: Restar 7 a cada dígito (mod 10)
8-7=1, 9-7=2, 0-7=-7→3, 1-7=-6→4, 2-7=-5→5, 3-7=-4→6
# Resultado final: 123456
```

## 🧪 Validaciones

La aplicación valida:
- ✓ Campo no vacío
- ✓ Exactamente 6 dígitos
- ✓ Solo caracteres numéricos (0-9)

## 🏛️ Arquitectura

### Separación de Responsabilidades

- **`src/logic/`**: Lógica de negocio independiente de la UI
  - `cipher.py`: Algoritmos de cifrado y descifrado

- **`src/ui/`**: Componentes de interfaz gráfica
  - `app_window.py`: Controlador principal y navegación
  - `ventana_*.py`: Vistas individuales

- **`src/utils/`**: Funciones auxiliares reutilizables
  - `validators.py`: Validaciones de entrada

### Principios Aplicados

- **Single Responsibility Principle**: Cada módulo tiene una responsabilidad única
- **Separation of Concerns**: UI separada de la lógica de negocio
- **DRY (Don't Repeat Yourself)**: Código reutilizable en módulos compartidos
- **Modularidad**: Componentes independientes y desacoplados

## 🧪 Tests Unitarios

El proyecto incluye una suite completa de tests unitarios con **56 tests** y **100% de cobertura** en la lógica de negocio.

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con reporte de cobertura
pytest --cov=src --cov-report=term-missing

# Ejecutar solo tests de cifrado
pytest tests/test_cipher.py -v

# Ejecutar solo tests de validadores
pytest tests/test_validators.py -v
```

### Desde PyCharm

1. Seleccionar la configuración "Tests" en el dropdown superior
2. Hacer clic en Run (▶️) para ejecutar todos los tests
3. Ver resultados y cobertura en la ventana de tests

### Cobertura de Tests

- **`test_cipher.py`**: 23 tests
  - Tests de cifrado básico
  - Tests de descifrado
  - Tests de simetría (cifrar/descifrar)
  - Tests de casos límite
  - Tests de algoritmo

- **`test_validators.py`**: 33 tests
  - Tests de validación exitosa
  - Tests de entradas inválidas
  - Tests de longitud incorrecta
  - Tests de caracteres especiales
  - Tests de valores límite
  - Tests de consistencia

### Estructura de Tests

```
tests/
├── __init__.py
├── conftest.py              # Configuración de pytest
├── test_cipher.py           # Tests de lógica de cifrado
└── test_validators.py       # Tests de validadores
```

## 🐛 Debug y Desarrollo

### Puntos de Interrupción Recomendados

Para entender el flujo de la aplicación, coloca breakpoints en:

1. **`src/logic/cipher.py:34`** - Proceso de cifrado
2. **`src/logic/cipher.py:63`** - Proceso de descifrado
3. **`src/ui/ventana_cifrado.py:76`** - Validación de entrada (cifrado)
4. **`src/ui/ventana_descifrado.py:85`** - Validación de entrada (descifrado)

### Variables de Interés

- `digitos_cifrados`: Lista con dígitos tras sumar 7
- `digitos_intercambiados`: Lista con posiciones intercambiadas
- `numero_cifrado`/`numero_original`: Resultado final

## 📝 Notas Técnicas

- **Framework GUI:** PyQt6 (Qt 6.x)
- **Patrón de Diseño:** MVC (Model-View-Controller) simplificado
- **Gestión de Estado:** Callback-based navigation
- **Python Version Target:** 3.8+

## 🔄 Extensiones Futuras

Posibles mejoras para el proyecto:

- [ ] Soporte para números de longitud variable
- [ ] Algoritmos de cifrado adicionales (César, Vigenère, etc.)
- [x] Tests unitarios con pytest
- [ ] Tests de interfaz con pytest-qt

## 📄 Licencia

Proyecto académico desarrollado para la asignatura Aplicaciones I de la Universidad de La Salle.

## 📞 Contacto

Orlando Duque Cantor - oduque94@unisalle.edu.co

---

**Universidad de La Salle** | Aplicaciones I | 2025haz
