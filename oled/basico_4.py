import machine
import ssd1306
import time

# Configuración
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Variable con un valor
mi_variable = 42

# Función para mostrar el texto con el valor de la variable
def mostrar_valor():
    oled.fill(0)
    oled.text("Valor:", 0, 0)
    oled.text(str(mi_variable), 0, 16)  # Concatenamos el valor de la variable
    oled.show()

# Mostrar el texto inicial
oled.text("Pantalla OLED", 0, 0)
oled.show()

# Mostrar el valor de la variable
mostrar_valor()

# Esperar antes de salir
time.sleep(2)
