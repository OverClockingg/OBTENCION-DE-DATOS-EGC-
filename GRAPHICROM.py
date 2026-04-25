import wfdb
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar el registro original
record = wfdb.rdrecord('s0010_re')
signal = record.p_signal[:, 1]  # Derivación II

# 2. SELECCIÓN DEL LATIDO (Ajusta estos números)
# En s0010_re, un latido limpio suele estar entre estas muestras:
inicio = 650
fin = 1550 
latido = signal[inicio:fin]

# 3. PROCESAMIENTO (Igual al que irá a la FPGA)
# Normalizamos a 8 bits (0-255) para un DAC R-2R
latido_norm = ((latido - np.min(latido)) / (np.max(latido) - np.min(latido)) * 255).astype(int)

# 4. GRÁFICA DE VERIFICACIÓN
plt.figure(figsize=(12, 6))

# Subplot 1: La señal completa con el área seleccionada
plt.subplot(2, 1, 1)
plt.plot(signal[:5000]) # Mostramos los primeros 5 seg
plt.axvspan(inicio, fin, color='red', alpha=0.3, label='Segmento a Exportar')
plt.title('Señal Original (Área de recorte)')
plt.legend()

# Subplot 2: El latido que entrará a la ROM (ya normalizado)
plt.subplot(2, 1, 2)
plt.plot(latido_norm, color='red')
plt.title(f'Latido a exportar (ROM: {len(latido_norm)} muestras, Rango: 0-255)')
plt.xlabel('Dirección de Memoria en FPGA')
plt.ylabel('Valor Digital (DAC)')
plt.grid(True)

plt.tight_layout()
plt.show()

# 5. Obtener el punto máximo y generar datos para VHDL
indice_pico = np.argmax(latido_norm)
valor_maximo = latido_norm[indice_pico]

print("-" * 30)
print(f"RESULTADOS PARA TU CÓDIGO VHDL:")
print(f"Tamaño de la ROM: {len(latido_norm)} muestras")
print(f"El pico R está en la MUESTRA: {indice_pico}")
print(f"Valor en ese punto: {valor_maximo} (Digital)")
print("-" * 30)

# Opcional: Generar el archivo listo para copiar y pegar en el array de VHDL
with open("datos_ecg.txt", "w") as f:
    f.write(", ".join(map(str, latido_norm)))