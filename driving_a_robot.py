import RPi.GPIO as GPIO
from time import sleep

IN1 = 23
IN2 = 24
IN3 = 25
IN4 = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


try:
    while True:
        
        # drive forward
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)
        GPIO.output(IN3, True) 
        GPIO.output(IN4, False)

        sleep(2)

        # drive backward
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(IN3, False) 
        GPIO.output(IN4, True)

except KeyboardInterrupt:
    print("quitting")
    GPIO.cleanup()

