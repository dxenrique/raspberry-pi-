import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
list=[OxC0,OxF9,OxA4,OxB0,Ox99,Ox92,Ox82,OxF8,Ox80,Ox90]
y=[24,23,22,27,18,17,4]
for i in range(len(y)):
    GPIO.setup(y[i],GPIO.OUT)
TRIGGER=13
ECHO=19
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
    while (GPIO.input(ECHO)==1):
        stoptime=time.time()
T=stoptime-starttime
distance=(34400*T)/2
print(round(distance),"cm")
if distance<10:
    for j in range(len(list)):
        c=format(list[distance],"08b")
        for k in range(len(y)):
            GPIO.output(y[k],int(c[k+1]))
        time.sleep(0.1)
