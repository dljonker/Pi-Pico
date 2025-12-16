# Source: Electrocredible.com, Language: MicroPython

from machine import Pin,I2C
from bmp280 import * # type: ignore
import time

sdaPIN=machine.Pin(0) # type: ignore
sclPIN=machine.Pin(1) # type: ignore
bus = I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
time.sleep(0.1)
bmp = BMP280(bus) # type: ignore

bmp.use_case(BMP280_CASE_INDOOR) # type: ignore

while True:
    pressure=bmp.pressure
    p_bar=pressure/100000
    p_mmHg=pressure/133.3224
    temperature=bmp.temperature
    print("Temperature: {} C".format(temperature))
    print("Pressure: {} Pa, {} bar, {} mmHg".format(pressure,p_bar,p_mmHg))
    time.sleep(1)