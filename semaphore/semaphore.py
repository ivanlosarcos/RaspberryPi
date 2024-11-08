from gpiozero import LED, Button, Buzzer
from time import sleep

button = Button(21)

green = LED(12)
yellow = LED(16)
red = LED(20)

buzzer = Buzzer(2)


button.wait_for_press()
while True:
    red.on()
    sleep(1)
    red.off()

    yellow.on()
    sleep(1)
    yellow.off()

    green.on()
    sleep(1)
    green.off()

    buzzer.beep()

    button.wait_for_press() = break