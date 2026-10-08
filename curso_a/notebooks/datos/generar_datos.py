import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import random
import os

# Asegurar directorio de datos
base_dir = os.path.dirname(os.path.abspath(__file__))
print("Generando datos en:", base_dir)

np.random.seed(42)

# --- Generar Excel de Registro Meteorológico (con errores para limpieza) ---
fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
estaciones = ['Estacion_A_Aeroparque', 'Estacion_B_Ezeiza', 'Estacion_C_San_Fernando']

datos = []
for fecha in fechas:
    for estacion in estaciones:
        temp_max = np.random.normal(loc=20, scale=8)
        temp_min = temp_max - np.random.uniform(5, 12)
        precip = np.random.exponential(scale=2) if np.random.rand() > 0.7 else 0.0
        humedad = np.random.normal(loc=60, scale=15)
        
        # Introducir algunos errores para que los alumnos limpien con pandas
        if np.random.rand() < 0.05:
            temp_max = np.nan # Null value
        if np.random.rand() < 0.03:
            temp_min = temp_min * 10 # Outlier
        if np.random.rand() < 0.02:
            humedad = -999 # Código de error común
        
        datos.append([fecha, estacion, temp_max, temp_min, precip, humedad])

df_clima = pd.DataFrame(datos, columns=['Fecha', 'Estacion', 'Temperatura_Max', 'Temperatura_Min', 'Precipitacion_mm', 'Humedad_Relativa'])

# Guardar a Excel
excel_path = os.path.join(base_dir, 'registro_meteorologico.xlsx')
df_clima.to_excel(excel_path, index=False)
print(f"Excel generado: {excel_path}")

# Guardar una versión CSV simple para la sesión 5
csv_path = os.path.join(base_dir, 'datos_basicos.csv')
df_clima[df_clima['Estacion'] == 'Estacion_A_Aeroparque'].to_csv(csv_path, index=False)
print(f"CSV generado: {csv_path}")

# --- Generar base de datos SQLite de Estaciones ---
sqlite_path = os.path.join(base_dir, 'estaciones_meteo.sqlite')
conn = sqlite3.connect(sqlite_path)
cursor = conn.cursor()

# Tabla de metadatos de estaciones
cursor.execute('''
CREATE TABLE IF NOT EXISTS info_estaciones (
    id_estacion INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    latitud REAL,
    longitud REAL,
    altitud_m REAL
)
''')

estaciones_info = [
    ('Estacion_A_Aeroparque', -34.558, -58.416, 5.0),
    ('Estacion_B_Ezeiza', -34.822, -58.535, 20.0),
    ('Estacion_C_San_Fernando', -34.453, -58.589, 3.0)
]
cursor.executemany('INSERT INTO info_estaciones (nombre, latitud, longitud, altitud_m) VALUES (?, ?, ?, ?)', estaciones_info)

# Tabla de mediciones (para simular joins)
# Usaremos datos limpios aquí para simplificar SQL
df_clima_limpio = df_clima.dropna()
df_clima_limpio = df_clima_limpio[df_clima_limpio['Humedad_Relativa'] >= 0]
# Formatear la fecha como string para SQLite
df_clima_limpio['Fecha'] = df_clima_limpio['Fecha'].dt.strftime('%Y-%m-%d')
# Map station names to IDs
estacion_id_map = {nombre: id_est for id_est, nombre, _, _, _ in cursor.execute('SELECT * FROM info_estaciones')}
df_clima_limpio['id_estacion'] = df_clima_limpio['Estacion'].map(estacion_id_map)

# Solo guardar algunas columnas
df_sql = df_clima_limpio[['Fecha', 'id_estacion', 'Temperatura_Max', 'Precipitacion_mm']]
df_sql.to_sql('mediciones', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print(f"SQLite generado: {sqlite_path}")
print("Generación de datos finalizada con éxito.")
