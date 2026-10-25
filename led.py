# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)

# LED_PIN = 14

# GPIO.setup(LED_PIN, GPIO.OUT)

# try:
#     while True:
#         GPIO.output(LED_PIN, GPIO.HIGH)
#         time.sleep(2)
#         GPIO.output(LED_PIN, GPIO.LOW)

# except KeyboardInterrupt:
#     print(" Quit")


from gpiozero import LED
from time import sleep 

LED_BLUE = LED(14) # default uses the BCM layout LED("GPIO14") or LED("BCM14") or LED("BOARD8")

try:
    while True:
        LED_BLUE.value = 0
        sleep (1)
        LED_BLUE.value = 1
        sleep(1)

except KeyboardInterrupt:
    print("Quitting")