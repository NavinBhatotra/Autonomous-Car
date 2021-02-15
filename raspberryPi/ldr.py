import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
input_ldr = 18 #input of the LDR Sensor
led = 12 #led pin
GPIO.setup(input_ldr,GPIO.IN)
GPIO.setup(led,GPIO.OUT,initial=0)

while True:

    print (GPIO.input(input_ldr))
    if(GPIO.input(input_ldr)==1):
        GPIO.output(led,GPIO.HIGH)
    else:
         GPIO.output(led,GPIO.LOW)   
