from machine import Pin
from neopixel import NeoPixel
from time import sleep

num_pixels = 10
color = (255, 255, 255)

strip_pin = Pin(28, Pin.OUT)

my_strip = NeoPixel(strip_pin, num_pixels)

my_strip.fill((100, 100, 100))
my_strip.write()

#while True:
    #for i in range(0, num_pixels):
        #my_strip.fill((0, 0, 0))
        #my_strip[i] = color
        #my_strip.write()
        #sleep(1.5)

#(RED, GREEN, BLUE)
# 0 to 255 - Brightness


""" def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write() """