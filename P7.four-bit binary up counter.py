import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

y=[18,23,24,25]
for i in range(len(y)):
    GPIO.setup(y[i],GPIO.OUT)

while True:
    for j in range(16):
        c=format(j,"04b")
        GPIO.output(18,int(c[0]))
        GPIO.output(23,int(c[1]))
        GPIO.output(24,int(c[2]))
        GPIO.output(25,int(c[3]))
        print(c,"=",j)
        time.sleep(1)