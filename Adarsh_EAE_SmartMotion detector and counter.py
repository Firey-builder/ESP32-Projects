from machine import Pin, SoftI2C
import ssd1306
import time

# OLED
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# PIR Sensor
pir = Pin(27, Pin.IN)

motion_count = 0
last_state = 0

while True:

    motion = pir.value()

    if motion == 1 and last_state == 0:

        motion_count += 1

        oled.fill(0)
        oled.text("MOTION", 25, 10)
        oled.text("DETECTED!", 18, 30)
        oled.text("Count: {}".format(motion_count), 10, 55)
        oled.show()

        time.sleep(3)

    if motion == 0:

        oled.fill(0)
        oled.text("SMART", 35, 10)
        #oled.text("ADARSH", 30, 10)
        oled.text("MONITOR", 25, 30)
        oled.text("Count: {}".format(motion_count), 10, 55)
        oled.show()

    last_state = motion

    time.sleep(0.1)