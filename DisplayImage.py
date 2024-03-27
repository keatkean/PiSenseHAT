from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_pixel(2,2,(0,0,255))
sense.set_pixel(4,2,(0,0,255))
sense.set_pixel(3,4,(100,0,0))
sense.set_pixel(1,5,(255,0,0))
sense.set_pixel(2,6,(255,0,0))
sense.set_pixel(3,6,(255,0,0))
sense.set_pixel(4,2,(255,0,0))
sense.set_pixel(5,5,(255,0,0))
sleep(1)

g = (0,255,0)
b = (0,0,0)

creeper_pix = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,b,b,g,g,b,b,g,
    g,b,b,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,g,g,b,g,g
]

sense.set_pixels(creeper_pix)
sleep(1)

B = (102,51,0)
a = (0,0,255)
S = (205,133,63)
W = (255,255,255)

steve_pix = [
    B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    B,S,S,S,S,S,S,B,
    S,S,S,S,S,S,S,S,
    S,W,a,S,S,a,W,S,
    S,S,S,B,B,S,S,S,
    S,S,B,S,S,B,S,S,
    S,S,B,B,B,B,S,S
]
sense.set_pixels(steve_pix)
sleep(3)
sense.clear()