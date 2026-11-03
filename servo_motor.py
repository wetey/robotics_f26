# import RPi.GPIO as GPIO

# from time import sleep

# SERVO_PIN = 23

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(SERVO_PIN, GPIO.OUT)

# pwm = GPIO.PWM(SERVO_PIN, 50) # 50Hz, the frequency the servo motor operate at

# pwm.start(0) # duty cycle is set to zero

# try:
#     while True:
        
#         pwm.ChangeDutyCycle(5) # left -90 deg position, 5%
#         sleep(1)
#         pwm.ChangeDutyCycle(7.5) # neutral position, 7.5%
#         sleep(1)
#         pwm.ChangeDutyCycle(10) # right +90 deg position, 10%
#         sleep(1)
# except KeyboardInterrupt:
#     print("quitting")
#     pwm.stop()
#     GPIO.cleanup()


from gpiozero import Servo
from time import sleep

servo = Servo(23)

try:
    while True:
        servo.min()
        sleep(2)
        servo.mid()
        sleep(2)
        servo.max()
        sleep(2)

except KeyboardInterrupt:
    print("quitting")