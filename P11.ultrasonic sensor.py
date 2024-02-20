import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIGGER=18
ECHO=23
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    GPIO.output(TRIGGER,GPIO.LOW)
    time.sleep(1)
    GPIO.output(TRIGGER,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER,GPIO.LOW)

    while (GPIO.input(ECHO)==0):
        starttime=time.time()
    while(GPIO.input(ECHO)==1):
        stoptime=time.time()

        timeelapsed=stoptime-starttime
        distance=(timeelapsed*34400)/2
        print(round(distance),"cm")
        time.sleep(1)