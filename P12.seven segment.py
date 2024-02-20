import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

list=[OxC0,OxF9,OxA4,OxB0,Ox99,Ox92,Ox82,OxF8,Ox80,Ox90];

y=[24,23,22,27,18,17,4]
for i in range(len(y)):
    GPIO.setup(y[i],GPIO.OUT)

while True:
    for j in range(10):
        c=format(list[j],'08b')
        print(c,"=",j)
        for k in range(len(y)):
            GPIO.output(y[k],int(c[k+1]))
    time.sleep(1)