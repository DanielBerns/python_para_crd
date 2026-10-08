# -*- coding: utf-8 -*-
"""
Script Principal - Sistema de Monitoreo y Alerta Agrometeorológica (SMAA)
Este script coordina la lectura de datos, procesamiento científico, detección de alertas
y la generación de reportes gráficos y ejecutivos.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
# Importar funciones del módulo local
from modulos.alertas import calcular_punto_rocio

def ejecutar_pipeline_smaa():
    print("[1/4] Iniciando carga de datos integrados...")
    # Simulación de carga (Los estudiantes usarán los datos de su carpeta datos/entrada)
    ruta_datos = "/content/notebooks_introduccion/datos_basicos.csv"
    if not os.path.exists(ruta_datos):
        print("Error: No se encuentran los datos básicos de entrada.")
        return
    
    df = pd.read_csv(ruta_datos)
    
    print("[2/4] Calculando índices y alertas agrometeorológicas...")
    # Aplicar la función importada para calcular el punto de rocío de manera vectorizada
    # Supongamos una humedad promedio de ejemplo para la serie histórica
    df['punto_rocio'] = df.apply(lambda row: calcular_punto_rocio(row['temperatura_media'], 65), axis=1)
    
    print("[3/4] Generando gráficos de control...")
    plt.figure(figsize=(10, 4))
    plt.plot(df.index, df['temperatura_media'], color='green', label='Temp Media (°C)')
    plt.plot(df.index, df['punto_rocio'], color='purple', linestyle='--', label='Punto de Rocío (°C)')
    plt.title("Evolución Térmica y Punto de Rocío")
    plt.xlabel("Registro diario")
    plt.ylabel("Temperatura / Punto de Rocío")
    plt.legend()
    plt.grid(True, linestyle=':')
    
    # Guardar gráfico en la carpeta correspondiente
    grafico_out = "/content/proyecto_final_smaa/graficos/analisis_temperatura.png"
    plt.savefig(grafico_out, dpi=150)
    plt.close()
    print(f"-> Gráfico exportado a: {grafico_out}")
    
    print("[4/4] Exportando reporte consolidado en Excel...")
    reporte_out = "/content/proyecto_final_smaa/datos/salida/reporte_ejecutivo.xlsx"
    df.to_excel(reporte_out, index=False)
    print(f"-> Reporte de Excel generado en: {reporte_out}")
    print("
¡Procesamiento finalizado con éxito! El sistema está operativo.")

if __name__ == '__main__':
    ejecutar_pipeline_smaa()
