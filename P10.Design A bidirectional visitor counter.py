import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

y=1
while y>0:
    if GPIO.input(18)==1:
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        if GPIO.input(18)==0:
            GPIO.output(23,GPIO.LOW)
            print("student count is ",y)
            y=y+1
    else:
        GPIO.output(23,GPIO.LOW)
