from pyA20.gpio import gpio
from pyA20.gpio import port
#from pyA20.gpio import connector
#from orangepwm import *
from time import sleep

gpio.init() #Initialize module. Always called first

#pwm = OrangePwm(2000, port.PA12)

gpio.setcfg(port.PA11, gpio.INPUT) #Vhod za stikalo za luč
gpio.setcfg(port.PA12, gpio.OUTPUT)

#gpio.pullup(port.PA11, 0)
gpio.pullup(port.PA11, gpio.PULLUP)
#gpio.pullup(port.PA11, gpio.PULLDOWN)

while True:
	if gpio.input(port.PA11) == 0:
		gpio.output(port.PA12, gpio.HIGH)
		#pwm.start(15)
		print("HIGH")
	else:
		gpio.output(port.PA12, gpio.LOW)
		#pwm.stop()
		print("LOW")
#	sleep(0.08)
