from microbit import *

while True:
    if display.read_light_level() > 200:
        display.scroll(str("Day"))
    else:
        display.scroll(str("Night"))
