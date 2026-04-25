# OBTENCION-DE-DATOS-EGC-
Generador de Señales ECG para FPGA
Este proyecto contiene las herramientas necesarias para extraer, procesar y normalizar señales electrocardiográficas (ECG) reales de la base de datos PhysioNet, preparándolas para ser cargadas en una memoria ROM dentro de una FPGA.

Procesamiento en Python: Selección de derivaciones, normalización a 8 bits (0-255) y ajuste de continuidad de fase.
Sincronización de Eventos: Localización precisa del pico R para control de periféricos (como buzzers).

Contenido del Repositorio
EGC.py: Simulación animada de la señal con detección de picos en tiempo real.

EXPORTEGC.py: Script unificado para recorte, normalización y exportación de datos.

GRAPHICROM.py: Herramienta de visualización para verificar la continuidad y el rango de la señal antes de grabarla.

ecg_rom_final.txt: Arreglo de 900 muestras listo para el hardware.

Especificaciones Técnicas
Paciente: s0010_re (Infarto ínfero-lateral).

Derivación utilizada: Derivación I.

Frecuencia de muestreo: 1000 Hz.

Resolución: 8 bits (DAC R-2R).

Punto de sincronía (Beep): Muestra 73
