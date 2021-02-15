import socket
import time
import RPi.GPIO as GPIO


#Initializing Pin For Motor-Driver
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)   #Forward
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)   #Right
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)   #Left
GPIO.setup(4, GPIO.OUT)   #Enable pin of motor Driver
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)  #Reverse
#reverse = 8

forward = 22
right = 17
left = 27
speed = GPIO.PWM(4,90)
speed.start(12)

#Initializing Client Socket for Receiving
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.31.120",1234))

while True:
     msg = s.recv(10)
     receiver = int(msg.decode("utf-8"))
     print(receiver)
             
     if receiver == 2:
          #self.serial_port.write(chr(1).encode())
          GPIO.output(forward, GPIO.HIGH)
          print("Forward")
     elif receiver == 0:
          #self.serial_port.write(chr(7).encode())
          GPIO.output(right, GPIO.LOW)
          GPIO.output(forward, GPIO.HIGH)
          GPIO.output(left, GPIO.HIGH)
          print("Left-Forward")
     elif receiver == 1:
          #self.serial_port.write(chr(6).encode())
          GPIO.output(left, GPIO.OUT)
          GPIO.output(forward, GPIO.HIGH)
          GPIO.output(right, GPIO.HIGH)
          print("Right-Forward")
     elif receiver == 3:
          GPIO.output(forward, GPIO.LOW)
          GPIO.output(left, GPIO.LOW)
          GPIO.output(right, GPIO.LOW)
          #GPIO.output(reverse, GPIO.LOW)
          print("Stop Car")
     elif receiver == 11:
          GPIO.output(left, GPIO.LOW)
          print("Left")
     elif receiver == 22:
          GPIO.output(right, GPIO.LOW)
          print("Right")



