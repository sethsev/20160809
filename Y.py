from LEDsetup import*
led.update()
led.fill(Off)

def Y (Color):
    y[17,27,67,77,16,26,66,76,15,25,65,75,24,34,44,54,64,74,63,73,62,72,21,31,41,51,61,71]
for i in y:
    led.set(i,Color)
    led.update


Y(Yellow)
