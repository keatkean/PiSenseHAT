from sense_hat import SenseHat

sense = SenseHat()
try:
    while True:
        t = sense.get_temperature()
        t2 = sense.get_temperature_from_pressure()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t,1)
        t2 = round(t2,1)
        p = round(p,1)
        h = round(h,1)

        final_t = round((t+t2)/2,1)

        msg = "Temp: " + str(final_t) + " Humid: " + str(h)
        sense.show_message(msg, scroll_speed=0.05)
except KeyboardInterrupt:
    print('Application Terminated.')
    sense.clear()