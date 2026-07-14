from machine import Pin, I2C
import ssd1306
import time
import random

# OLED SETUP
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# BUTTON SETUP
button = Pin(4, Pin.IN, Pin.PULL_UP)

best_time = None


def center(text, y):
    x = (128 - len(text) * 8) // 2
    if x < 0:
        x = 0
    oled.text(text, x, y)


while True:

    # START SCREEN
    oled.fill(0)
    center("REACTION TEST", 8)
    center("Press Button", 30)
    center("to Start", 45)
    oled.show()

    # Wait for button press
    while button.value() == 1:
        pass

    # Wait until button is released
    while button.value() == 0:
        pass

    time.sleep_ms(200)

    # COUNTDOWN
    false_start = False

    for num in ["3", "2", "1"]:

        oled.fill(0)
        center(num, 25)
        oled.show()

        start = time.ticks_ms()

        while time.ticks_diff(time.ticks_ms(), start) < 1000:
            if button.value() == 0:
                false_start = True
                break

        if false_start:
            break

    if false_start:
        oled.fill(0)
        center("Too Early!", 20)
        center("Game Reset", 40)
        oled.show()

        while button.value() == 0:
            pass

        time.sleep(2)
        continue

    # RANDOM WAIT
    delay = random.randint(2000, 5000)

    start = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start) < delay:
        if button.value() == 0:
            false_start = True
            break

    if false_start:
        oled.fill(0)
        center("Too Early!", 20)
        center("Game Reset", 40)
        oled.show()

        while button.value() == 0:
            pass

        time.sleep(2)
        continue

    # GO!
    oled.fill(0)
    center("GO!", 25)
    oled.show()

    reaction_start = time.ticks_ms()

    while button.value() == 1:
        pass

    reaction = time.ticks_diff(time.ticks_ms(), reaction_start)

    while button.value() == 0:
        pass

    if best_time is None or reaction < best_time:
        best_time = reaction
        new_record = True
    else:
        new_record = False

    # RESULTS
    oled.fill(0)
    oled.text("Reaction:", 0, 0)
    oled.text(str(reaction) + " ms", 0, 15)
    oled.text("Best:", 0, 38)
    oled.text(str(best_time) + " ms", 0, 53)
    oled.show()

    time.sleep(3)

    if new_record:
        oled.fill(0)
        center("NEW RECORD!", 15)
        center(str(best_time) + " ms", 35)
        oled.show()
        time.sleep(2)