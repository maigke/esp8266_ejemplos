import machine
import ssd1306
import time

# Configuración del I2C y la pantalla OLED
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Limpiar la pantalla y mostrar un mensaje inicial
oled.fill(0)
oled.text("Hola!!", 0, 0)
oled.show()

# Configuración del UART (puerto serie)
uart = machine.UART(0, baudrate=115200)

while True:
    if uart.any():
        #data = uart.readline().decode('utf-8').strip()
        #print('Data received:', data)  # Imprimir los datos recibidos en la consola serie

        # Limpiar pantalla
        oled.fill(0)

        # Mostrar los datos recibidos en la pantalla OLED
        oled.text(data, 0, 0)
        oled.show()

        # Enviar los datos de vuelta por el puerto USB
        uart.write(data + '\n')

    time.sleep(1)

    # Código adicional de prueba
    a = 2
    b = 3
    result = f'La suma de {a} + {b} = {a + b}'
    print(result)
    uart.write(result + '\n')
