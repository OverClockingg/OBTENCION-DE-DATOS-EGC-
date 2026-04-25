import wfdb
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar el registro
record = wfdb.rdrecord('s0010_re')
# Usamos la Derivación I (Canal 0) porque se ve mejor
signal = record.p_signal[:, 0] 

# 2. SELECCIÓN DE RANGO
inicio = 650
fin = 1550 
latido = signal[inicio:fin]

# 3. NORMALIZACIÓN (0-255 para el DAC)
latido_norm = ((latido - np.min(latido)) / (np.max(latido) - np.min(latido)) * 255).astype(int)

# --- MEJORA DE CONTINUIDAD ---
# Forzamos que el primer dato sea igual al último para evitar el salto
latido_norm[0] = latido_norm[-1]
# Opcional: suavizamos los primeros 3 puntos para que no sea un cambio brusco
for i in range(1, 4):
    latido_norm[i] = int((latido_norm[i] + latido_norm[0]) / 2)
# -----------------------------

# 4. CÁLCULOS PARA VHDL
tamano_rom = len(latido_norm)
indice_pico = np.argmax(latido_norm)

print("-" * 40)
print(f"DATOS FINALES PARA TU VHDL (UPIITA):")
print(f"Tamaño de la ROM: {tamano_rom} muestras")
print(f"Muestra del Pico R (Buzzer): {indice_pico}")
print(f"Valor Inicio: {latido_norm[0]} | Valor Fin: {latido_norm[-1]}")
print("-" * 40)

# 5. GRÁFICA DE VERIFICACIÓN
plt.figure(figsize=(10, 5))
plt.plot(latido_norm, color='red', label='Señal ECG continua')
plt.scatter(indice_pico, latido_norm[indice_pico], color='blue', s=100, label='Punto del Beep')

# Dibujamos líneas para ver si los extremos coinciden
plt.axhline(y=latido_norm[0], color='green', linestyle=':', label='Nivel de Continuidad')

plt.title('Verificación de Continuidad para ROM')
plt.xlabel('Dirección de Memoria')
plt.ylabel('Valor Digital (0-255)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 6. EXPORTAR
with open('ecg_rom_final.txt', 'w') as f:
    for valor in latido_norm:
        f.write(f"{valor},\n")