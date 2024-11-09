from gpiozero import DistanceSensor, LED
import time
from picamera2 import Picamera2, Preview


ultrasonic = DistanceSensor(echo=17, trigger=4)
led = LED(21)

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)


def calculate_speed(a, b, time_interval):
    speed = abs(a-b)/time_interval
    return speed 
    

threshold=1.5
start_time = time.time()
last_distance = ultrasonic.distance 


while True:
    time.sleep(0.1)
    
    current_time = time.time()
    time_interval = current_time - start_time
    
    current_distance = ultrasonic.distance
    
    speed = calculate_speed(last_distance, current_distance, time_interval)
    print(f"Velocidad: {speed} metros por segundo")

    if speed > threshold:
        led.on()
        print("Velocidad superada, tomando foto...")
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")  
        picam2.start_preview(Preview.NULL)
        picam2.start_and_capture_file(f"foto_{timestamp}.jpg")
        
        print("Foto tomada y guardada.")
        time.sleep(1)
        break


    last_distance = current_distance
    start_time = current_time