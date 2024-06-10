import machine
import ssd1306

#Configuracion
i2c = machine.I2C( scl = machine.Pin(22),
                   sda = machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#limpia la pantalla
oled.fill(0)
oled.show()

#muestra el texto
oled.text("¡¡Hola!!", 0, 0)
oled.show()