import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#For each GPIO pin, set it for output and set it to high (turn them on)
for i in range(27):
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)
time.sleep(2)

#For each GPIO pin, set each to low (turn them off)
for i in range(27):
	GPIO.output(i, GPIO.LOW)

