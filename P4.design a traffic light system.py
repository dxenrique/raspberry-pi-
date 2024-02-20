import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

#x=[18,19,20]
#for i in range(len(x)):
    #GPIO.setup(x[i],GPIO.OUT)



while True:
    print("STOP")
    for i in range(10,0,-1):
        print(i)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
    GPIO.output(18,GPIO.LOW)

    print("READY")
    for i in range(3,0,-1):
        print(i)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(1)
    GPIO.output(19,GPIO.LOW)

    print("GO")
    for i in range(15,0,-1):
        print(i)
        GPIO.output(20,GPIO.HIGH)
        time.sleep(1)
    GPIO.output(20,GPIO.LOW)



