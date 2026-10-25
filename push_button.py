# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BCM)

# LED_PIN = 24
# PUSH_PIN = 23


# GPIO.setup(LED_PIN, GPIO.OUT)
# GPIO.setup(PUSH_PIN, GPIO.IN)

# try:
#     while True:
#         if GPIO.input(PUSH_PIN) == 1:
#             print("Push button pressed")
#             GPIO.output(LED_PIN, True)
#             time.sleep(2)
#         else:
#             GPIO.output(LED_PIN, False)

# except KeyboardInterrupt:
#     GPIO.cleanup()
#     print("Quitting")



from gpiozero import Button, LED
from time import sleep

button = Button(23)
led = LED(24)

try:
    while True:
        if button.is_pressed:
            print("button pressed")
            led.value = 1 # led.on
        else:
            led.value = 0 # led.off
        sleep(2)
except KeyboardInterrupt:
    print("Quitting")