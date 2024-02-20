import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.IN)

while True:
    if GPIO.input(23)==1:
        GPIO.output(18,GPIO.HIGH)
        print("OBJECT DETECTED")
    else:
        GPIO.output(18,GPIO.LOW)
        print("OBJECT NOT DETECTED")