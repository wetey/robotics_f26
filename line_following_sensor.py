import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
print(GPIO.BCM)
LINE_PIN = 23

GPIO.setup(LINE_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(LINE_PIN) == GPIO.HIGH:
            print("line detected")
        else:
            print("no line detected")
        sleep(2)
except KeyboardInterrupt:
    print("quitting")
    GPIO.cleanup()
