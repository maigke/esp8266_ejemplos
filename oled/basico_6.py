import machine
import ssd1306
import time

# Configuración
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def scroll_text(text, delay=0.1):
    # Mueve el texto de izquierda a derecha
    for i in range(len(text) + 128):
        oled.fill(0)
        oled.text(text, 128 - i, 0)
        oled.show()
        time.sleep(delay)

# Mostrar el texto inicial
oled.text("Hola, mundo!", 0, 0)
oled.show()

# Desplazar el texto
scroll_text("Hola, mundo!")

# Esperar antes de salir
time.sleep(2)
