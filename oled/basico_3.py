# Importa las bibliotecas necesarias
import machine
import ssd1306

# Configura la comunicación I2C con la pantalla OLED
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Limpia la pantalla
oled.fill(0)
oled.show()

# Dibuja un rectángulo rojo en la primera línea (0, 0 a 127, 15)
oled.fill_rect(0, 0, 128, 15, 1)

# Dibuja un rectángulo verde en la segunda línea (0, 16 a 127, 31)
oled.fill_rect(0, 16, 128, 15, 1)

# Actualiza la pantalla
oled.show()
