import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

# where we'll connect the pins 
TRIG = 23
ECHO = 24

pulse_end = 0
pulse_start = 0

# configure the input and output pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001) # trigger pulse for 10micro seconds
GPIO.output(TRIG, False)


while GPIO.input(ECHO) == 0:
    pulse_start = time.time()

while GPIO.input(ECHO) == 1:
    pulse_end = time.time()


pulse_duration = pulse_end - pulse_start    

distance = (pulse_duration * 34000) /  2

print(f"Distance to object {distance:.2f}")