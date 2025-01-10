from sense_hat import SenseHat

sense = SenseHat()
try:
    while True:
        h = sense.get_humidity()

        h = int(h)

        sense.show_message(str(h), scroll_speed=0.05)

except KeyboardInterrupt:
    print('Application Terminated.')
    sense.clear()

    