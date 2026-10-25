from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)
LED_BLUE = LED(14)
try:
    while True:
        distance = sensor.distance * 100

        print(f'Distance: {distance}')
        if distance < 20:
            LED_BLUE.value = 1
        else:
            LED_BLUE.value = 0
        sleep(3)

except KeyboardInterrupt:
    print("Quitting")