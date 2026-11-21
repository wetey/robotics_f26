import RPi.GPIO as GPIO
import time
PIR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
time.sleep(30)
try:
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            print("motion detected")
        else:
            print("nothing")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("quitting")
    GPIO.cleanup()



# from gpiozero import MotionSensor
# import time
# pir = MotionSensor(23)
# time.sleep(60)
# try:
#     while True:
#         if pir.motion_detected:
#             print("motion detected")
#         else:
#             print("nothing")
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\nExiting...")
#     GPIO.cleanup()