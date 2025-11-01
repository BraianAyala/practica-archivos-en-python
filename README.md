Actividad 2

Este proyecto forma parte de la materia Programació y tiene como objetivo practicar la lectura, procesamiento y análisis de archivos CSV en Python.  
El programa analiza registros de entrenamientos de distintos campeones, determina patrones según los días de la semana y genera archivos con estadísticas resumidas en formato CSV y JSON.

 Funcionalidades principales

El programa cumple con los siguientes puntos solicitados en la consigna:

1. **Lectura del archivo CSV** sin cargar todo en memoria.  
2. **Identificación del día de la semana** correspondiente a cada entrenamiento.  
3. **Determinación del/los día/s** con mayor cantidad de sesiones.  
4. **Cálculo de los días transcurridos** entre el primer y último entrenamiento.  
5. **Detección del campeón que más entrenó.**  
6. **Cálculo del promedio diario** de entrenamientos.  
7. **Identificación del campeón que más entrena los fines de semana.**  
8. **Generación automática de una carpeta `/salida`** que contiene:  
   - `entrenamientos_por_campeon.csv`: cantidad total de entrenamientos por campeón.  
   - `resultado.json`: resumen con la cantidad de registros y detalle por día.  

---


- Manipulación de archivos con `csv` y `json`.  
- Manejo de fechas con el módulo `datetime`.  
- Creación de rutas dinámicas con `pathlib.Path`.  
- Uso de **diccionarios anidados** para acumular información.  
- Empleo de **funciones lambda** en la ordenación de datos (`sorted`).  
- Procesamiento de archivos **línea por línea** (sin almacenar todo el contenido en memoria).  

---

# Ejecución del programa

1. Asegurarse de tener instalado **Python 3.10** o superior.
2. Ubicar el archivo `actividad_2.csv` en la misma carpeta que el script `solucion.py`.
3. Ejecutar el programa desde la terminal o un entorno de desarrollo:





