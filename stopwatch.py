import tm1637
import time
import RPi.GPIO as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Light
GPIO.setup(18, GPIO.OUT)
#Button
GPIO.setup(19, GPIO.IN)
#Display & Stopwatch Timer
display = tm1637.TM1637(clk=21, dio=20)
clear = [0, 0, 0, 0]
stopwatch = 0


while True:
	#Wait for input, and when detected, turn on the light and start the stopwatch
	if GPIO.input(19) == 0:
		time.sleep(1)
		GPIO.output(18, GPIO.HIGH)
		print("Stopwatch Start")
		
		#Until button is pressed again, run stopwatch
		while GPIO.input(19) != 0:
			time.sleep(1)
			stopwatch += 1
			display.show(str(stopwatch))
		
		#End timer and turn off light
		print("Stopwatch Ends")
		GPIO.output(18, GPIO.LOW)
		break

#Display stopwatch time for 2 seconds before clearing
display.show(str(stopwatch))
time.sleep(2)
display.write(clear)
