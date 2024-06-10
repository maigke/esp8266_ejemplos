import machine
import ssd1306
import time

# Configuración
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def fade_out():
    for i in range(255, 0, -5):
        oled.fill(0)
        oled.text("Transicion", 0, 0)
        oled.show()
        oled.contrast(i)
        time.sleep_ms(50)
        

def show_new_screen():
    oled.fill(0)
    oled.show()
    oled.text("Nueva pantalla", 0, 0)
    oled.show()

# Mostrar la pantalla inicial
oled.text("Puqui", 0, 0)
oled.show()
time.sleep_ms(5000)
# Realizar la transición
fade_out()
oled.text("nuevo",0,16)
oled.show()
time.sleep(3)
show_new_screen()
