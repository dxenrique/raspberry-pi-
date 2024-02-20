import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

while True:
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    print("0")
    time.sleep(1)

    GPIO.output(23,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    print("1")
    time.sleep(1)

    GPIO.output(23,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    print("2")
    time.sleep(1)

    GPIO.output(23,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    print("3")
    time.sleep(1)