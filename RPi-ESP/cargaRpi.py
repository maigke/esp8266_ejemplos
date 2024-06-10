import serial
import psutil
import time

# Configuración del puerto serie
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

while True:
    # Obtener la carga del procesador
    cpu_usage = psutil.cpu_percent(interval=1)

    # Obtener el uso de la memoria RAM
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Crear la cadena de datos
    data = f"CPU:{cpu_usage}%,RAM:{memory_usage}%\n"

    # Enviar datos al ESP8266
    ser.write(data.encode('utf-8'))
    print(data)

    # Esperar antes de enviar nuevamente
    time.sleep(60)
