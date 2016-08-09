from LEDsetup import*
led.fill(Off)
led.update()

def I(Color):
    i=[11,17,21,27,31,37,41,42,43,44,45,46,47,51,52,53,54,55,56,57,61,67,71,77]
        for i in i:
            led.set(i,color)
            led.update()
I(Brown)
