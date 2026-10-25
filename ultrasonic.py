# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM) 

# # where we'll connect the pins 
# TRIG = 23
# ECHO = 24

# pulse_end = 0
# pulse_start = 0

# # configure the input and output pins
# GPIO.setup(TRIG, GPIO.OUT)
# GPIO.setup(ECHO, GPIO.IN)

# try:
#     while True:
#         GPIO.output(TRIG, False)
#         time.sleep(2)

#         GPIO.output(TRIG, True)
#         time.sleep(0.00001) # trigger pulse for 10micro seconds
#         GPIO.output(TRIG, False)

#         print("TRIG pulse sent")

#         print("while ECHO low")
#         while GPIO.input(ECHO) == 0:
#             pulse_start = time.time()

#         print("while ECHO high")
#         while GPIO.input(ECHO) == 1:
#             pulse_end = time.time()

#         print("calculating distance to object")
#         pulse_duration = pulse_end - pulse_start    

#         distance = (pulse_duration * 34000) /  2

#         print(f"Distance to object {distance:.2f}")
# except KeyboardInterrupt:
#     GPIO.cleanup()



from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)

try:
    while True:
        print('Distance: ', sensor.distance * 100)
        sleep(3)

except KeyboardInterrupt:
    print("Quitting")