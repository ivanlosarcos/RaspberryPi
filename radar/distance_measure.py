from gpiozero import DistanceSensor, PWMLED
import keyboard

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))
    
red = PWMLED(21)
green = PWMLED(26)
ultrasonic = DistanceSensor(echo=17, trigger=4)

max_value = 0


while True:

    new_distance = ultrasonic.distance
    red.value = clamp(1-ultrasonic.distance*2, 0, 1)
    green.value = clamp(ultrasonic.distance*2, 0, 1)

    print(f"Led Rojo: {round(red.value, 2)}, Led Verde: {round(green.value, 2)}")
    

    if new_distance > max_value:
        max_value = new_distance

    if keyboard.is_pressed('a'):
        break

red.value=0
green.value = 0
print(f"La mayor distancia registrada ha sido de {round(max_value*100, 2)} centimetros.")