import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

x=[23,18]
for i in range(len(x)):
    GPIO.setup(x[i],GPIO.OUT)

while True :
    for j in range(4):
        c=format(j,"02b")
        GPIO.output(23,int(c[0]))
        GPIO.output(18,int(c[1]))
        print(c,"=",j)
        time.sleep(1)
