import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

while True:
    GPIO.output(18,GPIO.HIGH)
    print("led on")
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    print("led off")
    time.sleep(1)