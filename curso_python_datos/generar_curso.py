import os
import json
import uuid

base_dir = '/home/dberns/Projects/github/DanielBerns/san_luis/python_para_crd/curso_python_datos'
notebooks_dir = os.path.join(base_dir, 'notebooks')

os.makedirs(notebooks_dir, exist_ok=True)

# -----------------
# CONTENIDO DE SESIONES
# -----------------

sesiones = [
    {
        "id": "01",
        "title": "Introducción a Colab, Jupyter y Python Básico",
        "md_content": """# Sesión 1: Introducción a Colab, Jupyter y Python Básico

## Objetivos
- Familiarizarse con el entorno de trabajo (Jupyter Notebooks / Colab).
- Entender el concepto de celdas de código y texto (Markdown).
- Aprender la sintaxis básica de Python: variables, tipos de datos y operadores.

## ¿Qué es Python?
Python es un lenguaje de programación interpretado, de alto nivel y con una sintaxis muy legible. Es muy popular en Ciencias de la Atmósfera para análisis de datos meteorológicos.

## Entorno de Trabajo
Los Notebooks nos permiten intercalar texto explicativo con código ejecutable. 
- **Colab**: Es un servicio de Google que permite ejecutar notebooks en la nube.
- **Jupyter**: Es el entorno local equivalente.

Ve a la carpeta `notebooks/` y abre `01_introduccion.ipynb` para comenzar con la práctica interactiva.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 1: Introducción a Python\n", "En esta sesión aprenderemos a definir variables y usar operadores."]},
            {"cell_type": "code", "source": ["# Ejecuta esta celda presionando Shift + Enter\n", "print('¡Hola, mundo meteorológico!')"]},
            {"cell_type": "markdown", "source": ["## Variables y Tipos de Datos\n", "Podemos almacenar datos (como temperaturas, presiones, nombres de estaciones) en variables."]},
            {"cell_type": "code", "source": ["temperatura = 23.5 # Float (número real)\n", "estacion = 'Aeroparque' # String (cadena de texto)\n", "lluvia = True # Booleano (Verdadero o Falso)\n", "print(f'Estación {estacion}: Temperatura={temperatura}C, Lluvia={lluvia}')"]},
            {"cell_type": "markdown", "source": ["## Operadores Matemáticos"]},
            {"cell_type": "code", "source": ["t_min = 15.2\n", "t_max = 28.4\n", "amplitud_termica = t_max - t_min\n", "print('Amplitud Térmica:', amplitud_termica)"]}
        ]
    },
    {
        "id": "02",
        "title": "Estructuras de Datos y Control de Flujo",
        "md_content": """# Sesión 2: Estructuras de Datos y Control de Flujo

## Objetivos
- Aprender a agrupar datos usando listas, tuplas y diccionarios.
- Aprender a controlar el flujo del programa con condicionales (`if`) y bucles (`for`, `while`).

## Estructuras de Datos
- **Listas**: Colecciones ordenadas y mutables. Ej: `[15.5, 16.2, 17.0]`
- **Diccionarios**: Colecciones de pares clave-valor. Ej: `{'Aeroparque': 23.5, 'Ezeiza': 22.1}`

Ve a la carpeta `notebooks/` y abre `02_estructuras_control.ipynb` para continuar.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 2: Estructuras y Control de Flujo"]},
            {"cell_type": "code", "source": ["# Listas de temperaturas\n", "temps = [12.5, 13.0, 14.2, 11.8]\n", "temps.append(15.1)\n", "print('Temperaturas:', temps)"]},
            {"cell_type": "code", "source": ["# Diccionarios (muy útiles para datos estructurados)\n", "clima = {'estacion': 'Ezeiza', 'temp_max': 25, 'temp_min': 15}\n", "print('Estación:', clima['estacion'])"]},
            {"cell_type": "markdown", "source": ["## Condicionales (if / else)"]},
            {"cell_type": "code", "source": ["temp = 32\n", "if temp > 30:\n", "    print('Alerta de calor')\n", "elif temp < 5:\n", "    print('Alerta de helada')\n", "else:\n", "    print('Temperatura normal')"]},
            {"cell_type": "markdown", "source": ["## Bucles (for)"]},
            {"cell_type": "code", "source": ["# Calcular el promedio de una lista\n", "suma = 0\n", "for t in temps:\n", "    suma += t\n", "promedio = suma / len(temps)\n", "print('Temperatura promedio:', promedio)"]}
        ]
    },
    {
        "id": "03",
        "title": "Funciones y Clases",
        "md_content": """# Sesión 3: Funciones y Clases

## Objetivos
- Crear funciones para reutilizar código.
- Entender los conceptos básicos de la Programación Orientada a Objetos (POO) y cómo se aplica al análisis de datos (ej. un DataFrame es un objeto de una clase).

Ve a la carpeta `notebooks/` y abre `03_funciones_clases.ipynb` para la práctica.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 3: Funciones y Clases"]},
            {"cell_type": "markdown", "source": ["## Funciones\n", "Las funciones agrupan código que podemos llamar múltiples veces."]},
            {"cell_type": "code", "source": ["def celsius_a_fahrenheit(c):\n", "    return (c * 9/5) + 32\n\n", "print('20°C en F:', celsius_a_fahrenheit(20))"]},
            {"cell_type": "markdown", "source": ["## Clases y Objetos\n", "Una clase es un 'molde' para crear objetos. Librerías como Pandas usan clases constantemente."]},
            {"cell_type": "code", "source": ["class EstacionMeteorologica:\n", "    def __init__(self, nombre, lat, lon):\n", "        self.nombre = nombre\n", "        self.lat = lat\n", "        self.lon = lon\n", "        self.mediciones = []\n\n", "    def agregar_medicion(self, temp):\n", "        self.mediciones.append(temp)\n\n", "    def promedio(self):\n", "        return sum(self.mediciones) / len(self.mediciones) if self.mediciones else 0\n"]},
            {"cell_type": "code", "source": ["est_eze = EstacionMeteorologica('Ezeiza', -34.82, -58.53)\n", "est_eze.agregar_medicion(20)\n", "est_eze.agregar_medicion(22)\n", "print(f'Promedio de {est_eze.nombre}: {est_eze.promedio()}')"]}
        ]
    },
    {
        "id": "04",
        "title": "Introducción a Numpy",
        "md_content": """# Sesión 4: Introducción a Numpy

## Objetivos
- Comprender qué es NumPy y por qué es más rápido que las listas estándar de Python.
- Crear y manipular arreglos (arrays) n-dimensionales.
- Realizar operaciones matemáticas sobre grandes volúmenes de datos meteorológicos.

Ve a la carpeta `notebooks/` y abre `04_numpy.ipynb`.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 4: Introducción a NumPy\n", "NumPy (Numerical Python) es la librería base para cálculos científicos en Python."]},
            {"cell_type": "code", "source": ["import numpy as np"]},
            {"cell_type": "markdown", "source": ["## Arreglos (Arrays)"]},
            {"cell_type": "code", "source": ["# Crear un arreglo a partir de una lista\n", "temps_lista = [15.5, 16.2, 17.0, 14.8]\n", "temps_array = np.array(temps_lista)\n", "print(temps_array)\n", "print('Tipo:', type(temps_array))"]},
            {"cell_type": "code", "source": ["# Operaciones vectorizadas (mucho más rápido que un for)\n", "temps_kelvin = temps_array + 273.15\n", "print('En Kelvin:', temps_kelvin)"]},
            {"cell_type": "markdown", "source": ["## Estadísticas básicas"]},
            {"cell_type": "code", "source": ["print('Media:', np.mean(temps_array))\n", "print('Máxima:', np.max(temps_array))\n", "print('Desvío estándar:', np.std(temps_array))"]},
            {"cell_type": "code", "source": ["# Manejo de valores faltantes (NaN)\n", "temps_con_nan = np.array([15.5, np.nan, 17.0])\n", "print('Media ignorando NaN:', np.nanmean(temps_con_nan))"]}
        ]
    },
    {
        "id": "05",
        "title": "Introducción a Pandas",
        "md_content": """# Sesión 5: Introducción a Pandas

## Objetivos
- Aprender qué es Pandas y cómo se basa en Numpy.
- Trabajar con `Series` y `DataFrames`.
- Importar datos tabulares básicos desde un archivo CSV.

Ve a la carpeta `notebooks/` y abre `05_pandas.ipynb`.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 5: Introducción a Pandas\n", "Pandas proporciona estructuras de datos (Series y DataFrames) de alto nivel y muy eficientes."]},
            {"cell_type": "code", "source": ["import pandas as pd\n", "import numpy as np"]},
            {"cell_type": "markdown", "source": ["## Series (1D) y DataFrames (2D)"]},
            {"cell_type": "code", "source": ["# DataFrame desde un diccionario\n", "datos = {\n", "    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03'],\n", "    'Temperatura': [25.5, 26.1, 24.8],\n", "    'Lluvia': [0, 5.2, 0]\n", "}\n", "df = pd.DataFrame(datos)\n", "display(df)"]},
            {"cell_type": "markdown", "source": ["## Lectura de CSV"]},
            {"cell_type": "code", "source": ["# Leemos un archivo generado previamente\n", "df_basico = pd.read_csv('datos/datos_basicos.csv')\n", "display(df_basico.head())"]},
            {"cell_type": "markdown", "source": ["## Exploración básica"]},
            {"cell_type": "code", "source": ["df_basico.info()"]},
            {"cell_type": "code", "source": ["df_basico.describe()"]}
        ]
    },
    {
        "id": "06",
        "title": "Procesamiento de archivos Excel con Pandas",
        "md_content": """# Sesión 6: Procesamiento de archivos Excel con Pandas

## Objetivos
- Importar y exportar archivos de Excel (`.xlsx`).
- Realizar limpieza de datos meteorológicos (lidiar con valores faltantes y outliers).
- Filtrar y agrupar información usando `groupby`.

Ve a la carpeta `notebooks/` y abre `06_pandas_excel.ipynb`.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 6: Archivos Excel y Limpieza de Datos"]},
            {"cell_type": "code", "source": ["import pandas as pd\n", "import numpy as np"]},
            {"cell_type": "markdown", "source": ["## Leer Excel"]},
            {"cell_type": "code", "source": ["# Leemos el registro completo\n", "df_meteo = pd.read_excel('datos/registro_meteorologico.xlsx')\n", "display(df_meteo.head())"]},
            {"cell_type": "markdown", "source": ["## Limpieza de Datos\n", "En meteorología es muy común tener datos erróneos por falla de sensores."]},
            {"cell_type": "code", "source": ["# Detectar NaN en temperatura máxima\n", "faltantes = df_meteo['Temperatura_Max'].isna().sum()\n", "print(f'Faltantes en Temp Max: {faltantes}')"]},
            {"cell_type": "code", "source": ["# Detectar humedad errónea (ej: -999)\n", "errores_humedad = len(df_meteo[df_meteo['Humedad_Relativa'] < 0])\n", "print(f'Errores en Humedad (-999): {errores_humedad}')"]},
            {"cell_type": "code", "source": ["# Limpiar: reemplazar -999 con NaN y luego imputar o borrar\n", "df_limpio = df_meteo.copy()\n", "df_limpio.loc[df_limpio['Humedad_Relativa'] < 0, 'Humedad_Relativa'] = np.nan\n", "# Borramos las filas que contengan NaN para simplificar\n", "df_limpio = df_limpio.dropna()\n", "print('Datos originales:', len(df_meteo), 'Datos limpios:', len(df_limpio))"]},
            {"cell_type": "markdown", "source": ["## Agrupación (Groupby)"]},
            {"cell_type": "code", "source": ["# Promedio de variables por estación\n", "promedios = df_limpio.groupby('Estacion')[['Temperatura_Max', 'Temperatura_Min', 'Humedad_Relativa']].mean()\n", "display(promedios)"]}
        ]
    },
    {
        "id": "07",
        "title": "Bases de datos con SQLite y Python",
        "md_content": """# Sesión 7: Bases de datos con SQLite y Python

## Objetivos
- Entender qué es una base de datos relacional y SQLite.
- Conectarse a SQLite desde Python usando la librería `sqlite3`.
- Ejecutar consultas SQL y leer resultados directamente como DataFrames de Pandas.

Ve a la carpeta `notebooks/` y abre `07_sqlite_pandas.ipynb`.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 7: SQLite y Pandas"]},
            {"cell_type": "code", "source": ["import sqlite3\n", "import pandas as pd"]},
            {"cell_type": "markdown", "source": ["## Conectar a la base de datos"]},
            {"cell_type": "code", "source": ["# Creamos la conexión al archivo .sqlite\n", "conn = sqlite3.connect('datos/estaciones_meteo.sqlite')"]},
            {"cell_type": "markdown", "source": ["## Consultas SQL Directas (sqlite3)"]},
            {"cell_type": "code", "source": ["cursor = conn.cursor()\n", "cursor.execute('SELECT * FROM info_estaciones')\n", "estaciones = cursor.fetchall()\n", "for est in estaciones:\n", "    print(est)"]},
            {"cell_type": "markdown", "source": ["## Integración con Pandas (Recomendado)"]},
            {"cell_type": "code", "source": ["# Leer tabla de mediciones directamente a un DataFrame\n", "df_sql = pd.read_sql_query('SELECT * FROM mediciones LIMIT 10', conn)\n", "display(df_sql)"]},
            {"cell_type": "code", "source": ["# Hacer un JOIN complejo usando SQL y traerlo a Pandas\n", "query = '''\n", "SELECT m.Fecha, e.nombre, m.Temperatura_Max, m.Precipitacion_mm\n", "FROM mediciones m\n", "JOIN info_estaciones e ON m.id_estacion = e.id_estacion\n", "WHERE m.Temperatura_Max > 30\n", "'''\n", "df_dias_calurosos = pd.read_sql_query(query, conn)\n", "display(df_dias_calurosos.head())"]},
            {"cell_type": "code", "source": ["# Cerrar conexión\n", "conn.close()"]}
        ]
    },
    {
        "id": "08",
        "title": "Visualización de Datos",
        "md_content": """# Sesión 8: Visualización de Datos

## Objetivos
- Utilizar Matplotlib para crear gráficos simples.
- Aprovechar las capacidades gráficas integradas de Pandas (que usan Matplotlib por debajo) para visualizar series temporales meteorológicas.

Ve a la carpeta `notebooks/` y abre `08_visualizacion.ipynb`.
""",
        "notebook_cells": [
            {"cell_type": "markdown", "source": ["# Sesión 8: Visualización de Datos\n", "En meteorología es fundamental graficar las series temporales."]},
            {"cell_type": "code", "source": ["import pandas as pd\n", "import matplotlib.pyplot as plt\n\n", "# Configuración para ver gráficos dentro del notebook\n", "%matplotlib inline"]},
            {"cell_type": "markdown", "source": ["## Cargar Datos Limpios"]},
            {"cell_type": "code", "source": ["# Volvemos a leer y limpiar rápidamente\n", "df_meteo = pd.read_excel('datos/registro_meteorologico.xlsx')\n", "df_meteo = df_meteo[df_meteo['Humedad_Relativa'] >= 0]\n", "df_meteo = df_meteo.dropna()\n", "df_meteo['Fecha'] = pd.to_datetime(df_meteo['Fecha'])"]},
            {"cell_type": "markdown", "source": ["## Filtrar para una estación y fijar índice"]},
            {"cell_type": "code", "source": ["df_aero = df_meteo[df_meteo['Estacion'] == 'Estacion_A_Aeroparque'].copy()\n", "df_aero.set_index('Fecha', inplace=True)\n", "display(df_aero.head())"]},
            {"cell_type": "markdown", "source": ["## Gráficos usando Pandas/Matplotlib"]},
            {"cell_type": "code", "source": ["# Plot simple de Temperatura Máxima (Serie temporal)\n", "plt.figure(figsize=(12, 5))\n", "df_aero['Temperatura_Max'].plot(color='red', title='Temperatura Máxima en Aeroparque (2023)')\n", "plt.ylabel('Temperatura (°C)')\n", "plt.grid(True)\n", "plt.show()"]},
            {"cell_type": "code", "source": ["# Histograma de humedad\n", "plt.figure(figsize=(8, 5))\n", "df_aero['Humedad_Relativa'].plot(kind='hist', bins=20, color='blue', alpha=0.7)\n", "plt.title('Distribución de la Humedad Relativa')\n", "plt.xlabel('Humedad (%)')\n", "plt.show()"]},
            {"cell_type": "code", "source": ["# Scatter plot (Dispersión): T_Max vs Humedad\n", "df_aero.plot.scatter(x='Temperatura_Max', y='Humedad_Relativa', figsize=(8,5), alpha=0.5)\n", "plt.title('Relación entre T. Máxima y Humedad')\n", "plt.show()"]}
        ]
    }
]

# Crear un notebook template básico
def create_notebook(cells):
    # Colab requiere que cada celda tenga un ID único (nbformat >= 4.5)
    for cell in cells:
        if 'id' not in cell:
            cell['id'] = str(uuid.uuid4())[:8]

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

# Generar archivos
nombres_notebooks = [
    "01_introduccion.ipynb",
    "02_estructuras_control.ipynb",
    "03_funciones_clases.ipynb",
    "04_numpy.ipynb",
    "05_pandas.ipynb",
    "06_pandas_excel.ipynb",
    "07_sqlite_pandas.ipynb",
    "08_visualizacion.ipynb"
]

for i, sesion in enumerate(sesiones):
    # Escribir archivo MD
    md_filename = os.path.join(base_dir, f"sesion_{sesion['id']}.md")
    with open(md_filename, 'w', encoding='utf-8') as f:
        f.write(sesion["md_content"])
    print(f"Creado {md_filename}")
    
    # Escribir archivo IPYNB
    nb_filename = os.path.join(notebooks_dir, nombres_notebooks[i])
    nb_data = create_notebook(sesion["notebook_cells"])
    with open(nb_filename, 'w', encoding='utf-8') as f:
        json.dump(nb_data, f, indent=1, ensure_ascii=False)
    print(f"Creado {nb_filename}")

print("¡Generación de sesiones completada!")
