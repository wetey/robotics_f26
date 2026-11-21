
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ENA = 18
IN1 = 23
IN2 = 24

IN3 = 25
IN4 = 16
ENB = 13

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# control motor speed
pwm_left = GPIO.PWM(ENA, 1000)
pwm_right = GPIO.PWM(ENB, 1000)

pwm_left.start(0)
pwm_right.start(0)


def set_speed(speed):
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)

# forward
def forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    set_speed(speed)


# backward
def backward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    set_speed(speed)

# left
def left(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    set_speed(speed)


# right
def right(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    set_speed(speed)

# stop
def stop():
    set_speed(0)

try:
    while True:
        print("forward")
        forward(50)
        time.sleep(2)

        print("backward")
        backward(50)
        time.sleep(2)

        print("left")
        left(40)
        time.sleep(2)

        print("right")
        right(40)
        time.sleep(2)

        print("stop")
        stop()
        time.sleep(2)

except KeyboardInterrupt:
    print("quitting")
    stop()
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()

