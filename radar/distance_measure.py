from gpiozero import DistanceSensor
import keyboard


ultrasonic = DistanceSensor(echo=17, trigger=4)

max_value = 0

while True:

    new_distance = ultrasonic.distance
    print(ultrasonic.distance)

    if new_distance > max_value:
        max_value = new_distance

    if keyboard.is_pressed('a'):
        break

print(f"La mayor distancia registrada ha sido de {round(max_value*100, 2)} centimetros.")