from pyA20.gpio import gpio
from pyA20.gpio import port
from orangepwm import *
from time import sleep

gpio.init() #Initialize module. Always called first

#Configuration
pwm_port = port.PA12
pwm_freq = 1000 #Hz
switch_port = port.PA11
light_transition_time = 1000 #ms


pwm = OrangePwm(pwm_freq, pwm_port)
pwm.start(0)
gpio.setcfg(switch_port, gpio.INPUT)
gpio.pullup(switch_port, gpio.PULLUP)

state = gpio.input(switch_port)
last_state = state

try:
	while True:

		state = gpio.input(switch_port)

		if state != last_state:
			last_state = state
			if state == 0:
				print("HIGH")
				for i in range(101):
					pwm.changeDutyCycle(i)
					sleep(light_transition_time / 1000 / 101)

			if state == 1:
				print("LOW")
				for i in reversed(range(100)):
					pwm.changeDutyCycle(i)
					sleep(light_transition_time / 1000 / 100)
except KeyboardInterrupt:
	print("Exiting...")

	pwm.stop()
	gpio.setcfg(pwm_port, gpio.OUTPUT)
	gpio.output(pwm_port, gpio.LOW)
