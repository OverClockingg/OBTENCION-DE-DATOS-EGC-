# OBTENCION-DE-DATOS-EGC-
Generador de Señales ECG para FPGA
Este proyecto contiene las herramientas necesarias para extraer, procesar y normalizar señales electrocardiográficas (ECG) reales de la base de datos PhysioNet, preparándolas para ser cargadas en una memoria ROM dentro de una FPGA.

Procesamiento en Python: Selección de derivaciones, normalización a 8 bits (0-255) y ajuste de continuidad de fase.
Sincronización de Eventos: Localización precisa del pico R para control de periféricos (como buzzers).

Contenido del Repositorio
EGC.py: Simulación animada de la señal con detección de picos en tiempo real.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/33c07c69-cd7e-4447-bb46-ddddaa011322" />
EXPORTEGC.py: Script unificado para recorte, normalización y exportación de datos.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/24f57144-f25f-4b2d-bb1a-df8597b897d7" />

GRAPHICROM.py: Herramienta de visualización para verificar la continuidad y el rango de la señal antes de grabarla.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/219b83ed-53ed-451a-b63b-4ace56966190" />

ecg_rom_final.txt: Arreglo de 900 muestras listo para el hardware.

Especificaciones Técnicas
Paciente: s0010_re (Infarto ínfero-lateral).

Derivación utilizada: Derivación I.

Frecuencia de muestreo: 1000 Hz.

Resolución: 8 bits (DAC R-2R).

Punto de sincronía (Beep): Muestra 73
