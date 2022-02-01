from microbit import *
import music

while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 20 and reading_y < -20:
        display.show(Image("00999:"
                           "00009:"
                           "00009:"
                           "00000:"
                           "00000:"
                           ))
                           
    elif reading_x > 20 and reading_y > 20:
        display.show(Image("00000:"
                           "00000:"
                           "00009:"
                           "00009:"
                           "00999:"
                           ))
                           
    elif reading_x < -20 and reading_y > 20:
        display.show(Image("00000:"
                           "00000:"
                           "90000:"
                           "90000:"
                           "99900:"
                           ))
    
    elif reading_x < -20 and reading_y < -20:
        display.show(Image("99900:"
                           "90000:"
                           "90000:"
                           "00000:"
                           "00000:"
                           ))
    
    else: display.show("-")