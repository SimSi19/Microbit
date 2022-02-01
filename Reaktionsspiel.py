from microbit import *          #Alle librarys hinzugefügt
import random                   #Random librarys hinzugefügt

ready = True                    #hilfsvariabel

while ready:                                        #Schleife zu Überprüfung der Startsequenz
    gesture = accelerometer.current_gesture()       #entnimmt jetztige Position
    gameStarted = False                             #hilfsvariabel

    if gesture == "face up":                                        #Wenn microbit "face up" ist
        if button_a.is_pressed() and button_b.is_pressed():         #Wenn beide Knöpfe gedrückt sind
            display.show(Image.HAPPY)                               #Smiley auf 5x5 LED Feld
            sleep(500)                                              #Code wird für 500ms pausiert
            display.clear()                                         #LED Feld gelöscht
            ready = False                                           #hilfsvariabel
            gameStarted = True                                      #ende der Schleife

    else:
        display.show("-")                                           #sonst "-" angezeigt


while gameStarted:                              #Spielstart
    sleep(random.randint(3000, 30000))          #Wartezeit zwischen 3 und 30sek
    gameStarted = False                         #Schleife stoppen
    action = random.randrange(6)                #zufallszahl zwischen 0 und 5
    start = running_time()                      #stopuhr anfang
    loop = True                                 #hilfsvariabel

    if action == 0:                                     #Wenn zufallszahl zutrifft
        display.show("A")                               #"A" anzeigen

        while loop:                                     #Schleife wartet bis if ausgeführ wird
            if button_a.is_pressed():
                display.clear()                         #LED Feld löschen
                time = running_time() - start           #Zeit seit stopuhr anfang
                points = max(0, 5000-time)              #kann nicht unter 0, punkte wird als 5000-gebrauchte Zeit gewärtet
                display.scroll(str(points))             #anzeigen der Punkte
                loop = False                            #Schlaife wird gestopt



    elif action == 1:               #same as A
        display.show("B")

        while loop:
            if button_b.is_pressed():
                display.clear()
                time = running_time() - start
                points = max(0, 5000-time)
                display.scroll(str(points))
                loop = False



    elif action == 2:
        display.show(Image.ARROW_N)         #Pfeil nach oben

        while loop:
            gesture = accelerometer.current_gesture()       #jetztige Position durchgehend abgefragt
            if gesture == "down":                           #wenn nach unten gezeigt wird dann stop vorgang
                display.clear()
                time = running_time() - start
                points = max(0, 5000-time)
                display.scroll(str(points))
                loop = False



    elif action == 3:
        display.show(Image.ARROW_E)

        while loop:
            gesture = accelerometer.current_gesture()
            if gesture == "right":
                display.clear()
                time = running_time() - start
                points = max(0, 5000-time)
                display.scroll(str(points))
                loop = False



    elif action == 4:
        display.show(Image.ARROW_S)

        while loop:
            gesture = accelerometer.current_gesture()
            if gesture == "up":
                display.clear()
                time = running_time() - start
                points = max(0, 5000-time)
                display.scroll(str(points))
                loop = False



    elif action == 5:
        display.show(Image.ARROW_W)

        while loop:
            gesture = accelerometer.current_gesture()
            if gesture == "left":
                display.clear()
                time = running_time() - start
                points = max(0, 5000-time)
                display.scroll(str(points))
                loop = False

