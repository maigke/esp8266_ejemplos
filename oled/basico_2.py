import machine
import ssd1306

# Configura la comunicación I2C con la pantalla OLED
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Limpia la pantalla
oled.fill(0)
oled.show()

# Muestra texto en varias líneas
line1 = "Hola, mundo!"
line2 = "Bienvenidos a"
line3 = "MicroPython!"

oled.text(line1, 0, 0)
oled.text(line2, 0, 16)
oled.text(line3, 0, 32)
oled.show()
