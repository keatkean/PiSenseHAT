from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
r = 255
g = 255
b = 255

sense.clear((r,g,b))
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
yellow = (255,255,0)

def random_colour():
    return (randint(0,255), randint(0,255), randint(0,255)) # R,G,B
#sense.show_message("Hello World",scroll_speed=0.1, text_colour=yellow, back_colour=blue)
#sleep(1)

sense.show_letter("N", random_colour())
sleep(1)
sense.show_letter("Y", random_colour())
sleep(1)
sense.show_letter("P", random_colour())
sleep(1)

sense.clear()