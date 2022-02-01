from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image(
        "00000:"
        "09090:"
        "00500:"
        "90009:"
        "09990:"
       ))
    if button_b.was_pressed():
        display.clear()