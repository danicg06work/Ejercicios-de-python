# Ejercicios de Python

Repositorio de ejercicios prácticos orientados al aprendizaje, afianzamiento y dominio de la programación en Python. Incluye 50 ejercicios organizados modularmente que cubren desde los fundamentos de sintaxis y aritmética básica hasta estructuras de datos avanzadas.

---

## Tabla de Contenidos

- [Objetivos](#objetivos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Índice de Ejercicios](#índice-de-ejercicios)
  - [Módulo 1: Sintaxis Básica y Aritmética (01-10)](#módulo-1-sintaxis-básica-y-aritmética-01-10)
  - [Módulo 2: Variables, Tipos y Operadores Lógicos (11-20)](#módulo-2-variables-tipos-y-operadores-lógicos-11-20)
  - [Módulo 3: Estructuras Condicionales (21-25)](#módulo-3-estructuras-condicionales-21-25)
  - [Módulo 4: Bucles y Control de Flujo (26-30)](#módulo-4-bucles-y-control-de-flujo-26-30)
  - [Módulo 5: Manipulación de Cadenas de Texto (31-40)](#módulo-5-manipulación-de-cadenas-de-texto-31-40)
  - [Módulo 6: Estructuras de Datos (41-50)](#módulo-6-estructuras-de-datos-41-50)
- [Requisitos e Instalación](#requisitos-e-instalación)
- [Ejecución](#ejecución)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Objetivos

- Afianzar la sintaxis fundamental de Python y el manejo de variables y tipos de datos.
- Aplicar operadores aritméticos, lógicos y relacionales.
- Implementar estructuras de control de flujo (`if`, `elif`, `else`, `while`, `for`).
- Emplear métodos integrados para la manipulación y formateo de cadenas de texto.
- Gestionar colecciones de datos esenciales: listas, tuplas, conjuntos y diccionarios.

---

## Estructura del Proyecto

Los ejercicios están contenidos dentro del directorio `Ej1`, organizados en archivos individuales `.py` correspondientes a cada número de ejercicio:

```text
Ejercicios-de-python/
│
├── Ej1/
│   ├── enunciados.txt       # Listado de enunciados de los ejercicios
│   ├── ejercicio_01.py      # Solución al ejercicio 1
│   ├── ejercicio_02.py      # Solución al ejercicio 2
│   ├── ...
│   └── ejercicio_50.py      # Solución al ejercicio 50
│
└── README.md                # Documentación del repositorio
```

---

## Índice de Ejercicios

### Módulo 1: Sintaxis Básica y Aritmética (01-10)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_01.py` | Programa que imprime "Hola, Mundo" en la consola | `print()` |
| `ejercicio_02.py` | Suma de dos números e impresión del resultado | Operador `+` |
| `ejercicio_03.py` | Diferencia entre dos números | Operador `-` |
| `ejercicio_04.py` | Producto de dos números | Operador `*` |
| `ejercicio_05.py` | Cociente de la división entre dos números | Operador `/` |
| `ejercicio_06.py` | Impresión de un número flotante con dos decimales | Formateo numérico |
| `ejercicio_07.py` | Cálculo de una potencia (2 elevado a 5) | Operador `**` |
| `ejercicio_08.py` | Cálculo del resto de una división (17 módulo 3) | Operador `%` |
| `ejercicio_09.py` | Evaluación con precedencia de operadores (5 + 3 * 2) | Jerarquía de operadores |
| `ejercicio_10.py` | Impresión de línea en blanco y mensaje de finalización | Caracteres de escape (`\n`) |

### Módulo 2: Variables, Tipos y Operadores Lógicos (11-20)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_11.py` | Declaración e inspección de variables (int, float, str) | `type()` |
| `ejercicio_12.py` | Conversión explícita de tipo flotante a entero | Casting (`int()`) |
| `ejercicio_13.py` | Comparación de igualdad entre variables | Operador `==` |
| `ejercicio_14.py` | Comparación de relación mayor que | Operador `>` |
| `ejercicio_15.py` | Inversión booleana mediante negación | Operador `not` |
| `ejercicio_16.py` | Evaluación disyuntiva de condiciones numéricas | Operador `or` |
| `ejercicio_17.py` | Concatenación de cadenas de texto | Operador `+` |
| `ejercicio_18.py` | Cálculo del promedio de tres números | Operaciones compuestas |
| `ejercicio_19.py` | Determinación de paridad de un número | Operador `%` |
| `ejercicio_20.py` | Cálculo del área de un triángulo a partir de datos del usuario | `input()`, operaciones aritméticas |

### Módulo 3: Estructuras Condicionales (21-25)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_21.py` | Clasificación de un número en positivo, negativo o cero | `if`, `elif`, `else` |
| `ejercicio_22.py` | Verificación de mayoría de edad (umbral de 18 años) | Condicionales simples |
| `ejercicio_23.py` | Evaluación de divisibilidad simultánea entre 3 y 5 | Operador `and` |
| `ejercicio_24.py` | Comparación de dos entradas numéricas para obtener la mayor | Control condicional |
| `ejercicio_25.py` | Determinación de divisibilidad entre 2, 3 o ambos | Ramificación condicional |

### Módulo 4: Bucles y Control de Flujo (26-30)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_26.py` | Impresión secuencial del 1 al 10 | Bucle `while` |
| `ejercicio_27.py` | Impresión descendente del 10 al 1 | Bucle `while`, decremento |
| `ejercicio_28.py` | Generación de los primeros 10 números pares | Bucle `for`, `range()` |
| `ejercicio_29.py` | Iteración sobre caracteres de una cadena | Bucle `for`, strings |
| `ejercicio_30.py` | Secuencia numérica del 1 hasta un valor límite ingresado | `input()`, `for` |

### Módulo 5: Manipulación de Cadenas de Texto (31-40)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_31.py` | Cálculo de la longitud de una cadena | `len()` |
| `ejercicio_32.py` | Transformación de texto a minúsculas | `.lower()` |
| `ejercicio_33.py` | Transformación de texto a mayúsculas | `.upper()` |
| `ejercicio_34.py` | Sustitución de subcadenas | `.replace()` |
| `ejercicio_35.py` | Extracción de subcadenas por índice | Slicing |
| `ejercicio_36.py` | Segmentación de texto en lista de palabras | `.split()` |
| `ejercicio_37.py` | Concatenación de elementos de una lista con delimitador | `.join()` |
| `ejercicio_38.py` | Verificación de existencia de subcadena | Operador `in` |
| `ejercicio_39.py` | Conteo de frecuencia de un carácter | `.count()` |
| `ejercicio_40.py` | Eliminación de espacios en blanco al inicio y al final | `.strip()` |

### Módulo 6: Estructuras de Datos (41-50)

| Archivo | Descripción | Conceptos clave |
|:---|:---|:---|
| `ejercicio_41.py` | Definición e impresión de listas numéricas | Listas |
| `ejercicio_42.py` | Inserción de elementos en una lista vacía | `.append()` |
| `ejercicio_43.py` | Acceso a elementos por índice posicional | Indexación |
| `ejercicio_44.py` | Modificación de valores por índice | Mutabilidad |
| `ejercicio_45.py` | Extracción y borrado del último elemento de una lista | `.pop()` |
| `ejercicio_46.py` | Definición de tuplas y acceso a elementos | Tuplas |
| `ejercicio_47.py` | Frecuencia de elementos dentro de una tupla | `.count()` |
| `ejercicio_48.py` | Definición de conjuntos y adición de elementos | Conjuntos (`set`), `.add()` |
| `ejercicio_49.py` | Operación de intersección entre conjuntos | `.intersection()` |
| `ejercicio_50.py` | Definición de diccionarios y consulta por clave | Diccionarios (`dict`) |

---

## Requisitos e Instalación

### Requisitos

- Python 3.8 o superior.
- Git (opcional).

Comprobar la versión instalada:
```bash
python3 --version
```

### Clonar el Repositorio

```bash
git clone https://github.com/danicg06work/Ejercicios-de-python.git
cd Ejercicios-de-python
```

---

## Ejecución

Los ejercicios pueden ejecutarse de forma independiente desde la terminal.

Accediendo al directorio de los ejercicios:
```bash
cd Ej1
python3 ejercicio_01.py
```

O directamente desde la raíz del repositorio:
```bash
python3 Ej1/ejercicio_01.py
```

---

## Autor

- Dani CG ([@danicg06work](https://github.com/danicg06work))

---

## Licencia

Este proyecto se distribuye bajo los términos de la Licencia MIT.