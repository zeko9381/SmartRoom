import os
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

gpio.init()

sensor = port.PA12

gpio.setcfg(sensor, gpio.INPUT)

while True:
	print(gpio.input(sensor))
	#if(gpio.input(sensor) == gpio.LOW):
		#while(gpio.input(sensor) == gpio.LOW):
		#	print("LOW")
		#os.system("mplayer obi-wan.mp3")
		#print("Hello there!")
