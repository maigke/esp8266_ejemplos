import machine
import ssd1306
import time

# Configuración del UART (puerto serie)
uart = machine.UART(0, baudrate=115200)

# Configuración del OLED
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text('Loading',0,0)
oled.show()
time.sleep(5);
oled.text('some',0,16)
oled.show()
while True:
    if uart.any():
        data = uart.readline().decode('utf-8').strip()
        print(data)
        if data:
            try:
                cpu_usage, memory_usage = data.split(',')

                # Limpiar pantalla
                oled.fill(0)
                oled.show()

                # Mostrar datos en la pantalla OLED
                oled.text(cpu_usage, 0, 0)
                oled.text(memory_usage, 0, 10)
                oled.show()

            except Exception as e:
                print('Error:', e)

    time.sleep(1)
