from gpiozero import LightSensor
from time import sleep

ldr = LightSensor(4)

while True:
    print(f"Light sensor value: {ldr.value:.2f}")
    sleep(0.5)