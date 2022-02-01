from microbit import *
compass.calibrate()

while True:
    if button_a.was_pressed():
        display.scroll(compass.get_field_strength())
    if button_b.was_pressed():
        display.scroll(str(compass.heading()))