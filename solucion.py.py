from pathlib import Path
from datetime import datetime
import csv
import json
import os

 
# Configuracion de rutas
 
BASE = Path(__file__).parent if "__file__" in globals() else Path(".")
ARCHIVO_CSV = BASE / "actividad_2.csv"
CARPETA_SALIDA = BASE / "salida"
ARCHIVO_JSON = CARPETA_SALIDA / "resultado.json"
ARCHIVO_SALIDA_CSV = CARPETA_SALIDA / "entrenamientos_por_campeon.csv"

# Crear carpeta "salida" si no existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

 
# Inicializacion de estructuras de conteo
 
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
conteo_por_dia = {dia: 0 for dia in dias_semana}
conteo_por_campeon = {}
dias_campeon = {dia: {} for dia in dias_semana}

fecha_min = None
fecha_max = None
total_registros = 0

 
# Lectura del archivo CSV linea por linea 
 
with open(ARCHIVO_CSV, "r", encoding="utf-8", newline="") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)  # Salta el encabezado

    for fila in lector:
        if not fila:
            continue  # evita lineas vacias
        try:
            fecha_str = fila[0].split()[0]  # Toma solo la fecha (sin la hora)
            campeon = fila[1].strip()
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        except Exception:
            continue  # ignora filas con formato incorrecto

        dia = dias_semana[fecha.weekday()]
        conteo_por_dia[dia] += 1
        total_registros += 1

        # Conteo por campeon
        conteo_por_campeon[campeon] = conteo_por_campeon.get(campeon, 0) + 1

        # Conteo por día y campeon
        dias_campeon[dia][campeon] = dias_campeon[dia].get(campeon, 0) + 1

        # Actualiza fechas minima y maxima
        if fecha_min is None or fecha < fecha_min:
            fecha_min = fecha
        if fecha_max is None or fecha > fecha_max:
            fecha_max = fecha

 
# Procesamiento de resultados
 
if total_registros > 0:
    dias_totales = (fecha_max - fecha_min).days + 1
    promedio_diario = total_registros / dias_totales

    # Dia o dias con mas sesiones
    max_sesiones = max(conteo_por_dia.values())
    dias_mas_sesiones = [d for d, c in conteo_por_dia.items() if c == max_sesiones]

    # Campeon que mas entreno
    campeon_mas_activo = max(conteo_por_campeon, key=conteo_por_campeon.get)

    # Campeon que mas entrena fines de semana
    conteo_finde = {}
    for dia in ["Sabado", "Domingo"]:
        for campeon, cant in dias_campeon[dia].items():
            conteo_finde[campeon] = conteo_finde.get(campeon, 0) + cant
    campeon_finde = max(conteo_finde, key=conteo_finde.get) if conteo_finde else None

     
    # Resultados por pantalla
     
    print(f"Fechas: {fecha_min.date()} a {fecha_max.date()} ({dias_totales} dias)")
    print(f"Promedio de entrenamientos por dia: {promedio_diario:.2f}")
    print(f"Dia(s) con mas sesiones: {', '.join(dias_mas_sesiones)} ({max_sesiones} sesiones)")
    print(f"Campeon que mas entreno: {campeon_mas_activo}")
    print(f"Campeon que mas entrena fines de semana: {campeon_finde or 'N/A'}")
    print("\nEntrenamientos por dia de la semana:")
    for d, c in conteo_por_dia.items():
        print(f"  {d}: {c}")

     
    # Guardar CSV con conteo por campeon 
     
    campeones_ordenados = sorted(conteo_por_campeon.items(), key=lambda x: x[1], reverse=True)
    with open(ARCHIVO_SALIDA_CSV, "w", newline="", encoding="utf-8") as salida_csv:
        writer = csv.writer(salida_csv)
        writer.writerow(["Campeon", "Cantidad_entrenamientos"])
        writer.writerows(campeones_ordenados)

     
    # Guardar JSON con resumen
     
    salida_json = {
        "total_registros": total_registros,
        "dias": dias_campeon
    }

    with open(ARCHIVO_JSON, "w", encoding="utf-8") as fjson:
        json.dump(salida_json, fjson, ensure_ascii=False, indent=4)

    print(f"\nArchivos generados en carpeta: {CARPETA_SALIDA}")

else:
    print("No se encontraron registros válidos en el archivo.")
