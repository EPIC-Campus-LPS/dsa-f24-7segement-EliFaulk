import tm1637
import time

#Display
display = tm1637.TM1637(clk=21, dio=20)
clear = [0, 0, 0, 0]

#Wait for input of name, and then print "Hello {name}"
display.write(clear)
time.sleep(1)
message = "Hello " + input("Hi, what's your name? ")
display.scroll(message, delay=250)
