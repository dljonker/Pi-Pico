from machine import Pin
from neopixel import NeoPixel
from machine import Pin, SoftI2C, I2C
import ssd1306 # type: ignore
from bmp280 import *
from time import sleep
import dht

sdaPIN=machine.Pin(0)
sclPIN=machine.Pin(1)
bus = I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
sleep(0.1)
bmp = BMP280(bus)

bmp.use_case(BMP280_CASE_INDOOR)

sensor = dht.DHT22(Pin(22))

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

num_pixels = 10
color = (0, 0, 0)

strip_pin = Pin(28, Pin.OUT)

my_strip = NeoPixel(strip_pin, num_pixels)

my_strip.fill(color)
my_strip.write()


while True:
  try:
    sensor.measure()
    temp = sensor.temperature()
    temp_string = str(temp)
    hum = sensor.humidity()
    hum_string = str(hum)
    pressure=bmp.pressure
    pressure_string = str(pressure)
    #temperature=bmp.temperature
    #temperature_string = str(temperature)
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    print("Temperature: {} C".format(temperature))
    print("Pressure: {} Pa".format(pressure))
    oled.text('Temperatura:', 0, 0)
    oled.text(temp_string, 0, 10)
    oled.text('Umidade:', 0, 20)
    oled.text(hum_string, 0, 30)
    oled.text('Pressao:', 0, 40)
    oled.text(pressure_string, 0, 50)
    oled.show()
    sleep(30)
    oled.fill(0)
    oled.show()
  except OSError as e:
    print('Failed to read sensor.')