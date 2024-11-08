from gpiozero import LED, Button, Buzzer
from time import sleep

button = Button(21)

green = LED(20)
yellow = LED(16)
red = LED(12)

buzzer = Buzzer(2)

def regresive_count(time):
    for i in range(time, 0, -1):
        if i > 5:  
            buzzer.beep()
            sleep(1)
        else:
            buzzer.beep()
            sleep(0.5)
        print(f"Tiempo restante: {i} segundos")


def semaphore():

    while True:
        green.on()
        button.wait_for_press()
        buzzer.beep()

        regresive_count(10)

        green.off()
        yellow.on()
        sleep(2)
        yellow.off()


        red.on()
        buzzer.beep()
        sleep(2)

        regresive_count(10)
        
        red.off()
        yellow.off()
        
        sleep(1)
        

semaphore()