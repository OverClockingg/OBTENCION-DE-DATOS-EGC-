import wfdb
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.signal import find_peaks

# 1. Cargar los datos
record = wfdb.rdrecord('s0010_re')
data = record.p_signal[:, 0]
fs = record.fs

# --- LISTAS PARA GUARDAR EL HISTORIAL DE PICOS ---
todos_los_picos_x = []
todos_los_picos_y = []

# 2. Configurar la figura
fig, ax = plt.subplots(figsize=(12, 5))
line, = ax.plot([], [], lw=1.5, color='blue', label='Señal ECG')
peaks_dots, = ax.plot([], [], 'ro', label='Picos R detectados')

ancho_ventana = 2000 
ax.set_ylim(np.min(data) - 0.2, np.max(data) + 0.2)
ax.set_title("Simulación ECG - Picos Persistentes")
ax.set_xlabel("Número de Muestra")
ax.set_ylabel("Voltaje (mV)")
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# 3. Función de actualización
def update(frame):
    end = frame
    start = max(0, end - ancho_ventana)
    
    # Datos de la ventana actual
    x_ventana = np.arange(start, end)
    y_ventana = data[start:end]
    
    # Buscamos picos solo en los NUEVOS datos que entran (los últimos 20)
    # Esto es más eficiente que buscar en toda la señal cada vez
    segmento_nuevo = data[max(0, end-20):end]
    indices_nuevos, _ = find_peaks(segmento_nuevo, height=0.5)
    
    for idx in indices_nuevos:
        idx_global = (end - 20) + idx
        # Evitamos duplicados si el salto de frames es pequeño
        if idx_global not in todos_los_picos_x:
            todos_los_picos_x.append(idx_global)
            todos_los_picos_y.append(data[idx_global])

    # Actualizamos la línea azul (solo lo que se ve)
    line.set_data(x_ventana, y_ventana)
    
    # Actualizamos los puntos rojos (filtramos para mostrar solo los que caen en la ventana)
    # Si quieres que se vean TODOS aunque estén fuera de vista (no recomendado por memoria), 
    # solo quita el filtrado. Aquí filtramos para que Matplotlib no se ponga lento:
    visibles_x = [px for px in todos_los_picos_x if px >= start]
    visibles_y = [todos_los_picos_y[i] for i, px in enumerate(todos_los_picos_x) if px >= start]
    
    peaks_dots.set_data(visibles_x, visibles_y)
    
    # Desplazar eje X
    ax.set_xlim(start, start + ancho_ventana)
    
    return line, peaks_dots

# 4. Ejecutar
ani = FuncAnimation(fig, update, frames=range(0, len(data), 20), 
                    interval=20, blit=False, repeat=False)

plt.show()